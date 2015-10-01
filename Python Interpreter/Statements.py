import abc

class Statement(object):
    def __init__(self):
        '''
        Constructor
        '''
    

    @abc.abstractmethod
    def execute(self):
        pass
    