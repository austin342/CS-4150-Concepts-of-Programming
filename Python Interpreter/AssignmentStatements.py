from Memorys import Memory
from Statements import Statement

class AssignmentStatement(Statement):
    # @param var - cannot be null.
    # @ param expr - cannot be null.

    def __init__(self, var, expr):
        '''
        Constructor
        '''
        if (var is None):
            raise Exception("null Id argument")       
        
        if (expr is None):
            raise Exception("null expression argument")
        self.var = var
        self.expr = expr

    def execute(self):
        m = Memory(self.var, self.expr)
        m.store(self.var.ch, self.expr.evaluate())