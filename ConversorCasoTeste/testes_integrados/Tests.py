import pandas as pd
import unittest
import sys
import os
from Cods.ConversorCasoTeste.problema import Conversor


class TestStringMethods(unittest.TestCase):

    def test_is_equal_greater_than(self):

        dados_massa = pd.read_excel("DadosContas.xlsx")
        problem = Conversor.Conversor(dados_massa)
        problem.adicionarVariaveis()

        problem.inserirRestricaoUmaVariavel("Saldo>800", "x")
        problem.inserirRestricaoDuasVariaveis("Saldo==Saldo", ["x", "y"])

        solucoes = problem.obterTodasSolucoes()

        for solucao in solucoes:
            print(solucao)

        valores_possiveis = [
            [1, 'BB', 'A', 1, 900, 9999, 'S'],
            [2, 'BRAD', 'A', 9, 900, 1111, 'N'],
            [11, 'BRAD', 'B', 11, 900, 5588, 'N']
            ]

        solucoesEsperadas = self.gerarJsons(valores_possiveis)

        self.printar_conjuntos_obtidos_e_esperados(solucoesEsperadas, solucoes)

        self.assertEqual(len(solucoes), len(valores_possiveis) * len(valores_possiveis))
        for elemento in solucoes:
            print("Elemento obtido: " + str(elemento))
            print("Está contido no conjunto esperado? " + str(solucoesEsperadas.__contains__(elemento)))
            self.assertTrue(solucoesEsperadas.__contains__(elemento))


    def test_greater_equal_operation_and(self):
        dados_massa = pd.read_excel("DadosContas.xlsx")
        problem = Conversor.Conversor(dados_massa)
        problem.adicionarVariaveis()

        problem.inserirRestricaoUmaVariavel("Saldo>=800", "x")
        problem.inserirRestricaoDuasVariaveis("Saldo==Saldo & Bloqueio==Bloqueio", ["x", "y"])

        valores_possiveis = [[1, 'BB', 'A', 1, 900, 9999, 'S'],
                             [2, 'BRAD', 'A', 9, 900, 1111, 'N'],
                             [3, 'BB', 'B', 5, 800, 5555, 'S'],
                             [11, 'BRAD', 'B', 11, 900, 5588, 'N']
                             ]

        esperado = [{'x': valores_possiveis[0], 'y': valores_possiveis[0]},
                    {'x': valores_possiveis[1], 'y': valores_possiveis[1]},
                    {'x': valores_possiveis[1], 'y': valores_possiveis[3]},
                    {'x': valores_possiveis[2], 'y': valores_possiveis[2]},
                    {'x': valores_possiveis[3], 'y': valores_possiveis[3]},
                    {'x': valores_possiveis[3], 'y': valores_possiveis[1]}
                    ]

        solucoes = problem.obterTodasSolucoes()
        self.printar_conjuntos_obtidos_e_esperados(esperado, solucoes)

        self.assertEqual(len(solucoes), len(esperado))
        for elemento in solucoes:
            print("\n" + "Elemento obtido: " + str(elemento))
            print("Está contido no conjunto esperado? " + str(esperado.__contains__(elemento)))
            self.assertTrue(esperado.__contains__(elemento))


    def test_lesser_equal_operation_or(self):
        dados_massa = pd.read_excel("DadosContas.xlsx")
        problem = Conversor.Conversor(dados_massa)
        problem.adicionarVariaveis()

        problem.inserirRestricaoUmaVariavel("Saldo<100", "x")
        problem.inserirRestricaoUmaVariavel("Saldo<100", "y")
        problem.inserirRestricaoDuasVariaveis("Saldo<=Saldo", ["x", "y"])

        solucoes = problem.obterTodasSolucoes()

        valores_possiveis = [
            [5, 'ITAU', 'A', 7, 70, 3333, 'N'],
            [6, 'BB', 'A', 4, 50, 6666, 'N'],
            [7, 'ITAU', 'C', 8, 80, 2222, 'S'],
            [10, 'XP', 'A', 2, 10, 8888, 'N']
            ]

        esperado = [{'x': valores_possiveis[0], 'y': valores_possiveis[0]},
                    {'x': valores_possiveis[0], 'y': valores_possiveis[2]},

                    {'x': valores_possiveis[1], 'y': valores_possiveis[0]},
                    {'x': valores_possiveis[1], 'y': valores_possiveis[1]},
                    {'x': valores_possiveis[1], 'y': valores_possiveis[2]},

                    {'x': valores_possiveis[2], 'y': valores_possiveis[2]},

                    {'x': valores_possiveis[3], 'y': valores_possiveis[0]},
                    {'x': valores_possiveis[3], 'y': valores_possiveis[1]},
                    {'x': valores_possiveis[3], 'y': valores_possiveis[2]},
                    {'x': valores_possiveis[3], 'y': valores_possiveis[3]}
                    ]

        self.printar_conjuntos_obtidos_e_esperados(esperado, solucoes)

        self.assertEqual(len(solucoes), 10)
        for elemento in solucoes:
            self.assertTrue(esperado.__contains__(elemento))


    def test_inside_not(self):
        dados_massa = pd.read_excel("DadosContas.xlsx")
        problem = Conversor.Conversor(dados_massa)
        problem.adicionarVariaveis()

        problem.inserirRestricaoUmaVariavel("!Saldo-in[100, 100]", "x")
        problem.inserirRestricaoUmaVariavel("Saldo-in[100]", "y")
        problem.inserirRestricaoDuasVariaveis("Saldo<=Saldo", ["x", "y"])

        solucoes = problem.obterTodasSolucoes()
        print(solucoes)

        valores_possiveis_x = [
            [5, 'ITAU', 'A', 7, 70, 3333, 'N'],
            [6, 'BB', 'A', 4, 50, 6666, 'N'],
            [7, 'ITAU', 'C', 8, 80, 2222, 'S'],
            [10, 'XP', 'A', 2, 10, 8888, 'N']
            ]

        valores_possiveis_y = [[8, 'XP', 'A', 3, 100, 7777, 'S'],
                             [9, 'BRAD', 'B', 10, 100, 1234, 'N']
                             ]

        esperado = [{'x': valores_possiveis_x[0], 'y': valores_possiveis_y[0]},
                    {'x': valores_possiveis_x[0], 'y': valores_possiveis_y[1]},

                    {'x': valores_possiveis_x[1], 'y': valores_possiveis_y[0]},
                    {'x': valores_possiveis_x[1], 'y': valores_possiveis_y[1]},

                    {'x': valores_possiveis_x[2], 'y': valores_possiveis_y[0]},
                    {'x': valores_possiveis_x[2], 'y': valores_possiveis_y[1]},

                    {'x': valores_possiveis_x[3], 'y': valores_possiveis_y[0]},
                    {'x': valores_possiveis_x[3], 'y': valores_possiveis_y[1]}
                    ]

        self.printar_conjuntos_obtidos_e_esperados(esperado, solucoes)
        self.assertEqual(len(solucoes), len(esperado))
        for elemento in solucoes:
            self.assertTrue(esperado.__contains__(elemento))

    if __name__ == '__main__':
        unittest.main()

    def gerarJsons(self, valores_possiveis):
        ret = []
        for elemento in valores_possiveis:
            for outro_elemento in valores_possiveis:
                ret.append({'x': elemento, 'y': outro_elemento})

        return ret

    def printar_conjuntos_obtidos_e_esperados(self, esperado, solucoes):
        print("Elementos do conjunto de solucoes obtidas:")
        for elemento in solucoes:
            print(elemento)
        print("\n")
        print("Elementos do conjunto de valores esperados:")
        for elemento in esperado:
            print(elemento)

