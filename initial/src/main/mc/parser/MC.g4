grammar MC;

@lexer::header {
from lexererr import *
}

@lexer::members {
def emit(self):
    tk = self.type
    if tk == self.UNCLOSE_STRING:       
        result = super().emit();
        raise UncloseString(result.text);
    elif tk == self.ILLEGAL_ESCAPE:
        result = super().emit();
        raise IllegalEscape(result.text);
    elif tk == self.ERROR_CHAR:
        result = super().emit();
        raise ErrorToken(result.text); 
    else:
        return super().emit();
}

options{
	language=Python3;
}

program : decl+ EOF;
decl : vardecl | funcdecl;

vardecl : primtype varname (COMMA varname)* SEMI;
primtype : BOOLEANTYPE | INTTYPE | FLOATTYPE | STRINGTYPE ;
varname: ID (LS INTLIT RS)?;

funcdecl: returntype ID LB paralist? RB blockstmt;
returntype: primtype | VOIDTYPE | arrptrtype;
arrptrtype : primtype LS RS;
paralist: para (COMMA para)*;    
para: primtype ID (LS RS)?;
blockstmt: LP (vardecl | stmt)* RP; // ?

stmt: ifstmt | dowhilestmt | forstmt | breakstmt | contistmt | returnstmt | expstmt | blockstmt;
ifstmt: IF LB exp RB stmt (ELSE stmt)?;
dowhilestmt: DO stmt+ WHILE exp SEMI;
forstmt:     FOR LB exp SEMI exp SEMI exp RB stmt;    
breakstmt:   BREAK SEMI;
contistmt:   CONTINUE SEMI;
returnstmt:  RETURN exp? SEMI;
expstmt:     exp SEMI;

exp : exp1 ASSIGN exp  | exp1;
exp1: exp1 OROP exp2  | exp2;
exp2: exp2 ANDOP exp3 | exp3;
exp3: exp4 EQUALOP exp4 | exp4;
exp4: exp5 COMPOP exp5 | exp5;
exp5: exp5 (ADDOP | SUBOP) exp6 | exp6;
exp6: exp6 (MULOP | DIVOP | MODOP) exp7 | exp7;
exp7: (SUBOP | NEGOP) exp7 | exp8;    // ?
exp8:   LB exp RB |
        literal |
        ID | 
        funcall |
        elearray | 
        exp8 LS exp RS
    ;

funcall : ID LB (exp (COMMA exp)*)? RB;     //?
elearray: ID LS INTLIT RS;

literal: INTLIT | FLOATLIT | BOOLEANLIT | STRINGLIT ;   
INTLIT: [0-9]+;
FLOATLIT:  [0-9]+'.'[0-9]*([eE]'-'?[0-9]+)?
        |  [0-9]*'.'[0-9]+([eE]'-'?[0-9]+)?
        |  [0-9]+([eE]'-'?[0-9]+)?
        ;
BOOLEANLIT: TRUE | FALSE;

STRINGLIT
        : '"'(ESC | ~["\b\n\f\r\t\\])*'"' 
        {
            self.text = self.text[1:-1]
        }
        ;
fragment ESC : '\\'[bfrnt"\\];


ID: [a-zA-Z_][a-zA-Z0-9_]*;

BLOCK_COMMENT: '/*' .*? '*/' -> skip;   //?
LINE_COMMENT: '//' ~[\r\n\f]* -> skip;  //?

BREAK: 'break';
CONTINUE: 'continue';
ELSE: 'else';
FOR: 'for';
IF: 'if';
RETURN: 'return';
DO: 'do';
WHILE: 'while';
TRUE : 'true';
FALSE: 'false';

BOOLEANTYPE: 'boolean';
VOIDTYPE: 'void';
INTTYPE: 'int';
FLOATTYPE: 'float';
STRINGTYPE: 'string';

ASSIGN: '=';
OROP: '||';
ANDOP: '&&';
EQUALOP: '==' | '!=';
COMPOP: '<'| '>'| '<='| '>=';
ADDOP: '+';
SUBOP: '-';
MULOP: '*';
DIVOP: '/';
MODOP: '%';
NEGOP: '!';
LB: '(' ;
RB: ')' ;
LP: '{';
RP: '}';
LS: '[';
RS: ']';
SEMI: ';';
COLON: ':';
COMMA: ',';

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines


ERROR_CHAR: .;

UNCLOSE_STRING
    : '"'(ESC | ~[\b\n\f\r\t\\"])*
    {
        self.text = self.text[1:]
    }
    ;
ILLEGAL_ESCAPE
    : '"'(ESC | ~[\b\n\f\r\t"])*'\\'.
    {
        self.text = self.text[1:]
    }
    ;