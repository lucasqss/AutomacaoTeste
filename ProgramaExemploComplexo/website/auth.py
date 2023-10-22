from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User, Contas
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user


auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')

    return render_template("login.html", user=current_user)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/reseta_banco', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        clear_data(session=db.session)
        db.session.add(Contas(identificacao_fiscal="123456", saldo=200, banco="bradesco", numero_conta=10, tipo_conta=1))
        db.session.add(Contas(identificacao_fiscal="123456", saldo=0, banco="itau", numero_conta=11, tipo_conta=2))
        db.session.add(Contas(identificacao_fiscal="123456", saldo=900, banco="bradesco", numero_conta=12, tipo_conta=1))

        db.session.add(Contas(identificacao_fiscal="654321", saldo=900, banco="itau", numero_conta=20, tipo_conta=2))
        db.session.add(Contas(identificacao_fiscal="654321", saldo=0, banco="bradesco", numero_conta=21, tipo_conta=3))
        db.session.add(Contas(identificacao_fiscal="654321", saldo=100, banco="caixa", numero_conta=22, tipo_conta=1))

        db.session.add(Contas(identificacao_fiscal="999999", saldo=900, banco="itau", numero_conta=30, tipo_conta=3))
        db.session.add(Contas(identificacao_fiscal="999999", saldo=0, banco="bradesco", numero_conta=31, tipo_conta=1))
        db.session.add(Contas(identificacao_fiscal="999999", saldo=100, banco="caixa", numero_conta=32, tipo_conta=1))

        db.session.commit()

        flash(db.session.query(Contas).filter_by(numero_conta=10).first().__dict__['numero_conta'])
        flash(db.session.query(Contas).filter_by(numero_conta=11).first().__dict__)
        flash(db.session.query(Contas).filter_by(numero_conta=12).first().__dict__)

        flash(db.session.query(Contas).filter_by(numero_conta=20).first().__dict__)
        flash(db.session.query(Contas).filter_by(numero_conta=21).first().__dict__)
        flash(db.session.query(Contas).filter_by(numero_conta=22).first().__dict__)

        flash(db.session.query(Contas).filter_by(numero_conta=30).first().__dict__)
        flash(db.session.query(Contas).filter_by(numero_conta=31).first().__dict__)
        flash(db.session.query(Contas).filter_by(numero_conta=32).first().__dict__)


    return render_template("reseta_banco.html", user=current_user)


def clear_data(session):
    meta = db.metadata
    for table in reversed(meta.sorted_tables):
        print('Clear table %s' % table)
        session.execute(table.delete())
    session.commit()


