import random
import constraint
from Cods.ConversorCasoTeste.utils import Parser
from Cods.ConversorCasoTeste.utils import Lexer
from Cods.ConversorCasoTeste.utils import FunctionList

class Conversor:

    def __init__(self, data_frame_massa_dados):
        self.data_frame_massa_dados = data_frame_massa_dados
        self.problem = constraint.Problem()
        self.nomes_colunas_dados = []

        for col in data_frame_massa_dados.columns:
            self.nomes_colunas_dados.append(col)

        self.lista_de_dados = data_frame_massa_dados.values.tolist()

        self.solutions = {}

    def adicionarVariaveis(self):
        self.problem.addVariable("x", self.lista_de_dados)
        self.problem.addVariable("y", self.lista_de_dados)

    def adicionarVariaveisDaLista(self, lista_de_variaveis):
        self.problem.addVariables(lista_de_variaveis, self.lista_de_dados)

    def inserirRestricaoUmaVariavel(self, string_da_restricao, variavel):
        lexer = Lexer.Lexer()
        lexer.input(string_da_restricao.replace(" ", ""))
        parser = Parser.Parser()
        parsed_string_first = parser.getParsedList(string_da_restricao)

        #print("String = " + parsed_string_first + "\npara a variavel : " + variavel)
        for variable_index_first in self.nomes_colunas_dados:
            if variable_index_first in lexer.getTokens():
                ind_first = self.nomes_colunas_dados.index(variable_index_first)
                parsed_string_first = parsed_string_first.replace(variable_index_first, str(ind_first))

        self.problem.addConstraint(lambda a: eval(parsed_string_first), [variavel])

    def inserirRestricaoDuasVariaveis(self, string_da_restricao, lista_de_variaveis):
        lexer = Lexer.Lexer()
        lexer.input(string_da_restricao.replace(" ", ""))

        parser = Parser.Parser()
        parsed_string_first = parser.getParsedList(string_da_restricao)


        #print("String = " + parsed_string_first + "\npara as variaveis : " + str(lista_de_variaveis))
        for variable_index_first in self.nomes_colunas_dados:
            if variable_index_first in lexer.getTokens():
                ind_first = self.nomes_colunas_dados.index(variable_index_first)
                parsed_string_first = parsed_string_first.replace(variable_index_first, str(ind_first))

        self.problem.addConstraint(lambda a, b: eval(parsed_string_first), lista_de_variaveis)

    def obterTodasSolucoes(self):
        self.solutions = self.problem.getSolutions()
        return self.solutions

    def obterSolucaoRandomica(self):
        solutions = self.problem.getSolutions()
        solution_index = random.randint(0, len(solutions) - 1)
        self.solutions = solutions[solution_index]
        return self.solutions
