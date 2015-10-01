
public class Feature
{

	private Compound com;
	
	/**
	 * @param com - cannot be null
	 * @throws IllegalArgumentException if com is null
	 */
	public Feature(Compound com)
	{
		if (com == null)
			throw new IllegalArgumentException ("null Compound argument");
		this.com = com;
	}
	
	public void execute ()
	{
		com.execute();
	}

}
