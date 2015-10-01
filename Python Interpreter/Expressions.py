import abc

class Expression(object):
    def __init__(self, expr):
        '''
        Constructor
        '''
        
    @abc.abstractmethod
    def evaluate(self):
        pass
    