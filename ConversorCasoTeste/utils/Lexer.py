import ply.lex as lex

'''
Grammar:    
------------------------------------------------------------------------------------------
Terminals:

    Precedence operators:
        RPAREN = right parentheses
        LPAREN = left parentheses

    Unary operators:
        NOT = negation operator

    Binary Operators:
        LTE = 'first' lesser than or equal 'second'
        LT = 'first' lesser than 'second'
        GTE = 'first' greater than or equal 'second'
        GT = 'first' greater than 'second'
        IN = 'first' is inside 'second'
        EQUALS = 'first' equals  'second'

    Logical operators:
        OR = or
        AND = and

    Variable identifiers:
        LIST = generic list of elements that must be created brackets
        ID = string that matches an attribute (column) of database

'''


class Lexer:

    tokens = (
        'NUMBER',
        'LIST',
        'AND',
        'OR',
        'NOT',
        'EQUALS',
        'IN',
        'GT',
        'GTE',
        'LT',
        'LTE',
        'ID',
    )

    t_LTE = r'\<='
    t_LT = r'\<'
    t_GTE = r'\>='
    t_GT = r'\>'
    t_IN = r'-in'
    t_EQUALS = r'\=='
    t_NOT = r'\!'
    t_OR = r'\|'
    t_AND = r'\&'

    t_NUMBER = r'[0-9]+'
    t_LIST = r'\[' + r'[\w\s,"]+' + r'\]'
    t_ID = r'[a-zA-Z_][0-9a-zA-Z_]*'

    identified_tokens = []

    def t_newline(self,t):
        r'\n+'
        t.lexer.lineno += len(t.value)

    t_ignore = ' \t'

    def t_error(self,t):
        print("Illegal character '%s'" % t.value[0])
        t.lexer.skip(1)

    # Build the lexer
    def build(self,**kwargs):
        self.errors = []
        self.lexer = lex.lex(module=self, **kwargs)

    def input(self, args):
        self.build()
        self.lexer.input(args)
        while True:
            tok = self.lexer.token()
            if not tok:
                break  # No more input
            if tok.type == 'ID':
                self.identified_tokens.append(tok.value)

    def getTokens(self):
        return self.identified_tokens
