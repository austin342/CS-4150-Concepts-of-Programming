
public class Id implements Expression
{

	private char ch;
	
	public Id(char ch)
	{
		this.ch = ch;
	}

	@Override
	public int evaluate()
	{
		return Memory.fetch (this);
	}

	public char getCh()
	{
		return ch;
	}

}
