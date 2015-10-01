import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;


public class LexicalAnalyzer
{

	private List<Token> tokenList;
	
	/**
	 * @param fileName - cannot be null & must have positive length
	 * @throws FileNotFoundException 
	 * @throws LexicalException 
	 * @throws IllegalArgumentException ("invalid file name argument");
	 */
	public LexicalAnalyzer(String fileName) throws FileNotFoundException, LexicalException
	{
		if (fileName == null || fileName.length() == 0)
			throw new IllegalArgumentException ("invalid file name argument");
		tokenList = new ArrayList<Token>();
		int lineNumber = 0;
		Scanner input = new Scanner (new File (fileName));
		while (input.hasNext())
		{
			lineNumber++;
			processLine (input.nextLine(), lineNumber);
		}
		tokenList.add(new Token (TokenType.EOS_TOK, "EOS", lineNumber + 1, 1));
		input.close();
	}

	private void processLine(String line, int lineNumber) throws LexicalException
	{
		assert line != null;
		assert lineNumber > 0;
		int index = skipWhiteSpace (line, 0);
		while (index < line.length())
		{
			String lexeme = getNextLexeme (line, lineNumber, index);
			lexeme = lexeme.toLowerCase();
			TokenType tokType = getTokenType (lexeme, lineNumber, index);
			index += lexeme.length();
			tokenList.add(new Token (tokType, lexeme, lineNumber, index + 1));
			index = skipWhiteSpace (line, index);
		}
	}

	private TokenType getTokenType(String lexeme, int lineNumber, int index) throws LexicalException
	{
		assert lexeme != null;
		assert lexeme.length() > 0;
		assert lineNumber > 0;
		assert index >= 0;
		TokenType tokType = TokenType.EOS_TOK;
		if (Character.isLetter(lexeme.charAt(0)))
			if (lexeme.length() == 1)
				tokType = TokenType.ID_TOK;
			else if (lexeme.equals("feature"))
				tokType = TokenType.FEATURE_TOK;
			else if (lexeme.equals("end"))
				tokType = TokenType.END_TOK;
			else if (lexeme.equals("if"))
				tokType = TokenType.IF_TOK;
			else if (lexeme.equals("print"))
				tokType = TokenType.PRINT_TOK;
			else if (lexeme.equals("loop"))
				tokType = TokenType.LOOP_TOK;
			else if (lexeme.equals("until"))
				tokType = TokenType.UNTIL_TOK;
			else if (lexeme.equals("from"))
				tokType = TokenType.FROM_TOK;
			else if (lexeme.equals("is"))
				tokType = TokenType.IS_TOK;
			else if (lexeme.equals("do"))
				tokType = TokenType.DO_TOK;
			else if (lexeme.equals ("else"))
				tokType = TokenType.ELSE_TOK;
			else if (lexeme.equals("then"))
				tokType = TokenType.THEN_TOK;
			else
				throw new LexicalException ("invalid identifier at row " +
					lineNumber + " and column " + (index + 1));
		else if (Character.isDigit(lexeme.charAt(0)))
			if (allDigits (lexeme))
				tokType = TokenType.LIT_INT_TOK;
			else
				throw new LexicalException ("invalid integer constant at row " +
					lineNumber + " and column " + (index + 1));
		else if (lexeme.equals (":="))
			tokType = TokenType.ASSIGN_TOK;
		else if (lexeme.equals("+"))
			tokType = TokenType.ADD_TOK;
		else if (lexeme.equals("-"))
			tokType = TokenType.SUB_TOK;
		else if (lexeme.equals ("*"))
			tokType = TokenType.MUL_TOK;
		else if (lexeme.equals ("/"))
			tokType = TokenType.DIV_TOK;
		else if (lexeme.equals("="))
			tokType = TokenType.EQ_TOK;
		else if (lexeme.equals("/="))
			tokType = TokenType.NE_TOK;
		else if (lexeme.equals ("<"))
			tokType = TokenType.LT_TOK;
		else if (lexeme.equals ("<="))
			tokType = TokenType.LE_TOK;
		else if (lexeme.equals (">"))
			tokType = TokenType.GT_TOK;
		else if (lexeme.equals (">="))
			tokType = TokenType.GE_TOK;
		else if (lexeme.equals("("))
			tokType = TokenType.LEFT_PAREN_TOK;
		else if (lexeme.equals(")"))
			tokType = TokenType.RIGHT_PAREN_TOK;
		else
			throw new LexicalException ("invalid lexeme at row " +
				lineNumber + " and column " + (index + 1));
		return tokType;
	}

	private boolean allDigits(String s)
	{
		assert s != null;
		int index = 0;
		while (index < s.length() && Character.isDigit(s.charAt(index)))
			index++;
		return index >= s.length();
	}

	private String getNextLexeme(String line, int lineNumber, int index)
	{
		assert line != null;
		assert lineNumber > 0;
		assert index >= 0;
		int i = index;
		while (i < line.length() && !Character.isWhitespace(line.charAt(i)))
			i++;
		return line.substring(index, i);
	}

	private int skipWhiteSpace(String line, int index)
	{
		assert line != null;
		assert index >= 0;
		int i = index;
		while (i < line.length() && Character.isWhitespace(line.charAt(i)))
			i++;
		return i;
	}

	/**
	 * precondition: there is another token
	 * @return copy of next token
	 * @throws LexicalException if there is not another token
	 */
	public Token getLookaheadToken() throws LexicalException
	{
		if (tokenList.isEmpty())
			throw new LexicalException ("no more tokens");
		return tokenList.get(0);
	}

	/**
	 * precondition: there is another token
	 * postcondition: removed token is removed
	 * @return next token
	 * @throws LexicalException if there is not another token
	 */
	public Token getNextToken() throws LexicalException
	{
		if (tokenList.isEmpty())
			throw new LexicalException ("no more tokens");
		return tokenList.remove(0);
	}

}
