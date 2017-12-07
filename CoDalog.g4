grammar CoDalog;

prog		    :  (clause (NEWLINE)*)+ ;

clause		    :  goal|fact|e_rule ;

e_rule 		    :   predicate (WS)* RULESIGN (WS)* body (WS)* (COMMA (WS)* bp (WS)*  (COMMA (WS)*  bp)*)* (WS)* PERIOD;

fact                :	 atom constantList RIGHTBRAK PERIOD;

goal		    :   GOALSIGN atom termList RIGHTBRAK PERIOD;

body		    :  predicate |(predicate (WS)*  COMMA  (WS)* predicate)*;

predicate           : 	atom variableList RIGHTBRAK;

atom      	    :   LW LEFTBRAK ;

bp           :    variable (WS)* op (WS)* term;

termList	    :  term| (term (WS)*  (COMMA (WS)* term)*)* ;

constantList	    :  constant| (constant (WS)*  (COMMA (WS)* constant)*)* ;

variableList	    :  (variable (WS)* (COMMA (WS)* variable)*)* | variable  ;

term          : variable | constant;

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

op:       '=='|'!='|'<'|'>'|'>='|'<=';


LC		  : ('a'..'z')|'_' ;

UC  		  : ('A'..'Z') ;

DIGIT      	  : ('0'..'9')+ ;

NEWLINE 	  :'\r'? '\n' ;

WS		  : (' ' | '\t')+ ;
