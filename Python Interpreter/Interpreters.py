from Parsers import Parser
from LexicalExceptions import LexicalException
from ParserExceptions import ParserException
import traceback

if __name__ == '__main__':
    try:
        test = "test2.e"
        p = Parser(test)
        feat = p.parse()
        feat.execute()
    
    except FileNotFoundError:
        print("File not found")
        traceback.print_exception()
    
    except LexicalException as e:
        print(e.message)
    
    except ParserException as e:
        print(e.message)
        
    except Exception:
        print("An unknown error has occurred ")
        traceback.print_exc()