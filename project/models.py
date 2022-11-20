from flask_login import UserMixin
from . import db


class User(UserMixin, db.Model):
    __tablename__ = 'User'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password  = db.Column(db.String(100))
    name = db.Column(db.String(1000))

    def __init__(self, email, password, name):
        self.email = email
        self.password = password
        self.name = name

    def __repr__(self):
        return '<id {}>'.format(self.id)


class Catalogo(db.Model):
    __tablename__ = 'Catalogo'
    
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(180))
    complexidade = db.Column(db.String(20))
    escopo = db.Column(db.String(180))
    tempo = db.Column(db.String(180))
    entregaveis = db.Column(db.String(180))
    perfil = db.Column(db.String(180))
    atividades = db.Column(db.String(180))
    
    def __init__(self, nome, complexidade, escopo, tempo, entregaveis, perfil, atividades):
        self.nome = nome
        self.complexidade = complexidade
        self.escopo = escopo
        self.tempo = tempo
        self.entregaveis = entregaveis
        self.perfil = perfil
        self.atividades = atividades
        
    def __repr__(self):
        return '<id {}>'.format(self.id)
