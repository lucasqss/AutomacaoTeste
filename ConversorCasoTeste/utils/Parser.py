import ply.yacc as yacc
from Cods.ConversorCasoTeste.utils import Lexer

'''
Grammar:
------------------------------------------------------------------------------------------
Non-terminals:

S -> expr

expr -> expr OL expr 
     |  term
     ;
     
term -> ID OB ID
     |  ID IN LIST
     |  not term
     ;
     
OL -> AND
   |  OR
   ;
   
OB -> EQUALS
   |  LTE
   |  LT
   |  GTE
   |  GT
   |  IN
   ;
   
not -> NOT ;

'''

class Parser:

    def __init__(self):
        self.parsedList = []
        self.tokens = Lexer.Lexer().tokens

    def p_expression_paren_expression(self, p):
        'expression :  expression logical expression '
        p[0] = 'FunctionList.logical_operation(\'' + p[2] + '\',' + p[1] + ',' + p[3] + ')'

    def p_expression_term(self, p):
        'expression : term '
        p[0] = p[1]

    def p_term_not(self, p):
        'term : not term'
        p[0] = 'FunctionList.unary_operation(\'' + p[1] + '\', ' + p[2] + ')'

    def p_term_number(self, p):
        'term : ID binary NUMBER'
        p[0] = 'FunctionList.binary_operation(\'' + p[2] + '\',*' + p[1] + '/,' + p[3] + ')'

    def p_term_list(self, p):
        'term : ID IN LIST'
        p[0] = 'FunctionList.binary_operation(\'' + p[2] + '\',*' + p[1] + '/,' + p[3] + ')'

    def p_term_binary(self, p):
        'term : ID binary ID'
        p[0] = 'FunctionList.binary_operation(\'' + p[2] + '\',*' + p[1] + '/,+' + p[3] + '/)'

    def p_logical_and(self, p):
        'logical : AND'
        p[0] = p[1]

    def p_logical_or(self, p):
        'logical : OR'
        p[0] = p[1]

    def p_binary_equals(self, p):
        'binary : EQUALS'
        p[0] = p[1]

    def p_binary_in(self, p):
        'binary : IN'
        p[0] = p[1]

    def p_binary_gt(self, p):
        'binary : GT'
        p[0] = p[1]

    def p_binary_gte(self, p):
        'binary : GTE'
        p[0] = p[1]

    def p_binary_lt(self, p):
        'binary : LT'
        p[0] = p[1]

    def p_binary_lte(self, p):
        'binary : LTE'
        p[0] = p[1]

    def p_not(self, p):
        'not : NOT'
        p[0] = p[1]

    # Error rule for syntax errors
    def p_error(self, p):
        print("Syntax error in input! p = ", p)

    # Build the parser
    def build(self):
        self.parser = yacc.yacc(module=self)


    def getParsedList(self, args):
        self.build()

        parsed_list = self.parser.parse(args)
        parsed_string = ""
        for i in parsed_list:
            if i == "*":
                parsed_string += 'a['
            elif i == "/":
                parsed_string += ']'
            elif i == "+":
                parsed_string += 'b['
            else:
                parsed_string += i

        return parsed_string

