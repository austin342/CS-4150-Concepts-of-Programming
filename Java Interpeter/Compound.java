import java.util.ArrayList;
import java.util.List;


public class Compound
{

	private List<Statement> stmts;
	
	public Compound ()
	{
		stmts = new ArrayList<Statement>();
	}
	
	/**
	 * @param s - cannot be null
	 * @throws IllegalArgumentException if s is null
	 */
	public void add(Statement s)
	{
		if (s == null)
			throw new IllegalArgumentException ("null Statement argument");
		stmts.add(s);
	}
	
	public void execute()
	{
		for (Statement s: stmts)
			s.execute();
	}

}
