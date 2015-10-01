
public class BooleanExpression
{

	private RelationalOperator op;
	
	private Expression expr1, expr2;
	
	/**
	 * @param op - cannot be null
	 * @param expr1 - cannot be null
	 * @param expr2 - cannot be null
	 * @throws IllegalArgumentException if any precondition is not satisfied
	 */
	public BooleanExpression(RelationalOperator op, Expression expr1,
			Expression expr2)
	{
		if (op == null)
			throw new IllegalArgumentException ("null RelationalOperator argument");
		if (expr1 == null || expr2 == null)
			throw new IllegalArgumentException ("null Expression argument");
		this.op = op;
		this.expr1 = expr1;
		this.expr2 = expr2;
	}
	
	public boolean evaluate ()
	{
		boolean value = false;
		switch (op)
		{
			case EQ_OP:
				value = expr1.evaluate() == expr2.evaluate();
				break;
			case NE_OP:
				value = expr1.evaluate() != expr2.evaluate();
				break;
			case GT_OP:
				value = expr1.evaluate() > expr2.evaluate();
				break;
			case GE_OP:
				value = expr1.evaluate() >= expr2.evaluate();
				break;
			case LT_OP:
				value = expr1.evaluate() < expr2.evaluate();
				break;
			case LE_OP:
				value = expr1.evaluate() <= expr2.evaluate();
				break;
		}
		return value;
	}

}
