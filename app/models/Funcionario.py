from app import db
from Usuario import Usuario

class Funcionario(Usuario):
    __tablename__ = 'funcionarios' 

    def __init__(self) -> None:
        super().__init__()

    def __repr__(self):
        return f'<Funcionario {self.id} {self.nome}>'
