from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import Contas
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from sqlalchemy import update
from flask_login import login_user, login_required, logout_user, current_user
from .comportamentos import *

transactions = Blueprint('transactions', __name__)

@transactions.route('/operacao1', methods=['GET', 'POST'])
def operacao1():
    if request.method == 'POST':
        conta_cedente = request.form.get('conta_cedente')
        conta_cessionaria = request.form.get('conta_cessionaria')
        valor_transacao = request.form.get('valor_transacao')

        cedente = Contas.query.filter_by(numero_conta=conta_cedente).first().__dict__
        cessionario = Contas.query.filter_by(numero_conta=conta_cessionaria).first().__dict__

        if cedente['numero_conta'] == cessionario['numero_conta']:
            flash("Contas devem ser distintas")

        else:
            if validar_operacao1(cedente, cessionario, valor_transacao):
                trocar_custodia(db.session, cedente['numero_conta'], cessionario['numero_conta'], valor_transacao)
                flash(Contas.query.filter_by(numero_conta=conta_cedente).first().__dict__)
                flash(Contas.query.filter_by(numero_conta=conta_cessionaria).first().__dict__)
            else:
                pass

    return render_template("operacao1.html", user=current_user)





@transactions.route('/operacao2', methods=['GET', 'POST'])
def operacao2():
    if request.method == 'POST':
        conta_cedente = request.form.get('conta_cedente')
        conta_cessionaria = request.form.get('conta_cessionaria')
        valor_transacao = request.form.get('valor_transacao')

        cedente = Contas.query.filter_by(numero_conta=conta_cedente).first().__dict__
        cessionario = Contas.query.filter_by(numero_conta=conta_cessionaria).first().__dict__

        if cedente['numero_conta'] == cessionario['numero_conta']:
            flash("Contas devem ser distintas")

        else:
            if validar_operacao2(cedente, cessionario, valor_transacao):
                trocar_custodia(db.session, cedente['numero_conta'], cessionario['numero_conta'], valor_transacao)
                flash(Contas.query.filter_by(numero_conta=conta_cedente).first().__dict__)
                flash(Contas.query.filter_by(numero_conta=conta_cessionaria).first().__dict__)
            else:
                pass

    return render_template("operacao2.html", user=current_user)




@transactions.route('/operacao3', methods=['GET', 'POST'])
def operacao3():
    if request.method == 'POST':
        conta_cedente = request.form.get('conta_cedente')
        conta_cessionaria = request.form.get('conta_cessionaria')
        valor_transacao = request.form.get('valor_transacao')

        cedente = Contas.query.filter_by(numero_conta=conta_cedente).first().__dict__
        cessionario = Contas.query.filter_by(numero_conta=conta_cessionaria).first().__dict__

        if cedente['numero_conta'] == cessionario['numero_conta']:
            flash("Contas devem ser distintas")

        else:
            if validar_operacao3(cedente, cessionario, valor_transacao):
                trocar_custodia(db.session, cedente['numero_conta'], cessionario['numero_conta'], valor_transacao)
                flash(Contas.query.filter_by(numero_conta=conta_cedente).first().__dict__)
                flash(Contas.query.filter_by(numero_conta=conta_cessionaria).first().__dict__)
            else:
                pass

    return render_template("operacao3.html", user=current_user)




@transactions.route('/operacao4', methods=['GET', 'POST'])
def operacao4():
    if request.method == 'POST':
        conta_cedente = request.form.get('conta_cedente')
        conta_cessionaria = request.form.get('conta_cessionaria')
        valor_transacao = request.form.get('valor_transacao')

        taxa = 100

        cedente = Contas.query.filter_by(numero_conta=conta_cedente).first().__dict__
        cessionario = Contas.query.filter_by(numero_conta=conta_cessionaria).first().__dict__

        if cedente['numero_conta'] == cessionario['numero_conta']:
            flash("Contas devem ser distintas")

        else:
            if validar_operacao4(cedente, cessionario, valor_transacao, taxa):
                trocar_custodia(db.session, cedente['numero_conta'], cessionario['numero_conta'], valor_transacao)
                flash(Contas.query.filter_by(numero_conta=conta_cedente).first().__dict__)
                flash(Contas.query.filter_by(numero_conta=conta_cessionaria).first().__dict__)
            else:
                pass

    return render_template("operacao4.html", user=current_user)




