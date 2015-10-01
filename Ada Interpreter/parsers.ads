with Lexical_Analyzers, Features;
use Lexical_Analyzers, Features;

package Parsers is

   parser_exception: exception;

   type Parser is private;

   function create_parser (file_name: in String) return Parser;

   procedure parse (p: in out Parser; f: out Feature);

private
   type Parser is record
      lex: Lexical_Analyzer;
   end record;

end Parsers;
