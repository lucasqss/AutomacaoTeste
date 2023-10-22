from Cods.ConversorCasoTeste.problema import Conversor


class GerenciadorTestes:

    def __init__(self, tests_data_frame, input_data_variables):
        self.tests_data_frame = tests_data_frame.fillna("").astype(str)
        self.input_data_variables = input_data_variables.astype(str)
        self.test_columns = []
        for column in tests_data_frame.columns:
            self.test_columns.append(column)

        self.problem = None
        self.test_dictionary = {}
        self.restrictions = []
        self.restrictions_first = []
        self.restrictions_first = []
        self.restrictions_second = []
        self.restrictions_both = []
        self.solutions = []

    def setRestrictions(self, restrictions_column_name):
        try:
            self.restriction_list = self.tests_data_frame[restrictions_column_name]
        except:
            print("Coluna de nome " + restrictions_column_name + " não encontrada")

    def setRestrictionsFirst(self, restrictions_first_column_name):
        try:
            self.restrictions_first = self.tests_data_frame[restrictions_first_column_name]
        except:
            print("Coluna de nome " + restrictions_first_column_name + " não encontrada")

    def setRestrictionsSecond(self, restrictions_second_column_name):
        try:
            self.restrictions_second = self.tests_data_frame[restrictions_second_column_name]
        except:
            print("Coluna de nome " + restrictions_second_column_name + " não encontrada")

    def setRestrictionsBoth(self, restrictions_both_column_name):
        try:
            self.restrictions_both = self.tests_data_frame[restrictions_both_column_name]
        except:
            print("Coluna de nome " + restrictions_both_column_name + " não encontrada")

    def obterSolucoes(self):

        for restriction_index in range(len(self.restrictions_first)):
            self.problem = Conversor.Conversor(self.input_data_variables)
            self.problem.adicionarVariaveis()

            if len(self.restrictions_first) > 0:
                if str(self.restrictions_first[restriction_index]) not in ["nan", ""]:
                    self.problem.inserirRestricaoUmaVariavel(self.restrictions_first[restriction_index], "x")

            if len(self.restrictions_second) > 0:
                if str(self.restrictions_second[restriction_index]) not in ["nan", ""]:
                    self.problem.inserirRestricaoUmaVariavel(self.restrictions_second[restriction_index], "y")

            if len(self.restrictions_both) > 0:
                if str(self.restrictions_both[restriction_index]) not in ["nan", ""]:
                    self.problem.inserirRestricaoDuasVariaveis(self.restrictions_both[restriction_index], ["x", "y"])

            self.solutions.append(self.problem.obterSolucaoRandomica())

        self.test_dictionary["solutions"] = self.solutions
        return self.solutions


    def gerarSaidaExcel(self, json_solucoes):
        planilha_saida = self.tests_data_frame

        if 'Restricoes Primeiro' in planilha_saida.columns:
            planilha_saida.drop(['Restricoes Primeiro'], axis=1, inplace=True)
        if 'Restricoes Segundo' in planilha_saida.columns:
            planilha_saida.drop(['Restricoes Segundo'], axis=1, inplace=True)

        for i in range(len(json_solucoes)):
            print(planilha_saida.loc[i, 'Restricoes Ambos'])
            print(json_solucoes[i])
            planilha_saida.loc[i, 'Restricoes Ambos'] = str(json_solucoes[i])

        planilha_saida.rename(columns={'Restricoes Ambos': 'Valores Concretos'}, inplace=True)
        print(planilha_saida)
        planilha_saida.to_excel('SaidaGerada.xlsx', index=False)

    def gerarSaidaExcelComNome(self, json_solucoes, nome_saida):
        planilha_saida = self.tests_data_frame

        if 'Restricoes Primeiro' in planilha_saida.columns:
            planilha_saida.drop(['Restricoes Primeiro'], axis=1, inplace=True)
        if 'Restricoes Segundo' in planilha_saida.columns:
            planilha_saida.drop(['Restricoes Segundo'], axis=1, inplace=True)

        for i in range(len(json_solucoes)):
            print(planilha_saida.loc[i, 'Restricoes Ambos'])
            print(json_solucoes[i])
            planilha_saida.loc[i, 'Restricoes Ambos'] = str(json_solucoes[i])

        planilha_saida.rename(columns={'Restricoes Ambos': 'Valores Concretos'}, inplace=True)
        print(planilha_saida)
        planilha_saida.to_excel(nome_saida + ".xlsx", index=False)

    def obterSolucoesExcel(self):

        self.setRestrictionsFirst('Restricoes Primeiro')
        self.setRestrictionsSecond("Restricoes Segundo")
        self.setRestrictionsBoth("Restricoes Ambos")

        return self.obterSolucoes()

    def getStructuredTest(self):
        return self.test_dictionary

    def setStrExpected(self, expected_column_name):
        self.test_dictionary[expected_column_name] = self.tests_data_frame[expected_column_name].tolist()

    def setIntExpected(self, expected_column_name):
        self.test_dictionary[expected_column_name] = self.tests_data_frame[expected_column_name].astype(int).tolist()

    def setListExpected(self, expected_column_name):
        out = []
        for element in self.tests_data_frame[expected_column_name]:
            temp = []
            if str(element) != "":
                temp.append(element)
            out.append(temp)
        self.test_dictionary[expected_column_name] = out
