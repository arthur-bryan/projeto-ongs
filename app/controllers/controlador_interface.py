from app.utils import utils
from app.models.classes.usuario import Usuario
from app.models.classes.doacao import Doacao
from app.models.classes.log import Logger
from app.models.classes.ong import ONG
import json


class ControladorInterface:

    def __init__(self):
        self.__logger = Logger("APLICACAO")

    @staticmethod
    def validar_senha_cadastro(dados_cadastro_json):
        dados_cadastro_json = str(dados_cadastro_json).replace("'", '"')
        dados_json = json.loads(dados_cadastro_json)
        if dados_json["conteudo"]["senha"] == dados_json["conteudo"]["confirmacao_senha"]:
            return {
                "status": True,
                "codigo": None,
                "mensagem": f"Senhas conferem!"
            }
        return {
            "status": False,
            "codigo": None,
            "mensagem": f"Senhas nao conferem!"
        }

    @staticmethod
    def obter_dados_cadastro_usuario(requisicao_json):
        requisicao = json.loads(str(requisicao_json).replace("'", '"'))
        usuario = Usuario()
        usuario.login_usuario = requisicao["conteudo"]["login_usuario"]
        usuario.nome = requisicao["conteudo"]["nome"]
        usuario.sobrenome = requisicao["conteudo"]["sobrenome"]
        usuario.email = requisicao["conteudo"]["email"]
        usuario.senha = requisicao["conteudo"]["senha"]
        usuario.numero_telefone = requisicao["conteudo"]["numero_telefone"]
        usuario.endereco = requisicao["conteudo"]["endereco"]
        usuario.registrado_em = utils.obter_data_atual()
        return usuario
    
    @staticmethod
    def obter_dados_cadastro_ong(requisicao_json):
        print(requisicao_json)
        requisicao = json.loads(str(requisicao_json).replace("'", '"'))
        ong = ONG()
        ong.nome = requisicao["conteudo"]["nome_ong"]
        ong.representante = requisicao["conteudo"]["representante"]
        ong.email = requisicao["conteudo"]["email_ong"]
        ong.numero_contato_1 = requisicao["conteudo"]["numero_contato_1"]
        ong.numero_contato_2 = requisicao["conteudo"]["numero_contato_2"]
        ong.endereco = requisicao["conteudo"]["endereco"]
        ong.chave_pix = requisicao["conteudo"]["chave_pix"]
        ong.registrado_em = utils.obter_data_atual()
        return ong

    @staticmethod
    def obter_dados_login(requisicao_json):
        requisicao = json.loads(str(requisicao_json).replace("'", '"'))
        login = requisicao["conteudo"]["login"]
        senha = requisicao["conteudo"]["senha"]
        return login, senha

    @staticmethod
    def obter_dados_doacao(requisicao_json):
        requisicao = json.loads(str(requisicao_json).replace("'", '"'))
        doacao = Doacao()
        doacao.login_usuario = requisicao["conteudo"]["login_usuario_ong"]
        doacao.nome_ong = requisicao["conteudo"]["nome_ong"]
        doacao.valor = requisicao["conteudo"]["valor"]
        doacao.metodo_pagamento = requisicao["conteudo"]["metodo_pagamento"]
        doacao.status_pagamento = requisicao["conteudo"]["status_pagamento"] if "status_pagamento" in requisicao["conteudo"] else ""
        doacao.data_hora = utils.obter_data_atual()
        return doacao
    #
    # @staticmethod
    # def logout_usuario(requisicao_json):
    #     requisicao = json.loads(requisicao_json)
    #     email = requisicao["conteudo"]["email"]
    #     usuario_inscrito = Inscrito(email=email)
    #     usuario_inscrito.esta_conectado = False
    #     resposta = {
    #         "codigo": 200,
    #         "mensagem": f"Usuário com email {email} fez o logout com sucesso!"
    #     }
    #     return resposta
