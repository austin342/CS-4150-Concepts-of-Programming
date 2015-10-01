class Token(object):
    global tokType
    global lexeme
    global rowNumber
    global columnNmber
    # @param tokType - cannot be null.
    # @param lexeme - cannot be null.
    # @param rowNumber - cannot be <= 0.
    # @param columnNumber - cannot be <= 0.
    # @throws Exception if preconditions are not met. 
    def __init__(self, tokType, lexeme, rowNumber, columnNumber):
        '''
        Constructor
        '''
        if (tokType is None):
            raise Exception("tokType cannot be null")
        
        if (lexeme is None or len(lexeme) == 0):
            raise Exception("Invalid lexeme argument")
        
        if (rowNumber <= 0):
            raise Exception("Invalid row number argument")
        
        if (columnNumber <= 0):
            raise Exception("Invalid column argument")
        
        self.tokType = tokType
        self.lexeme = lexeme
        self.rowNumber = rowNumber
        self.columnNumber = columnNumber
        
    def getTokType(self):
        return self.tokType
    
    def getLexeme(self):
        return self.lexeme
    
    def getRowNumber(self):
        return self.rowNumber
    
    def getColumnNumber(self):
        return self.columnNumber
    
    
        
        