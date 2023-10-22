import pandas as pd
import easygui

from Cods.ConversorCasoTeste.problema.GerenciadorTestes import GerenciadorTestes

print("Selecione planilha com os testes:")
planilha_teste = easygui.fileopenbox()
dados_teste = pd.read_excel(planilha_teste)

print("Selecione planilha com a massa de dados:")
planilha_massa = easygui.fileopenbox()
dados_massa = pd.read_excel(planilha_massa)

testmanager = GerenciadorTestes(dados_teste, dados_massa)

solutions = testmanager.obterSolucoesExcel()
print(solutions)

testmanager.gerarSaidaExcel(solutions)



