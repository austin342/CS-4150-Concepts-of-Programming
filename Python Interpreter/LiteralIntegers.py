from Expressions import Expression

class LiteralInteger(Expression):
    def __init__(self, value):
        '''
        Constructor
        '''
        self.value = value
    
    def evaluate(self):
        return int(self.value.value)