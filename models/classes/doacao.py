class Doacao:

    def __init__(self):
        self.login_usuario = ""
        self.id_usuario = ""
        self.nome_ong = ""
        self.id_ong = ""
        self.valor = ""
        self.metodo_pagamento = ""
        self.status_pagamento = ""
        self.data_hora = ""

    def json(self):
        return {
            "login_usuario": self.login_usuario,
            "id_usuario": self.id_usuario,
            "nome_ong": self.nome_ong,
            "id_ong": self.id_ong,
            "valor": self.valor,
            "metodo_pagamento": self.metodo_pagamento,
            "status_pagamento": self.status_pagamento,
            "data_hora": self.data_hora
        }

