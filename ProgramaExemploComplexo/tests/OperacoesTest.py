import pandas as pd
import sqlalchemy as db

from Cods.ConversorCasoTeste.problema import GerenciadorAsserts
from Cods.ConversorCasoTeste.problema.GerenciadorTestes import GerenciadorTestes
from Cods.ProgramaExemploComplexo.website.comportamentos import validar_operacao2, validar_operacao3, validar_operacao4


engine = db.create_engine('sqlite:///database.db')
connection = engine.connect()
metadata = db.MetaData()
contas = db.Table('Contas', metadata, autoload=True, autoload_with=engine)

# Equivalent to 'SELECT * FROM census'
query = db.select([contas])
dados_banco = pd.read_sql(query, connection)
connection.close()
# print(dados_banco)


print("\n Inicio dos testes da operação 2\n")

dados_testes = pd.read_excel("Testes_Complexo_Oper2.xlsx", dtype=str)
# print(dados_testes.to_string())


testmanager = GerenciadorTestes(dados_testes, dados_banco)
testmanager.setRestrictionsFirst("Restricoes Primeiro")
testmanager.setRestrictionsBoth("Restricoes Ambos")
solucoes = testmanager.obterSolucoes()
testmanager.gerarSaidaExcelComNome(solucoes, "Operacao 2")
testmanager.setStrExpected("Resultado esperado")

dicionario_testes = testmanager.getStructuredTest()
# print("\n", dicionario_testes)
# print(dicionario_testes.get('solutions')[0])


for indice in range(len(dicionario_testes.get("solutions"))):
    dicionario_cedente = {'identificacao_fiscal': dicionario_testes.get('solutions')[indice].get('x')[1],
                          'banco': dicionario_testes.get('solutions')[indice].get('x')[3],
                          'tipo_conta': dicionario_testes.get('solutions')[indice].get('x')[5],
                          'saldo': dicionario_testes.get('solutions')[indice].get('x')[2]}

    dicionario_cessionario = {'identificacao_fiscal': dicionario_testes.get('solutions')[indice].get('y')[1],
                              'banco': dicionario_testes.get('solutions')[indice].get('y')[3],
                              'tipo_conta': dicionario_testes.get('solutions')[indice].get('y')[5],
                              'saldo': dicionario_testes.get('solutions')[indice].get('y')[2]}

    valor = 100

    print("\n\n Executando teste ", indice + 1, " da operação 2")
    print(dicionario_cedente)
    print(dicionario_cessionario)
    assertion_manager = GerenciadorAsserts.GerenciadorAsserts()
    assertion_manager.insertAssertion('Resultado esperado',
                                      validar_operacao2(dicionario_cedente, dicionario_cessionario, valor),
                                      eval(dicionario_testes.get('Resultado esperado')[indice]))
    assertion_manager.performAssertion()


print("\n\n\n Fim dos testes da operacao 2 ---------------------------------------------------------------\n\n\n")


print("\n Inicio dos testes da operação 3\n")

dados_testes = pd.read_excel("Testes_Complexo_Oper3.xlsx", dtype=str)
# print(dados_testes.to_string())


testmanager = GerenciadorTestes(dados_testes, dados_banco)
testmanager.setRestrictionsFirst("Restricoes Primeiro")
testmanager.setRestrictionsBoth("Restricoes Ambos")

solucoes = testmanager.obterSolucoes()
testmanager.gerarSaidaExcelComNome(solucoes, "Operacao 3")

testmanager.setStrExpected("Resultado esperado")

dicionario_testes = testmanager.getStructuredTest()
# print("\n", dicionario_testes)
# print(dicionario_testes.get('solutions')[0])


for indice in range(len(dicionario_testes.get("solutions"))):
    dicionario_cedente = {'identificacao_fiscal': dicionario_testes.get('solutions')[indice].get('x')[1],
                          'banco': dicionario_testes.get('solutions')[indice].get('x')[3],
                          'tipo_conta': dicionario_testes.get('solutions')[indice].get('x')[5],
                          'saldo': dicionario_testes.get('solutions')[indice].get('x')[2]}

    dicionario_cessionario = {'identificacao_fiscal': dicionario_testes.get('solutions')[indice].get('y')[1],
                              'banco': dicionario_testes.get('solutions')[indice].get('y')[3],
                              'tipo_conta': dicionario_testes.get('solutions')[indice].get('y')[5],
                              'saldo': dicionario_testes.get('solutions')[indice].get('y')[2]}

    valor = 100

    print("\n\n Executando teste ", indice + 1, " da operação 3")
    print(dicionario_cedente)
    print(dicionario_cessionario)
    assertion_manager = GerenciadorAsserts.GerenciadorAsserts()
    assertion_manager.insertAssertion('Resultado esperado',
                                      validar_operacao3(dicionario_cedente, dicionario_cessionario, valor),
                                      eval(dicionario_testes.get('Resultado esperado')[indice]))
    assertion_manager.performAssertion()

print("\n\n\n Fim dos testes da operacao 3 ---------------------------------------------------------------\n\n\n")
print("\n Inicio dos testes da operação 4\n")

dados_testes = pd.read_excel("Testes_Complexo_Oper4.xlsx", dtype=str)
# print(dados_testes.to_string())


testmanager = GerenciadorTestes(dados_testes, dados_banco)
testmanager.setRestrictionsFirst("Restricoes Primeiro")
testmanager.setRestrictionsBoth("Restricoes Ambos")

solucoes = testmanager.obterSolucoes()
testmanager.gerarSaidaExcelComNome(solucoes, "Operacao 4")

testmanager.setStrExpected("Resultado esperado")

dicionario_testes = testmanager.getStructuredTest()
# print("\n", dicionario_testes)
# print(dicionario_testes.get('solutions')[0])


for indice in range(len(dicionario_testes.get("solutions"))):
    dicionario_cedente = {'identificacao_fiscal': dicionario_testes.get('solutions')[indice].get('x')[1],
                          'banco': dicionario_testes.get('solutions')[indice].get('x')[3],
                          'tipo_conta': dicionario_testes.get('solutions')[indice].get('x')[5],
                          'saldo': dicionario_testes.get('solutions')[indice].get('x')[2]}

    dicionario_cessionario = {'identificacao_fiscal': dicionario_testes.get('solutions')[indice].get('y')[1],
                              'banco': dicionario_testes.get('solutions')[indice].get('y')[3],
                              'tipo_conta': dicionario_testes.get('solutions')[indice].get('y')[5],
                              'saldo': dicionario_testes.get('solutions')[indice].get('y')[2]}

    valor = 100
    taxa = 100

    print("\n\n Executando teste ", indice + 1, " da operação 4")
    print(dicionario_cedente)
    print(dicionario_cessionario)
    assertion_manager = GerenciadorAsserts.GerenciadorAsserts()
    assertion_manager.insertAssertion('Resultado esperado',
                                      validar_operacao4(dicionario_cedente, dicionario_cessionario, valor, taxa),
                                      eval(dicionario_testes.get('Resultado esperado')[indice]))
    assertion_manager.performAssertion()

print("\n\n\n Fim dos testes da operacao 4 ---------------------------------------------------------------\n\n\n")

exit()
