import datetime

from models.classes.inscrito import Inscrito
import json


class Controlador:

    def __init__(self):
        pass

    @staticmethod
    def validar_senha_cadastro(requisicao_json):
        requisicao = json.loads(requisicao_json)
        senha = requisicao["conteudo"]["senha"]
        confirmacao_senha = requisicao["conteudo"]["confirmacao_senha"]
        return senha == confirmacao_senha

    @staticmethod
    def cadastrar_usuario(requisicao_json):
        requisicao = json.loads(requisicao_json)
        nome_completo = " ".join([requisicao["conteudo"]["nome"], requisicao["conteudo"]["sobrenome"]])
        nome_usuario = requisicao["conteudo"]["nome_usuario"]
        email = requisicao["conteudo"]["email"]
        senha = requisicao["conteudo"]["senha"]
        usuario_inscrito = Inscrito(usuario_login=nome_usuario,
                                    email=email,
                                    senha=senha)
        usuario_inscrito.esta_conectado = True
        usuario_inscrito.esta_cadastrado = True
        resposta = {
            "codigo": 200,
            "mensagem": f"Usuário {nome_usuario} foi cadastrado!"
        }
        return resposta

    @staticmethod
    def login_usuario(requisicao_json):
        requisicao = json.loads(requisicao_json)
        email = requisicao["conteudo"]["email"]
        senha = requisicao["conteudo"]["senha"]
        usuario_inscrito = Inscrito(email=email,
                                    senha=senha)
        usuario_inscrito.esta_conectado = True
        resposta = {
            "codigo": 200,
            "mensagem": f"Usuário com email {email} fez o login com sucesso!"
        }
        return resposta

    @staticmethod
    def doacao_usuario(requisicao_json):
        requisicao = json.loads(requisicao_json)
        id_doador = requisicao["conteudo"]["id_doador"]
        id_ong = requisicao["conteudo"]["id_ong"]
        valor = requisicao["conteudo"]["valor"]
        timestamp = datetime.datetime.now()
        metodo_pagamento = requisicao["conteudo"]["metodo_pagamento"]
        status_pagamento = requisicao["conteudo"]["status_pagamento"]
        resposta = {
            "codigo": 200,
            "mensagem": f"Doação no valor de {valor}, feita por {id_doador}, para a ONG {id_ong} feita com sucesso!"
        }
        return resposta

    @staticmethod
    def logout_usuario(requisicao_json):
        requisicao = json.loads(requisicao_json)
        email = requisicao["conteudo"]["email"]
        usuario_inscrito = Inscrito(email=email)
        usuario_inscrito.esta_conectado = False
        resposta = {
            "codigo": 200,
            "mensagem": f"Usuário com email {email} fez o logout com sucesso!"
        }
        return resposta
