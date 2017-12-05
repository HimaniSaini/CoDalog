grammar CoDalog;

prog		    :  (clause (NEWLINE)*)* EOF ;

clause		    :  goal|fact|e_rule ;

e_rule 		    :   predicate (WS)* RULESIGN (WS)* body  PERIOD;

fact                :	 atom constantList RIGHTBRAK PERIOD;

goal		    :   GOALSIGN atom termList RIGHTBRAK PERIOD;

body		    :  predicate |(predicate (WS)*  COMMA  (WS)* predicate)*;

predicate           : 	atom variableList RIGHTBRAK;

atom      	    :   LW LEFTBRAK ;

termList	    :  term| (term (WS)*  (COMMA (WS)* term)*)* ;

constantList	    :  constant| (constant (WS)*  (COMMA (WS)* constant)*)* ;

variableList	    :  (variable (WS)* (COMMA (WS)* variable)*)* | variable  ;

term          : UW | LW | DIGIT;

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


LC		  : ('a'..'z')|'_' ;

UC  		  : ('A'..'Z') ;

DIGIT      	  : ('0'..'9')+ ;

NEWLINE 	  :'\r'? '\n' ;

WS		  : (' ' | '\t')+ ;
