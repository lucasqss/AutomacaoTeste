from .models import Contas
from flask import flash


def is_mesma_titularidade(dicionario_cedente, dicionario_cessionario):
    if dicionario_cedente['identificacao_fiscal'] == dicionario_cessionario['identificacao_fiscal']:
        return True
    else:
        try:
            flash("titularidades incompativeis")
        except:
            print("teste")
        return False


def is_titularidades_diferentes(dicionario_cedente, dicionario_cessionario):

    if dicionario_cedente['identificacao_fiscal'] != dicionario_cessionario['identificacao_fiscal']:
        return True
    else:
        try:
            flash("titularidades incompativeis")
        except:
            print("teste")
        return False


def is_mesmo_custodiante(dicionario_cedente, dicionario_cessionario):
    if dicionario_cedente['banco'] == dicionario_cessionario['banco']:
        return True
    else:
        try:
            flash("instituições financeiras incompativeis")
        except:
            print("teste")
        return False


def is_custodiantes_diferentes(dicionario_cedente, dicionario_cessionario):
    if dicionario_cedente['banco'] != dicionario_cessionario['banco']:
        return True
    else:
        try:
            flash("instituições financeiras incompativeis")
        except:
            print("teste")
        return False


def is_mesmo_tipo_conta(dicionario_cedente, dicionario_cessionario):
    if dicionario_cedente['tipo_conta'] == dicionario_cessionario['tipo_conta']:
        return True
    else:
        try:
            flash("tipo de conta incompativel")
        except:
            print("teste")
        return False


def is_tipos_conta_diferentes(dicionario_cedente, dicionario_cessionario):
    if dicionario_cedente['tipo_conta'] != dicionario_cessionario['tipo_conta']:
        return True
    else:
        try:
            flash("tipo de conta incompativel")
        except:
            print("teste")
        return False


def possui_saldo(dicionario_cedente, valor):

    try:
        valor_lido = int(dicionario_cedente['saldo'])
    except:
        print("Valor do dicionario nao eh inteiro")

    if valor_lido >= int(valor):
        return True
    else:
        try:
            flash("saldo insuficiente")
        except:
            print("teste")
        return False


def trocar_custodia(session, numero_cedente, numero_cessionario, valor):
    session.query(Contas).filter(Contas.numero_conta == numero_cedente).update({Contas.saldo: Contas.saldo - valor})
    session.query(Contas).filter(Contas.numero_conta == numero_cessionario).update({Contas.saldo: Contas.saldo + valor})
    session.commit()


def validar_operacao1(dicionario_cedente, dicionario_cessionario, valor):
    return possui_saldo(dicionario_cedente, int(valor))


def validar_operacao2(dicionario_cedente, dicionario_cessionario, valor):
    return possui_saldo(dicionario_cedente, int(valor)) \
           and is_titularidades_diferentes(dicionario_cedente, dicionario_cessionario)


def validar_operacao3(dicionario_cedente, dicionario_cessionario, valor):
    return possui_saldo(dicionario_cedente, int(valor)) \
           and is_mesmo_custodiante(dicionario_cedente, dicionario_cessionario) \
           and is_titularidades_diferentes(dicionario_cedente, dicionario_cessionario)


def validar_operacao4(dicionario_cedente, dicionario_cessionario, valor, taxa):
    return possui_saldo(dicionario_cedente, int(valor) + int(taxa)) \
           and is_custodiantes_diferentes(dicionario_cedente, dicionario_cessionario) \
           and is_mesma_titularidade(dicionario_cedente, dicionario_cessionario)
