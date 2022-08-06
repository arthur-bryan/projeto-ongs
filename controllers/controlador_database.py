from models.classes.database import Database
from models.classes.log import Logger
from config import config


class ControladorDatabase:

    def __init__(self):
        self.__database = Database(config.NOME_ARQUIVO_DATABASE)
        self.__logger = Logger("DATABASE")
        self.__database.criar_tabela_usuarios()
        self.__database.criar_tabela_ongs()
        self.__database.criar_tabela_doacoes()

    def cadastrar_usuario(self, usuario):
        if self.__database.checar_usuario_existe(usuario.login_usuario):
            resultado = {
                "status": False,
                "codigo": config.CODIGOS_HTTP["Unauthorized"],
                "mensagem": f"Usuario {usuario.login_usuario} ja esta em uso!"
            }
            return self.__logger.log_message(mensagem=resultado)

        if self.__database.checar_email_existe(usuario.email):
            resultado = {
                "status": False,
                "codigo": config.CODIGOS_HTTP["Unauthorized"],
                "mensagem": f"Email {usuario.email} ja esta em uso!"
            }
            return self.__logger.log_message(mensagem=resultado)

        sql_string = f"""
            INSERT INTO usuarios (login_usuario, nome, sobrenome, email, senha, numero_telefone, endereco,
                                  total_doacoes, registrado_em)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"""
        dados = (usuario.login_usuario, usuario.nome, usuario.sobrenome, usuario.email,
                 usuario.senha, usuario.numero_telefone, usuario.endereco, usuario.total_doacoes,
                 usuario.registrado_em)
        try:
            self.__database.executar_procedimento(sql_string=sql_string, dados=dados)
        except Exception as error:
            resultado = {
                "status": False,
                "codigo": config.CODIGOS_HTTP["Internal Server Error"],
                "mensagem": f"Falha ao cadastrar usuario '{usuario.login_usuario}': {error}"
            }
            return self.__logger.log_message(mensagem=resultado)
        else:
            self.__database.salvar_alteracoes()
            resultado = {
                "status": True,
                "codigo": config.CODIGOS_HTTP["Created"],
                "mensagem": f"Usuario '{usuario.login_usuario}' cadastrado com sucesso!"
            }
            return self.__logger.log_message(mensagem=resultado)

    def cadastrar_ong(self, ong):
        if self.__database.checar_ong_existe(ong.nome):
            resultado = {
                "status": False,
                "codigo": config.CODIGOS_HTTP["Unauthorized"],
                "mensagem": f"ONG '{ong.nome}' ja esta cadastrada!"
            }
            return self.__logger.log_message(mensagem=resultado)

        sql_string = f"""
            INSERT INTO ongs (nome, representante, email, numero_contato_1, numero_contato_2, endereco, chave_pix,
                              total_doacoes, total_valor_arrecadado, registrado_em)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""
        dados = (ong.nome, ong.representante, ong.email, ong.numero_contato_1, ong.numero_contato_2,
                 ong.endereco, ong.chave_pix, ong.total_doacoes, ong.total_valor_arrecadado,
                 ong.registrado_em)
        try:
            self.__database.executar_procedimento(sql_string=sql_string, dados=dados)
        except Exception as error:
            resultado = {
                "status": False,
                "codigo": config.CODIGOS_HTTP["Internal Server Error"],
                "mensagem": f"Falha ao cadastrar ONG '{ong.nome}': {error}"
            }
            return self.__logger.log_message(mensagem=resultado)
        else:
            self.__database.salvar_alteracoes()
            resultado = {
                "status": True,
                "codigo": config.CODIGOS_HTTP["Created"],
                "mensagem": f"ONG '{ong.nome}' cadastrada com sucesso!"
            }
            return self.__logger.log_message(mensagem=resultado)

    def login_usuario(self, login, senha):
        if self.__database.validar_credenciais_login(login, senha):
            resultado = {
                "status": True,
                "codigo": config.CODIGOS_HTTP["Ok"],
                "mensagem": f"Usuário '{login}' logado com sucesso!"
            }
            return self.__logger.log_message(mensagem=resultado)
        resultado = {
            "status": False,
            "codigo": config.CODIGOS_HTTP["Unauthorized"],
            "mensagem": f"Falha no ao realizar login! Usuario '{login}'."
        }
        return self.__logger.log_message(mensagem=resultado)

    def registrar_doacao(self, doacao):
        try:
            id_usuario = self.__database.buscar_id_usuario_pelo_login(doacao.login_usuario)[0][0]
            id_ong = self.__database.buscar_id_ong_pelo_nome(doacao.nome_ong)[0][0]
        except (KeyError, IndexError):
            resultado = {
                "status": False,
                "codigo": config.CODIGOS_HTTP["Not Found"],
                "mensagem": f"Falha na doacao! ONG '{doacao.nome_ong}' nao encontrada."
            }
            return self.__logger.log_message(mensagem=resultado)
        else:
            if not id_ong:
                resultado = {
                    "status": False,
                    "codigo": config.CODIGOS_HTTP["Not Found"],
                    "mensagem": f"Falha na doacao! ONG '{doacao.nome_ong}' nao encontrada."
                }
                return self.__logger.log_message(mensagem=resultado)
            sql_string = f"""
                INSERT INTO doacoes (id_usuario, id_ong, valor, metodo_pagamento, status_pagamento, data_hora)
                VALUES (?, ?, ?, ?, ?, ?)"""
            dados = (id_usuario, id_ong, doacao.valor, doacao.metodo_pagamento, doacao.status_pagamento, doacao.data_hora)
            try:
                self.__database.executar_procedimento(sql_string=sql_string, dados=dados)
                self.__database.contabilizar_doacao_ong(id_ong, doacao.valor)
                self.__database.contabilizar_doacao_usuario(id_usuario)
            except Exception as error:
                resultado = {
                    "status": False,
                    "codigo": config.CODIGOS_HTTP["Internal Server Error"],
                    "mensagem": f"Falha ao registrar doacao:  De usuario com ID {id_usuario} para ONG com ID {id_ong}. {error}"
                }
                return self.__logger.log_message(mensagem=resultado)
            else:
                self.__database.salvar_alteracoes()
                resultado = {
                    "status": True,
                    "codigo": config.CODIGOS_HTTP["Created"],
                    "mensagem": f"Doacao bem sucedida: De usuario com ID {id_usuario} para ONG com ID {id_ong}."
                }
                return self.__logger.log_message(mensagem=resultado)
