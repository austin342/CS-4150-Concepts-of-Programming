from LexicalAnalyzers import LexicalAnalyzer
from Tokens import Token
from ParserExceptions import ParserException
from RelationalOperators import RelationalOperator
from TokenTypes import TokenType
from BooleanExpressions import BooleanExpression
from ArithmeticOperators import ArithmeticOperator
from LiteralIntegers import LiteralInteger
from BinaryExpressions import BinaryExpression
from AssignmentStatements import AssignmentStatement
from IfStatements import IfStatement
from LoopStatements import LoopStatement
from Compounds import Compound
from Features import Feature
from Ids import Id
from PrintStatements import PrintStatement


class Parser(object):
    # @param fileName - file name cannot be null
    # @throws Exception if preconditions are not met. 
    def __init__(self, fileName):
        '''
        Constructor
        '''
        if (fileName is None):
            raise Exception("invalid file name argument")
        self.lex = LexicalAnalyzer(fileName)
    
    def parse(self):
        tok = Token #testing this
        
        # You are assigning the address of the init function to tok
        
        tok = self.getNextToken()
        self.match(tok, TokenType.FEATURE_TOK)
        var = Id(self.getId())
        #var = self.getId()
        tok = self.getNextToken()
        self.match(tok, TokenType.IS_TOK)
        tok = self.getNextToken()
        self.match(tok, TokenType.DO_TOK)
        comp = self.getCompound()
        tok = self.getNextToken()
        self.match(tok, TokenType.END_TOK)
        tok = self.getNextToken()
        if (tok.getTokType() != TokenType.EOS_TOK):
            raise ParserException("there is garbage at the end of the program ")
        return Feature(comp)
    
    def getCompound(self):
        comp = Compound()
        s = self.getStatement()
        comp.add(s)
        tok = self.getLookaheadToken()
        while(self.isValidStartOfStatement(tok)):
            s = self.getStatement()
            comp.add(s)
            tok = self.getLookaheadToken()
        return comp
    
    #@param tok - cannot be null.
    #@assertion if precondition is not met.   
    def isValidStartOfStatement(self, tok):
        assert tok != None
        #tok = Token
        return (tok.getTokType() == TokenType.ID_TOK or tok.getTokType() == TokenType.IF_TOK 
                or tok.getTokType() == TokenType.PRINT_TOK or tok.getTokType() == TokenType.FROM_TOK)

    #@throws Exception if we have no expected statements. 
    def getStatement(self):
        tok = self.getLookaheadToken()
        if(tok.getTokType() == TokenType.ID_TOK):
            s = self.getAssignmentStatement()
        elif (tok.getTokType() == TokenType.IF_TOK):
            s = self.getIfStatement()
        elif (tok.getTokType() == TokenType.PRINT_TOK):
            s = self.getPrintStatement()
        elif (tok.getTokType() == TokenType.FROM_TOK):
            s = self.getLoopStatement()
        else:
            #raise ParserException(tok.getTokType)
            raise ParserException(str(tok.getTokType()) + " statement is expected at row " + str(Token.getRowNumber()) + "and column " + str(Token.getColumnNumber()))
        return s
    
    
    def getLoopStatement(self):
        tok = self.getNextToken()
        self.match(tok, TokenType.FROM_TOK)
        s = self.getAssignmentStatement()
        tok = self.getNextToken()
        self.match(tok, TokenType.UNTIL_TOK)
        expr = self.getBooleanExpression()
        tok = self.getNextToken()
        self.match(tok, TokenType.LOOP_TOK)
        comp = self.getCompound()
        tok = self.getNextToken()
        self.match(tok, TokenType.END_TOK)
        return LoopStatement(s, expr, comp)
        
    def getPrintStatement(self):
        tok = self.getNextToken()
        self.match(tok, TokenType.PRINT_TOK)
        tok = self.getNextToken()
        self.match(tok, TokenType.LEFT_PAREN_TOK)
        expr = self.getExpression()
        tok = self.getNextToken()
        self.match(tok, TokenType.RIGHT_PAREN_TOK)
        return PrintStatement(expr)
        
    def getIfStatement(self):
        tok = self.getNextToken()
        self.match(tok, TokenType.IF_TOK)
        expr = self.getBooleanExpression()
        tok = self.getNextToken()
        self.match(tok, TokenType.THEN_TOKEN)
        comp1 = self.getCompound()
        tok = self.getNextToken()
        self.match(tok, TokenType.ELSE_TOK)
        comp2 = self.getCompound()
        tok = self.getNextToken()
        self.match(tok, TokenType.END_TOK)
        return IfStatement(expr, comp1, comp2)
    
    
    def getAssignmentStatement(self):
        var = self.getId()
        tok = self.getNextToken()
        self.match(tok, TokenType.ASSIGN_TOK)
        expr = self.getExpression()
        return AssignmentStatement(var, expr)
    
    
    def getExpression(self):
        tok = self.getLookaheadToken()
        if (tok.getTokType() == TokenType.ID_TOK):
            expr = self.getId()
        elif (tok.getTokType() == TokenType.LITERAL_INT_TOK):
            expr = self.getLiteralInteger()
        else:
            op = self.getArithmeticOperator()
            expr1 = self.getExpression()
            expr2 = self.getExpression()
            expr = BinaryExpression(op, expr1, expr2)
        return expr
    
    #@throws Exception if we do not find a literal integer when expected. 
    def getLiteralInteger(self):
        tok = self.getNextToken()
        self.match(tok, TokenType.LITERAL_INT_TOK)
        value = 0
        try:
            value = LiteralInteger(tok.getLexeme()) 
        except:
            raise ParserException("literal integer expected at row " + str(tok.getRowNumber()) + 
                                  "and column " + str(tok.getColumnNumber()))
        
        return LiteralInteger(value)
    
    #@throws Exception if invalid identifier is found
    def getId(self):
        tok = self.getNextToken()
        self.match(tok, TokenType.ID_TOK)
        if (len(tok.getLexeme()) != 1):
            raise ParserException("invalid identifier at row " + str(tok.getRowNumber()) + 
                                  "and column " + str(tok.getColumnNumber()))
        return Id(tok.getLexeme())
    
    #throws Exception if no valid arithmetic operator is found
    def getArithmeticOperator(self):
        tok = self.getNextToken()
        if (tok.getTokType() == TokenType.ADD_TOK):
            op = ArithmeticOperator.ADD_OP
        elif (tok.getTokType() == TokenType.SUB_TOK):
            op = ArithmeticOperator.SUB_OP
        elif (tok.getTokType() == TokenType.MUL_TOK):
            op = ArithmeticOperator.MUL_OP
        elif (tok.getTokType() == TokenType.DIV_TOK):
            op = ArithmeticOperator.DIV_OP
        else:
            raise ParserException("arithmetic operator expected at row " + str(tok.getRowNumber()) + 
                                  "and column " + str(tok.getColumnNumber()))
        return op
            
    def getBooleanExpression(self):
        op = self.getRelationalOperator()
        expr1 = self.getExpression()
        expr2 = self.getExpression()
        
        return BooleanExpression(op, expr1, expr2)
    
    #@throws Exception if no valid relational operator is found. 
    def getRelationalOperator(self):
        op = RelationalOperator
        tok = self.getNextToken()
        
        if (tok.getTokType() is TokenType.EQ_TOK):
            op = RelationalOperator.EQ_OP
        elif (tok.getTokType() is TokenType.NE_TOK):
            op = RelationalOperator.NE_OP      
        elif (tok.getTokType() is TokenType.GT_TOK):
            op = RelationalOperator.GT_OP
        elif (tok.getTokType() is TokenType.GE_TOK):
            op = RelationalOperator.GE_OP
        elif (tok.getTokType() is TokenType.LT_TOK):
            op = RelationalOperator.LT_OP
        elif (tok.getTokType() is TokenType.LE_TOK):
            op = RelationalOperator.LE_OP
        else:
            raise ParserException("relational operator expected at row " + Token.getRowNumber() + 
                                  "and column " + Token.getColumnNumber())
        return op
    
    #@param tok - cannot be null.
    #@param tokType - cannot be null
    #@assertion if preconditions not met.
    #@throws Exception if we do not find expected token. 
    def match(self, tok, tokType):
        assert tok != None
        assert tokType != None
        if (tok.getTokType() != tokType):
            #print(tok.getTokType, "expected", tokType) 
            raise ParserException(tokType)
       # else:
            #print(tok.getTokType, "match", tokType)

        #if (tok != tokType):
            #raise ParserException(str(tok.getTokType()) + "expected at row " + str(Token.getRowNumber()) + 
            #                     "and column " + str(tok.getColumnNumber()))
        #break
    def getLookaheadToken(self):
        try:
            tok = self.lex.getLookaheadToken()
        except:
            raise ParserException("look ahead token error")
        return tok
        
    def getNextToken(self):
        try:
            tok = self.lex.getNextToken()
        except:
            raise ParserException("get next token error")
        return tok 
      
        
    
    
        
        
        
        
        