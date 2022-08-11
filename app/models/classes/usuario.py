
class Usuario:

    def __init__(self):
        self.id = ""
        self.login_usuario = ""
        self.nome = ""
        self.sobrenome = ""
        self.email = ""
        self.senha = ""
        self.numero_telefone = ""
        self.endereco = ""
        self.total_doacoes = 0
        self.registrado_em = ""

    def json(self):
        return {
            "id": self.id,
            "login_usuario": self.login_usuario,
            "nome": self.nome,
            "sobrenome": self.sobrenome,
            "email": self.email,
            "senha": self.senha,
            "numero_telefone": self.numero_telefone,
            "endereco": self.endereco,
            "total_doacoes": self.total_doacoes,
            "registrado_em": self.registrado_em
        }
