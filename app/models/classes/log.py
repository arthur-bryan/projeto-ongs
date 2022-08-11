from app.utils import utils
import os


class Logger:

    def __init__(self, categoria):
        self.__categoria = categoria
        self.__caminho = "logs"
        if not os.path.exists(self.__caminho):
            os.mkdir(self.__caminho)
        self.__arquivo_log = open(f"{self.__caminho}/{categoria.lower()}.log", "a")

    def log_message(self, mensagem):
        self.__init__(self.__categoria)
        texto = mensagem["mensagem"]
        codigo = mensagem["codigo"]
        status = mensagem["status"]
        conteudo = f"{utils.obter_data_atual()},{texto},{codigo},{status}\n"
        self.__arquivo_log.write(conteudo)
        self.__arquivo_log.close()
        return mensagem
