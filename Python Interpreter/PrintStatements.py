class PrintStatement(object):
    def __init__(self, expr):
        '''
        Constructor
        '''
        if (expr is None):
            raise Exception("null expression argument")
        self.expr = expr
        
    def execute(self):
        print(self.expr.evaluate())
        