
public class LoopStatement implements Statement
{

	private AssignmentStatement s;
	
	private BooleanExpression expr;
	
	private Compound com;
	
	/**
	 * @param s - cannot be null
	 * @param expr - cannot be null
	 * @param com - cannot be null
	 * @throws new IllegalArgumentException if any precondition is not satisfied
	 */
	public LoopStatement(AssignmentStatement s, BooleanExpression expr,
			Compound com)
	{
		if (s == null)
			throw new IllegalArgumentException ("null AssignmentStatement argument");
		if (expr == null)
			throw new IllegalArgumentException  ("null BooleanExpression argument");
		if (com == null)
			throw new IllegalArgumentException ("null Compound argument");
		this.s = s;
		this.expr = expr;
		this.com = com;
	}

	@Override
	public void execute()
	{
		for (s.execute();!expr.evaluate();)
			com.execute();
	}

}
