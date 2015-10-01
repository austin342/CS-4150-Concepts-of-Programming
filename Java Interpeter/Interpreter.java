import java.io.FileNotFoundException;


public class Interpreter
{

	public static void main(String[] args)
	{
		try
		{
			Parser p = new Parser ("test4.e");
			Feature f = p.parse();
			f.execute();
		}
		catch (FileNotFoundException e)
		{
			System.out.println (e.getMessage());
			e.printStackTrace();
		}
		catch (LexicalException e)
		{
			System.out.println (e.getMessage());
			e.printStackTrace();
		}
		catch (ParserException e)
		{
			System.out.println (e.getMessage());
			e.printStackTrace();
		}
		catch (Exception e)
		{
			System.out.println (e.getMessage());
			e.printStackTrace();
			System.out.println ("unknown error occurred - terminating");
		}
	}

}
