class Feature(object):
    # @param comp - cannot be null.
    # @throws Exception if precondition is not met. 
    def __init__(self, comp):
        '''
        Constructor
        '''
        if (comp is None):
            raise Exception("Null compound argument")
        self.comp = comp
        
    def execute(self):
        self.comp.execute()
        