class ONG:

    def __init__(self):
        self.id = ""
        self.nome = ""
        self.representante = ""
        self.email = ""
        self.numero_contato_1 = ""
        self.numero_contato_2 = ""
        self.endereco = ""
        self.chave_pix = ""
        self.total_doacoes = 0
        self.total_valor_arrecadado = 0.0
        self.registrado_em = ""

    def json(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "representante": self.representante,
            "email": self.email,
            "numeco_contato_1": self.numero_contato_1,
            "numero_contato_2": self.numero_contato_2,
            "endereco": self.endereco,
            "chave_pix": self.chave_pix,
            "total_doacoes": self.total_doacoes,
            "total_valor_arrecadado": self.total_valor_arrecadado,
            "registrado_em": self.registrado_em
        }
