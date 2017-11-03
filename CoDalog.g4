
grammar CoDalog;

/*
PARSER RULES
*/

DatalogProgram	    : SchemaList  (ClauseList)* ;

SchemaList          : 'SCHEMA :' Schema*;

Schema              : Predicate '(' VariableList ')';

ClauseList          : RuleList | FactList | GoalList;

RuleList            : 'RULES :' ( Rule | Rule* ) ;

FactList            : 'FACTS :' ( Fact | Fact* ) ;

GoalList            : 'GOALS:'  (Goal | Goal* ) ;

Fact                : Predicate '(' ConstantList ')' PERIOD;  //Atomic formula of FOL and each fact of DatalogProgram is ground

Rule                : Head ':-' Body PERIOD ;   //When more than or equal to one literal in the body

Goal                : '?-' Body PERIOD ;       //When only one literal in the body

Head                : Literal ;

Body                : LiteralList PERIOD  ;

LiteralList         : Literal | Literal (',' Literal)*;

Literal             : Predicate '(' TermList ')';

Predicate           : LOWERCASE | Predicate VarChars ;           //Predicate symbol must start with Lowercase character

TermList            : Term | Term (',' Term)*;

Term                : Constant | Variable;

BuiltinExp          : Variable Operator Constant;

Operator            :  '>' | '<' | '=' | '!='  | '>=' | '<=' ;

VariableList        : Variable | Variable (',' Variable)*;

Variable            : UPPERCASE | Variable VarChars;   //Variable must start with an uppercase letter

VarChars            : LOWERCASE | UPPERCASE;

ConstantList        : Constant | Constant (',' Constant)*;

Constant            : LOWERCASE | Numbers | Constant ConstChars;  //Constant must start with Lowercase letter

ConstChars          : LOWERCASE | UPPERCASE | Numbers;

Comment             : '#' Words ~( NEWLINE) |  '#|' Words '|#' ;

/*LEXER RULES */

Words               : String | Words ' ' String;

String              : Character | String Character;

Character           : UPPERCASE | LOWERCASE | SPECIAL | Numbers ;

Numbers             : DIGIT | Numbers DIGIT;

PERIOD              : '.';

fragment SPECIAL    : '+' | '-' | '*' | '/' | '\\' | '^' | '~' | ':' | '.' | '?' | '#'| '$' | '&';

fragment LOWERCASE  : [a-z] ;   //rules fragments: they are reusable building blocks for lexer rules.

fragment UPPERCASE  : [A-Z] ;

fragment DIGIT      : [0-9] ;

WHITESPACE          : (' ' | '\t') ;

NEWLINE             : ('\r'? '\n' | '\r')+ ;
