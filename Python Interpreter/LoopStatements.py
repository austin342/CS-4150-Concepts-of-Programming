class LoopStatement(object):
    # @param stmt - cannot be null.
    # @param expr - cannot be null.
    # @param comp - cannot be null.
    # @throws Exception if preconditions are not met. 
    def __init__(self, stmt, expr, comp):
        '''
        Constructor
        '''
        if (stmt is None):
            raise Exception("null assignment statement argument")
        if (expr is None):
            raise Exception("null boolean expression argument")
        if (comp is None):
            raise Exception("null compound argument")
        self.stmt = stmt
        self.expr = expr
        self.comp = comp
        
    def execute(self):
        while (self.stmt.execute() and not self.expr.evaluate()):
            self.comp.execute() 
            
        # problems with logic here    
        