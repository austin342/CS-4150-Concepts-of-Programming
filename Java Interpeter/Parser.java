import java.io.FileNotFoundException;


public class Parser
{

	private LexicalAnalyzer lex;
	
	/**
	 * @param fileName - cannot be null & must have length >= 1
	 * @throws FileNotFoundException 
	 * @throws LexicalException 
	 * @throws IllegalArgumentException is precondition is not satisified
	 */
	public Parser (String fileName) throws FileNotFoundException, LexicalException
	{
		if (fileName == null || fileName.length() == 0)
			throw new IllegalArgumentException ("invalid file name argument");
		lex = new LexicalAnalyzer (fileName);
	}
	
	public Feature parse () throws ParserException
	{
		Token tok = getNextToken ();
		match (tok, TokenType.FEATURE_TOK);
		Id var = getId ();
		tok = getNextToken ();
		match (tok, TokenType.IS_TOK);
		tok = getNextToken ();
		match (tok, TokenType.DO_TOK);
		Compound com = getCompound ();
		tok = getNextToken ();
		match (tok, TokenType.END_TOK);
		tok = getNextToken ();
		if (tok.getTokType() != TokenType.EOS_TOK)
			throw new ParserException ("garbage at end of program");
		return new Feature (com);
	}

	private Compound getCompound() throws ParserException
	{
		Compound com = new Compound();
		Statement s = getStatement();
		com.add (s);
		Token tok = getLookaheadToken ();
		while (isValidStartOfStatement (tok))
		{
			s = getStatement ();
			com.add(s);
			tok = getLookaheadToken ();
		}
		return com;
	}

	private boolean isValidStartOfStatement(Token tok)
	{
		assert tok != null;
		return tok.getTokType() == TokenType.ID_TOK || tok.getTokType() == TokenType.IF_TOK
			|| tok.getTokType() == TokenType.PRINT_TOK || tok.getTokType() == TokenType.FROM_TOK;
	}

	private Statement getStatement() throws ParserException
	{
		Statement s;
		Token tok = getLookaheadToken();
		if (tok.getTokType() == TokenType.ID_TOK)
			s = getAssignmentStatement();
		else if (tok.getTokType() == TokenType.IF_TOK)
			s = getIfStatement ();
		else if (tok.getTokType() == TokenType.PRINT_TOK)
			s = getPrintStatement ();
		else if (tok.getTokType() == TokenType.FROM_TOK)
			s = getLoopStatement();
		else
			throw new ParserException ("statement expected at row " + tok.getRowNumber() +
				" and column " + tok.getColumnNumber());		
		return s;
	}

	private LoopStatement getLoopStatement() throws ParserException
	{
		Token tok = getNextToken ();
		match (tok, TokenType.FROM_TOK);
		AssignmentStatement s = getAssignmentStatement ();
		tok = getNextToken ();
		match (tok, TokenType.UNTIL_TOK);
		BooleanExpression expr = getBooleanExpression ();
		tok = getNextToken ();
		match (tok, TokenType.LOOP_TOK);
		Compound com = getCompound();
		tok = getNextToken ();
		match (tok, TokenType.END_TOK);
		return new LoopStatement (s, expr, com);
	}

	private PrintStatement getPrintStatement() throws ParserException
	{
		Token tok = getNextToken();
		match (tok, TokenType.PRINT_TOK);
		tok = getNextToken ();
		match (tok, TokenType.LEFT_PAREN_TOK);
		Expression expr = getExpression ();
		tok = getNextToken ();
		match (tok, TokenType.RIGHT_PAREN_TOK);
		return new PrintStatement (expr);
	}

	private IfStatement getIfStatement() throws ParserException
	{
		Token tok = getNextToken ();
		match (tok, TokenType.IF_TOK);
		BooleanExpression expr = getBooleanExpression ();
		tok = getNextToken ();
		match (tok, TokenType.THEN_TOK);
		Compound com1 = getCompound();
		tok = getNextToken ();
		match (tok, TokenType.ELSE_TOK);
		Compound com2 = getCompound();
		tok = getNextToken ();
		match (tok, TokenType.END_TOK);
		return new IfStatement (expr, com1, com2);
	}

	private AssignmentStatement getAssignmentStatement() throws ParserException
	{
		Id var = getId();
		Token tok = getNextToken ();
		match (tok, TokenType.ASSIGN_TOK);
		Expression expr = getExpression();
		return new AssignmentStatement (var, expr);
	}

	private Expression getExpression() throws ParserException
	{
		Expression expr;
		Token tok = getLookaheadToken ();
		if (tok.getTokType() == TokenType.ID_TOK)
			expr = getId();
		else if (tok.getTokType() == TokenType.LIT_INT_TOK)
			expr = getLiteralInteger();
		else
		{
			ArithmeticOperator op = getArithmeticOperator();
			Expression expr1 = getExpression ();
			Expression expr2 = getExpression();
			expr = new BinaryExpression (op, expr1, expr2);
		}		
		return expr;
	}

	private Expression getLiteralInteger() throws ParserException
	{
		Token tok = getNextToken ();
		match (tok, TokenType.LIT_INT_TOK);
		int value = 0;
		try
		{
			value = Integer.parseInt(tok.getLexeme());
		}
		catch (NumberFormatException e)
		{
			throw new ParserException ("literal integer expected at row " + tok.getRowNumber() +
				" and column " + tok.getColumnNumber());
		}
		return new LiteralInteger (value);
	}

	private Id getId() throws ParserException
	{
		Token tok = getNextToken ();
		match (tok, TokenType.ID_TOK);
		if (tok.getLexeme().length() != 1)
			throw new ParserException ("invalid identifier at row " + tok.getRowNumber() +
					" and column " + tok.getColumnNumber());
		return new Id (tok.getLexeme().charAt(0));
	}

	private ArithmeticOperator getArithmeticOperator() throws ParserException
	{
		ArithmeticOperator op;
		Token tok = getNextToken ();
		if (tok.getTokType() == TokenType.ADD_TOK)
			op = ArithmeticOperator.ADD_OP;
		else if (tok.getTokType() == TokenType.SUB_TOK)
			op = ArithmeticOperator.SUB_OP;
		else if (tok.getTokType() == TokenType.MUL_TOK)
			op = ArithmeticOperator.MUL_OP;
		else if (tok.getTokType() == TokenType.DIV_TOK)
			op = ArithmeticOperator.DIV_OP;
		else
			throw new ParserException ("arithmetic operator expected at row " + tok.getRowNumber() +
					" and column " + tok.getColumnNumber());
		return op;
	}

	private BooleanExpression getBooleanExpression() throws ParserException
	{
		RelationalOperator op = getRelationalOperator ();
		Expression expr1 = getExpression ();
		Expression expr2 = getExpression ();
		return new BooleanExpression (op, expr1, expr2);
	}

	private RelationalOperator getRelationalOperator() throws ParserException
	{
		RelationalOperator op;
		Token tok = getNextToken ();
		if (tok.getTokType() == TokenType.EQ_TOK)
			op = RelationalOperator.EQ_OP;
		else if (tok.getTokType() == TokenType.NE_TOK)
			op = RelationalOperator.NE_OP;
		else if (tok.getTokType() == TokenType.GT_TOK)
			op = RelationalOperator.GT_OP;
		else if (tok.getTokType() == TokenType.GE_TOK)
			op = RelationalOperator.GE_OP;
		else if (tok.getTokType() == TokenType.LT_TOK)
			op = RelationalOperator.LT_OP;
		else if (tok.getTokType() == TokenType.LE_TOK)
			op = RelationalOperator.LE_OP;
		else
			throw new ParserException ("relational operator expected at row " + tok.getRowNumber() +
					" and column " + tok.getColumnNumber());
		return op;
	}

	private void match(Token tok, TokenType tokType) throws ParserException
	{
		assert tok != null;
		assert tokType != null;
		if (tok.getTokType() != tokType)
			throw new ParserException (tokType.name() + " expected at row " + tok.getRowNumber() +
					" and column " + tok.getColumnNumber());

	}

	private Token getLookaheadToken() throws ParserException
	{
		Token tok;		
		try
		{
			tok = lex.getLookaheadToken ();
		}
		catch (LexicalException e)
		{
			throw new ParserException (e.getMessage());
		}
		return tok;
	}

	private Token getNextToken() throws ParserException
	{
		Token tok;		
		try
		{
			tok = lex.getNextToken ();
		}
		catch (LexicalException e)
		{
			throw new ParserException (e.getMessage());
		}
		return tok;
	}
}
