from app.controllers.controlador_interface import ControladorInterface
from app.controllers.controlador_database import ControladorDatabase
from app.config import config
import json


class WebSite:

    def __init__(self):
        self.__controlador_interface = ControladorInterface()
        self.__controlador_database = ControladorDatabase(config.NOME_ARQUIVO_DATABASE)

    def listener_requisicoes(self, requisicao_json):
        requisicao = json.loads(requisicao_json)
        if requisicao["tipo"] == "cadastro_usuario":
            self.requisicao_cadastro_usuario(requisicao_json)
        elif requisicao["tipo"] == "cadastro_ong":
            self.requisicao_cadastro_ong(requisicao_json)
        elif requisicao["tipo"] == "login":
            self.requisicao_login(requisicao_json)
        elif requisicao["tipo"] == "doacao":
            self.requisicao_doacao(requisicao_json)
        # elif requisicao["tipo"] == "logout":
        #     self.requisicao_logout(requisicao_json)
        else:
            pass

    def requisicao_cadastro_usuario(self, requisicao_json):
        validacao_senha_cadastro = self.__controlador_interface.validar_senha_cadastro(requisicao_json)
        if validacao_senha_cadastro["status"]:
            print(json.dumps(validacao_senha_cadastro, indent=4))
            usuario = self.__controlador_interface.obter_dados_cadastro_usuario(requisicao_json)
            resposta = json.dumps(self.__controlador_database.cadastrar_usuario(usuario), indent=4)
            print(resposta)
        else:
            print(json.dumps(validacao_senha_cadastro, indent=4))

    def requisicao_cadastro_ong(self, requisicao_json):
        ong = self.__controlador_interface.obter_dados_cadastro_ong(requisicao_json)
        resposta = json.dumps(self.__controlador_database.cadastrar_ong(ong), indent=4)
        print(resposta)

    def requisicao_login(self, requisicao_json):
        login, senha = self.__controlador_interface.obter_dados_login(requisicao_json)
        resposta = json.dumps(self.__controlador_database.login_usuario(login, senha), indent=4)
        print(resposta)

    def requisicao_doacao(self, requisicao_json):
        doacao = self.__controlador_interface.obter_dados_doacao(requisicao_json)
        resposta = json.dumps(self.__controlador_database.registrar_doacao(doacao), indent=4)
        print(resposta)

    # def requisicao_logout(self, requisicao_json):
    #     resposta = self.__controlador_interface.logout_usuario(requisicao_json)
    #     print(resposta)
