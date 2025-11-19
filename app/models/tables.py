from app import db 

class Aluno(db.Model):
    __tablename__ = 'alunos' 
#criação das colunas
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    cpf = db.Column(db.String(14), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    telefone = db.Column(db.String(20)) 
    matricula = db.Column(db.String(20), unique=True, nullable=False)

    #1 : N um aluno pode ter vários veículos
    veiculos = db.relationship('Veiculo',backref='dono', lazy=True) #backref cria um virtual atributo "dono"

    def __repr__(self):
        return f"<Aluno {self.nome}>"
    
class Veiculo(db.Model): 
    __tablename__ = 'veiculos'

    id = db.Column(db.Integer, primary_key=True)
    placa = db.Column(db.String(10), nullable=False, unique=True)
    modelo = db.Column(db.String(50), nullable=False)
    cor = db.Column(db.String(20))

    db.relationship('Movimentacao', backref='veiculo', lazy=True) #fk para aluno    

    def __repr__(self):
        return f"<Veiculo {self.placa}>"
    
class Movimentacao(db.Model):
    __tablename__ = 'movimentacoes'

    id = db.Column(db.Integer, primary_key=True)
    data_entrada = db.Column(db.DateTime, default=datetime.now)
    data_saida = db.Column(db.DateTime, nullable=True)


    

