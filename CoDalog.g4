grammar CoDalog;

//start               : DATALOGPROGRAM;

prog		    :  (clause (NEWLINE)*)* EOF ;

clause		    :  goal|fact|e_rule ;// predicate_name ;//rule|fact|goal| LW;//| ConstantList;

e_rule 		    :   predicate WS RULESIGN WS body PERIOD;//(fact | predicate | predicate (COMMA fact | COMMA predicate)* | fact (COMMA predicate| COMMA fact)*) PERIOD;

fact                :	 atom constantList RIGHTBRAK PERIOD;

goal		    :   GOALSIGN atom termList RIGHTBRAK PERIOD;

body		    :  predicate |(predicate COMMA predicate)*;// |(predicate COMMA predicate COMMA predicate)*;

predicate           : 	atom variableList RIGHTBRAK;

atom      	    :   LW LEFTBRAK ;

termList	    : constantList | variableList;// | constantList COMMA (constantList COMMA| variableList COMMA | WS)* | variableList COMMA (constantList COMMA | variableList COMMA| WS)* ; //| constantList+ | variableList+ ;

constantList	    :  constant| (constant COMMA WS constant)* ;

variableList	    :  (variable (WS)* COMMA (WS)* variable)* | variable  ;

variable	    :   UW;

constant	    :   LW | DIGIT;

UW	            :	UC | UC (UC)+;

LW	            :	LC | LC (LC)+ ;

GOALSIGN	    :	'?-';

RULESIGN	    :	':-';

RIGHTBRAK	    :	')';

LEFTBRAK	    :	'(';

COMMA		    :   ',';

PERIOD             : '.' ;

// SPECIAL    : '+' | '-' | '*' | '/' | '\\' | '^' | '~' | '#'| '$' | '&';

LC		  : ('a'..'z')|'_' ;

UC  		  : ('A'..'Z') ;

DIGIT      	  : ('0'..'9')+ ;

NEWLINE 	  :'\r'? '\n' ;

WS		  : (' ' | '\t')+ ;
