from models.classes.visitante import Visitante
from datetime import datetime


class Inscrito(Visitante):

    def __init__(self, usuario_login=None, email=None, senha=None):
        super().__init__()
        self.usuario_login = usuario_login
        self.email = email
        self.senha = senha
        self.esta_conectado = False
        self.data_cadastro = datetime.now()
