from app import db

class Veiculo(db.Model): 
    __tablename__ = 'veiculos'

    id = db.Column(db.Integer, primary_key=True)
    placa = db.Column(db.String(10), nullable=False, unique=True)
    modelo = db.Column(db.String(50), nullable=False)
    cor = db.Column(db.String(20))

    db.relationship('Movimentacao', backref='veiculo', lazy=True) #fk para aluno    

    def __repr__(self):
        return f"<Veiculo {self.placa}>"