from ArithmeticOperators import ArithmeticOperator
from Expressions import Expression

class BinaryExpression(Expression):
    # @param - op cannot be null
    # @param - expr 1 cannot be null
    # @param - expr 2 cannot be null
    # @throws Exception if preconditions are not met. 
    
    def __init__(self, op, expr1, expr2):
        '''
        Constructor
        '''
        if (op is None):
            raise Exception("Null arithmetic operator argument")
        if (expr1 or expr2 is None):
            raise Exception("Null expression argument")
        self.op = op
        self.expr1 = expr1
        self.expr2 = expr2
        
    #@throws Exception if there is no valid binary expression.
    #@returns value
    def evaluate(self):
        value = 0
        operator = ArithmeticOperator
        if (self.op == operator.ADD_OP ):
            value = self.expr1.evaluate() + self.expr2.evaluate()
        elif(self.op == operator.SUB_OP):
            value = self.expr1.evaluate - self.expr2.evaluate()
        elif(self.op == operator.MUL_OP):
            value = self.expr1.evaluate() * self.expr2.evaluate()
        elif(self.op == operator.DIV_OP):
            value = self.expr1.evaluate() / self.expr2.evaluate()
        else:
            raise Exception("invalid binary expression")
        return value
        
        
        