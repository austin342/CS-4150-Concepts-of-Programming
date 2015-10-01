class Memory(object):
    mem = [0] * 26
    
    def __init__(self, var, value):
        self.value = value
        self.var = var
        
    def store(self, var, value):
        if (var is None):
            raise Exception("null Id argument")
        self.mem[self.getIndex(var)] = value
        
    # @param var - cannot be null.
    # @returns value of var. 
    # @throws Exception if preconditions are not met. 
    def fetch(self, var):
        if (var is None):
            raise Exception("null Id argument")
        return self.mem[self.getIndex(var)]
      
    # @ param var - cannot be null.
    # @ assertion if the precondition is not met.  
    def getIndex(self, var):
        assert var != None
        ch = (ord(var)) - (ord('a'))        
        return ch
        