from Statements import Statement

class IfStatement(Statement):
    # @param expr - cannot be null.
    # @param comp1 - cannot be null.
    # @param comp2 - cannot be null.
    # @throws Exception if preconditions are not met. 
    def __init__(self, expr, comp1, comp2):
        '''
        Constructor
        '''
        if (expr is None):
            raise Exception("null boolean expression argument")
        if (comp1 is None or comp2 is None):
            raise Exception("null compound argument")
        self.expr = expr
        self.comp1 = comp1
        self.comp2 = comp2
        
    def execute(self):
        if (self.expr.evaluate()):
            self.comp1.execute()
        else:
            self.comp2.execute()
    
        