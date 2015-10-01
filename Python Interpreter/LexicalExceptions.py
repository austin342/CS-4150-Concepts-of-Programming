class LexicalException(Exception):
    def __init__(self, message):
        '''
        Constructor
        '''
        self.message = message
        print(self.message)
        