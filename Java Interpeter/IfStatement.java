
public class IfStatement implements Statement
{
	private BooleanExpression expr;
	
	private Compound com1, com2;

	/**
	 * @param expr - cannot be null
	 * @param com1 - cannot be null
	 * @param com2 - cannot be null
	 * @throws IllegalArgumentException if any precondition is not satisfied
	 */
	public IfStatement(BooleanExpression expr, Compound com1, Compound com2)
	{
		if (expr == null)
			throw new IllegalArgumentException ("null BooleanExpression argument");
		if (com1 == null || com2 == null)
			throw new IllegalArgumentException ("null Compound argument");
		this.expr = expr;
		this.com1 = com1;
		this.com2 = com2;
	}

	@Override
	public void execute()
	{
		if (expr.evaluate())
			com1.execute();
		else
			com2.execute();		
	}

}
