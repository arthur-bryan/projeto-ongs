from config import config
import sqlite3
import os


class Database:

    def __init__(self, nome_arquivo_database):
        self.__caminho = f"database"
        if not os.path.exists(self.__caminho):
            os.mkdir(self.__caminho)
        self.__conector = sqlite3.connect(f"{self.__caminho}/{nome_arquivo_database}")
        self.__cursor = self.__conector.cursor()

    def criar_tabela_usuarios(self):
        try:
            self.__cursor.execute("""
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                login_usuario TEXT,
                nome TEXT NOT NULL,
                sobrenome TEXT NOT NULL,
                email TEXT,
                senha TEXT,
                numero_telefone NUMBER,
                endereco TEXT,
                total_doacoes INTEGER,
                registrado_em DATE
            );
            """)
        except Exception as error:
            return {
                "status": False,
                "codigo": config.CODIGOS_HTTP["Internal Server Error"],
                "mensagem": f"Falha na criação da tabela 'usuarios'! {error}"
            }
        return {
            "status": True,
            "codigo": config.CODIGOS_HTTP["Created"],
            "mensagem": "Tabela 'usuarios' criada com sucesso!"
        }

    def criar_tabela_ongs(self):
        try:
            self.__cursor.execute("""
            CREATE TABLE IF NOT EXISTS ongs (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                representante TEXT NOT NULL,
                email TEXT,
                numero_contato_1 TEXT NOT NULL,
                numero_contato_2 TEXT,
                endereco TEXT NOT NULL,
                chave_pix TEXT NOT NULL,
                total_doacoes INTEGER,
                total_valor_arrecadado NUMBER,
                registrado_em TEXT NOT NULL
            );
            """)
        except Exception as error:
            return {
                "status": False,
                "codigo": config.CODIGOS_HTTP["Internal Server Error"],
                "mensagem": f"Falha na criação da tabela 'ongs'! {error}"
            }
        return {
            "status": True,
            "codigo": config.CODIGOS_HTTP["Created"],
            "mensagem": "Tabela 'ongs' criada com sucesso!"
        }

    def criar_tabela_doacoes(self):
        try:
            self.__cursor.execute("""
            CREATE TABLE IF NOT EXISTS doacoes (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                id_usuario INTEGER  NOT NULL,
                id_ong INTEGER NOT NULL,
                valor NUMBER NOT NULL,
                metodo_pagamento TEXT NOT NULL,
                status_pagamento TEXT NOT NULL,
                data_hora TEXT NOT NULL
            );
            """)
        except Exception as error:
            return {
                "status": False,
                "codigo": config.CODIGOS_HTTP["Internal Server Error"],
                "mensagem": f"Falha na criação da tabela 'doacoes'! {error}"
            }
        return {
            "status": True,
            "codigo": config.CODIGOS_HTTP["Created"],
            "mensagem": "Tabela 'doacoes' criada com sucesso!"
        }

    def checar_usuario_existe(self, login_usuario):
        self.__cursor.execute(f"""
            SELECT * FROM usuarios
            WHERE login_usuario=?""", (login_usuario,)
        )
        if self.__cursor.fetchall():
            return True
        return False

    def checar_email_existe(self, email):
        self.__cursor.execute(f"""
            SELECT * FROM usuarios
            WHERE email=?""", (email,)
                              )
        if self.__cursor.fetchall():
            return True
        return False

    def buscar_id_usuario_pelo_login(self, login_usuario):
        self.__cursor.execute(f"""
            SELECT id FROM usuarios
            WHERE login_usuario=?""", (login_usuario,))
        return self.__cursor.fetchall()

    def buscar_usuario_pelo_login(self, login_usuario):
        self.__cursor.execute(f"""
            SELECT * FROM usuarios
            WHERE login_usuario=?""", (login_usuario,))
        return self.__cursor.fetchall()

    def checar_ong_existe(self, nome_ong):
        self.__cursor.execute(f"""
            SELECT * FROM ongs
            WHERE nome=?""", (nome_ong,))
        if self.__cursor.fetchall():
            return True
        return False

    def validar_credenciais_login(self, login, senha):
        self.__cursor.execute(f"""
            SELECT * FROM usuarios
            WHERE email=? OR login_usuario=? AND senha=?""", (login, login, senha))
        if self.__cursor.fetchall():
            return True
        return False

    def buscar_id_ong_pelo_nome(self, nome_ong):
        self.__cursor.execute(f"""
            SELECT id FROM ongs
            WHERE nome=?""", (nome_ong,))
        return self.__cursor.fetchall()

    def buscar_ong_pelo_nome(self, nome_ong):
        self.__cursor.execute(f"""
            SELECT * FROM ongs
            WHERE nome=?""", (nome_ong,))
        return self.__cursor.fetchall()

    def contabilizar_doacao_ong(self, id_ong, valor):
        total_doacoes = self.obter_total_doacoes_ong(id_ong)[0][0]
        total_valor_arrecadado = self.obter_valor_arrecadado_ong(id_ong)[0][0]
        self.__cursor.execute(f"""
            UPDATE ongs
            SET total_doacoes = ?, total_valor_arrecadado = ?
            WHERE id=?""", (total_doacoes+1, total_valor_arrecadado+valor, id_ong))
        self.salvar_alteracoes()

    def obter_total_doacoes_ong(self, id_ong):
        self.__cursor.execute(f"""
            SELECT total_doacoes FROM ongs
            WHERE id=?""", (id_ong,))
        return self.__cursor.fetchall()

    def obter_valor_arrecadado_ong(self, id_ong):
        self.__cursor.execute(f"""
            SELECT total_valor_arrecadado FROM ongs
            WHERE id=?""", (id_ong,))
        return self.__cursor.fetchall()
    
    def contabilizar_doacao_usuario(self, id_usuario):
        total_doacoes = self.obter_total_doacoes_usuario(id_usuario)[0][0]
        self.__cursor.execute(f"""
            UPDATE usuarios
            SET total_doacoes = ?
            WHERE id=?""", (total_doacoes+1, id_usuario))
        self.salvar_alteracoes()

    def obter_total_doacoes_usuario(self, id_usuario):
        self.__cursor.execute(f"""
            SELECT total_doacoes FROM usuarios
            WHERE id=?""", (id_usuario,))
        return self.__cursor.fetchall()

    def executar_procedimento(self, sql_string, dados=None):
        self.__cursor.execute(sql_string, dados)

    def salvar_alteracoes(self):
        self.__conector.commit()
