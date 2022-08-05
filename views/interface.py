from controllers.controlador import Controlador
import json


class WebSite:

    def __init__(self):
        self.__controlador = Controlador

    def listener_requisicoes(self, requisicao_json):
        requisicao = json.loads(requisicao_json)
        if requisicao["tipo"] == "cadastro":
            self.requisicao_cadastro(requisicao_json)
        elif requisicao["tipo"] == "login":
            self.requisicao_login(requisicao_json)
        elif requisicao["tipo"] == "doacao":
            self.requisicao_doacao(requisicao_json)
        elif requisicao["tipo"] == "logout":
            self.requisicao_logout(requisicao_json)
        else:
            pass

    def requisicao_cadastro(self, requisicao_json):
        if self.__controlador.validar_senha_cadastro(requisicao_json):
            resposta = self.__controlador.cadastrar_usuario(requisicao_json)
            print(resposta)

    def requisicao_login(self, requisicao_json):
        resposta = self.__controlador.login_usuario(requisicao_json)
        print(resposta)

    def requisicao_doacao(self, requisicao_json):
        resposta = self.__controlador.doacao_usuario(requisicao_json)
        print(resposta)

    def requisicao_logout(self, requisicao_json):
        resposta = self.__controlador.logout_usuario(requisicao_json)
        print(resposta)