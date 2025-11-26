from app import db
from Usuario import Usuario

class Aluno(Usuario):
    __tablename__ = 'alunos' 

    def __init__(self) -> None:
        super().__init__()

    #1 : N um aluno pode ter vários veículos
    veiculos = db.relationship('Veiculo',backref='dono', lazy=True) #backref cria um virtual atributo "dono"

    def __repr__(self):
        return f'<Aluno {self.id} {self.nome}>'
