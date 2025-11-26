from app import db
from datetime import datetime

class Movimentacao(db.Model):
    __tablename__ = 'movimentacoes'

    id = db.Column(db.Integer, primary_key=True)
    data_entrada = db.Column(db.DateTime, default=datetime.now)
    data_saida = db.Column(db.DateTime, nullable=True)
