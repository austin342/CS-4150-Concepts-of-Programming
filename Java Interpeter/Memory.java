
public class Memory
{

	private static int[] mem = new int[26];
	
	/**
	 * @param var - cannot be null
	 * @param value
	 * @throws IllegalArgumentException if var is null
	 */
	public static void store(Id var, int value)
	{
		if (var == null)
			throw new IllegalArgumentException ("null Id argument");
		mem[getIndex(var)] = value;
	}

	/**
	 * @param var - cannot be null
	 * @return value stored at memory location for var
	 * @throws IllegalArgumentException if var is null
	 */
	public static int fetch(Id var)
	{
		if (var == null)
			throw new IllegalArgumentException ("null Id argument");
		return mem[getIndex(var)];
	}
	
	private static int getIndex (Id var)
	{
		assert var != null;
		char ch = var.getCh();
		return ch - 'a';
	}

}
