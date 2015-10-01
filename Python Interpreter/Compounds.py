class Compound(object):
    def __init__(self):
        '''
        Constructor
        '''
        self.stmts = []

    # @param s - cannot be null.
    # @throws Exception if precondition is not met. 
    def add(self, s):
        if s is None:
            raise Exception("Null statement argument")
        self.stmts.append(s)
    
    def execute(self):
        for s in self.stmts: 
            s.execute()
            