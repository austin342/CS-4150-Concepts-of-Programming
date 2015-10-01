from Memorys import Memory
from Expressions import Expression

class Id(Expression):
    def __init__(self, ch):
        '''
        Constructor
        '''
        self.ch = ch
        
    def evaluate(self):
        m = Memory(self.ch, None)
        return m.fetch(self.ch) 
    
    def getCh(self):
        return self.ch