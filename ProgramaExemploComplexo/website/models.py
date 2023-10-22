from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    identificacao_fiscal = db.Column(db.String(14))
    saldo = db.Column(db.Integer)
    banco = db.Column(db.String(100))
    numero_conta = db.Column(db.Integer, unique=True)
    tipo_conta = db.Column(db.Integer)


class Contas(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    identificacao_fiscal = db.Column(db.String(14))
    saldo = db.Column(db.Integer)
    banco = db.Column(db.String(100))
    numero_conta = db.Column(db.Integer, unique=True)
    tipo_conta = db.Column(db.Integer)

