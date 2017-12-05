grammar CoDalog;

//start               : DATALOGPROGRAM;

prog		    :  (clause (NEWLINE)*)* EOF ;

clause		    :  goal|fact|e_rule ;// predicate_name ;

e_rule 		    :   predicate (WS)* RULESIGN (WS)* body  PERIOD;

fact                :	 atom constantList RIGHTBRAK PERIOD;

//bp           :    variable (WS)* BPS (WS)* variable | variable (WS)* BPS (WS)* constant ;

//bpa          :    variable (WS)* Ar (WS)* variable (WS)* BPS (WS)* variable | variable BPS constant;

goal		    :   GOALSIGN atom termList RIGHTBRAK PERIOD;

body		    :  predicate |(predicate (WS)*  COMMA  (WS)* predicate)*;// |(predicate COMMA predicate COMMA predicate)*;

predicate           : 	atom variableList RIGHTBRAK;

atom      	    :   LW LEFTBRAK ;

termList	    : constantList | variableList;// | constantList COMMA (constantList COMMA| variableList COMMA | WS)* | variableList COMMA (constantList COMMA | variableList COMMA| WS)* ; //| constantList+ | variableList+ ;

constantList	    :  constant| (constant (WS)*  (COMMA (WS)* constant)*)* ;

variableList	    :  (variable (WS)* (COMMA (WS)* variable)*)* | variable  ;

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

//BPS: '=' | '<' | '>' | '>=' | '<=' | '!='| '+'| '-'| '*';

LC		  : ('a'..'z')|'_' ;

UC  		  : ('A'..'Z') ;

DIGIT      	  : ('0'..'9')+ ;

NEWLINE 	  :'\r'? '\n' ;

WS		  : (' ' | '\t')+ ;
