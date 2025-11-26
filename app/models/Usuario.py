from app import db

class Usuario(db.Model):
    #__tablename__ = 'alunos' 

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    cpf = db.Coumn(db.String(14), nullable=False)
    email = db.Column(db.String(100), nullable=False) 
    telefne = db.Column(db.String(20))
    matricula = db.Column(db.String(20), unique=True, nullable=False)
  
    # Define um campo DECIMAL(10, 2) no banco de dados, 10 dígitos no total, 2 após a vírgula
    saldo = db.Column(db.Numeric(10, 2), nullable=False)

    #1 : N um aluno pode ter vários veículos
    #veiculos = db.relationship('Veiculo',backref='dono', lazy=True) #backref cria um virtual atributo "dono"

    #def __repr__(self):
    #    return f'<Aluno {self.id} {self.nome}>'
