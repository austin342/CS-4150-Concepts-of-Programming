from Tokens import Token
from TokenTypes import TokenType
from LexicalExceptions import LexicalException

class LexicalAnalyzer(object):
    #come back and add print tokens for debugging.
    # @param fileName - cannot be null.
    # @throws Exception if precondition is not met. 
    def __init__(self, fileName):
        '''
        Constructor
        '''
        if (fileName is None or len(fileName) == 0):
            raise Exception("invalid file name argument we in lexical analyzers")
        self.tokenList = []
        lineNum = 1
        
        file = open(fileName, "r")
        #print (file.read()) #testing this works as intended 
        
        for line in file:
            self.processLine(line, lineNum)
            lineNum += 1
        tok = Token(TokenType.EOS_TOK, "EOS", lineNum, 1)
        self.tokenList.append(tok)
        file.close() 

    # @param line - cannot be null.
    # @param lineNum - must be > 0.
    # @assertion - if preconditions are not met. 
    def processLine(self, line, lineNum):
        assert line != None
        assert lineNum > 0 
        index = self.skipWhiteSpace(line, 0)
        while (index < len(line)): 
            lexeme = self.getNextLexeme(line, lineNum, index)
            lexeme = lexeme.lower()
            tokType = self.getTokenType(lexeme, lineNum, index)
            index += len(lexeme)
            tempToken = Token(tokType, lexeme, lineNum, index + 1)
            self.tokenList.append(tempToken)
            index = self.skipWhiteSpace(line, index)
    # @param lexeme - cannot be null.
    # @param lineNum - must be greater than 0.
    # @param index - must be >= 0.
    # @assertion - if preconditions are not met. 
    # @throws Exception if there is an invalid lexeme. 
    def getTokenType(self, lexeme, lineNum, index):
        assert lexeme != None
        assert len(lexeme) > 0
        assert lineNum > 0
        assert index >= 0
        tokType = TokenType.EOS_TOK
        if (lexeme[0].isalpha()):
        #if (str.isalpha(lexeme[0])):
            if (len(lexeme) == 1):
                tokType = TokenType.ID_TOK
            elif (lexeme == ("feature")): 
                tokType = TokenType.FEATURE_TOK
            elif (lexeme == ("end")):
                tokType = TokenType.END_TOK
            elif (lexeme == ("if")):
                tokType = TokenType.IF_TOK
            elif (lexeme == ("print")):
                tokType = TokenType.PRINT_TOK
            elif (lexeme == ("loop")):
                tokType = TokenType.LOOP_TOK
            elif (lexeme == ("until")):
                tokType = TokenType.UNTIL_TOK
            elif (lexeme == ("from")):
                tokType = TokenType.FROM_TOK
            elif (lexeme == ("is")):
                tokType = TokenType.IS_TOK
            elif (lexeme == ("do")):
                tokType = TokenType.DO_TOK
            elif (lexeme == ("else")):
                tokType = TokenType.ELSE_TOK
            elif (lexeme == ("then")):
                tokType = TokenType.THEN_TOKEN
            else:
                raise LexicalException("invalid identifier at row " + str(lineNum) + " and column " + str(index + 1))
        elif (lexeme[0].isdigit()):
            if (self.allDigits (lexeme)):
                tokType = TokenType.LITERAL_INT_TOK
            else:
                raise LexicalException("invalid integer constant at row " + str(lineNum) + "and column" + str(index + 1))
        elif (lexeme == (":=")):
            tokType = TokenType.ASSIGN_TOK
        elif (lexeme == ("+")):
            tokType = TokenType.ADD_TOK
        elif (lexeme == ("-")):
            tokType = TokenType.SUB_TOK
        elif (lexeme == ("*")):
            tokType = TokenType.MUL_TOK
        elif (lexeme == ("/")):
            tokType = TokenType.DIV_TOK
        elif (lexeme == ("=")):
            tokType = TokenType.EQ_TOK
        elif (lexeme == ("/=")):
            tokType = TokenType.NE_TOK
        elif (lexeme == ("<")):
            tokType = TokenType.LT_TOK
        elif (lexeme == ("<=")):
            tokType = TokenType.LE_TOK
        elif (lexeme == (">")):
            tokType = TokenType.GT_TOK
        elif (lexeme == (">=")):
            tokType = TokenType.GE_TOK
        elif (lexeme == ("(")):
            tokType = TokenType.LEFT_PAREN_TOK
        elif (lexeme == (")")):
            tokType = TokenType.RIGHT_PAREN_TOK
        else:
            LexicalException("invalid lexeme at row " + str(lineNum) + "and column " + str(index + 1)) 
        
        return tokType
    
    # @param s - cannot be null
    # @assertion if precondition is not met. 
    def allDigits(self, s):
        assert s != None
        index = 0
        while (index < len(s) and s[index].isdigit()):
            index += 1 
        return index >= len(s)

    # @param line - cannot be null.
    # @param lineNum - must be greater than 0.
    # @param index - must be >= 0.
    # @assertion if preconditions are not met. 
    def getNextLexeme(self, line, lineNum, index):
        assert line != None
        assert lineNum > 0
        assert index >= 0
        i = index
        #while (i < len(line) and line[index] != str.isspace(line[index])): #testing is space here vs " "
        while (i < len(line) and str.isspace(line[i]) != True):  
            i += 1               
        return line[index:i] 
    
    # @param line - cannot be null.
    # @param index - must be >= 0.
    # @assertion if preconditions are not met. 
    def skipWhiteSpace(self, line, index):
        assert line != None
        assert index >= 0
        i = index
        while (i < len(line) and line[i].isspace()):
            i += 1            
        return i
    
    def getLookaheadToken(self):
        if (self.tokenList is None):
            raise LexicalException("no more tokens ")
        return self.tokenList[0]
    
    def getNextToken(self):
        if (self.tokenList is None):
            raise LexicalException("No more tokens")
        return self.tokenList.pop(0)
    