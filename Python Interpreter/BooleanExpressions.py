from RelationalOperators import RelationalOperator


class BooleanExpression(object):
    # @param op - cannot be null.
    # @param expr1 - cannot be null.
    # @param expr2 - cannot be null.
    # @throws Exception if the preconditions are not met.

    def __init__(self, op, expr1, expr2):
        '''
        Constructor
        '''
        if (op is None):
            raise Exception("Null arithmetic operator argument")
        if (expr1 or expr2 is None):
            
            '''
                expr1 or expr2 is not valid syntax to accomplish what you want
            '''
            raise Exception("Null expression argument")
        self.op = op
        self.expr1 = expr1
        self.expr2 = expr2
        
    def evaluate(self):
        value = 0
        operator = RelationalOperator
         
        if (self.op is operator.EQ_OP):
            value = self.expr1.evaluate() == self.expr2.evaluate()
        elif (self.op is operator.NE_OP):
            value = self.expr1.evaluate() != self.expr2.evaluate()
        elif (self.op is operator.GT_OP):
            value = self.expr1.evaluate() > self.expr2.evaluate()
        elif (self.op is operator.GE_OP):
            value = self.expr1.evaluate() >= self.expr2.evaluate()
        elif (self.op is operator.LT_OP):
            value = self.expr1.evaluate() < self.expr2.evaluate()
        elif (self.op is operator.LE_OP):
            value = self.expr1.evaluate() <= self.expr2.evaluate()
        else:
            raise Exception("Invalid relational operator argument")
        return value

        
        