from app import config
from app import json
import unittest


class TesteCadastroUsuario(unittest.TestCase):

    CADASTRO_USUARIO_JSON = open("json/cadastro_usuario.json", "r").read()

    def test_validar_senha_cadastro_usuario(self):
        self.assertIsInstance(self.CADASTRO_USUARIO_JSON, str)
        dados = json.loads(self.CADASTRO_USUARIO_JSON)
        self.assertIsInstance(dados, dict)
        self.assertTrue(len(dados["conteudo"]["senha"]) >= config.TAMANHO_MINIMO_SENHA_USUARIO)
        self.assertIsNotNone(dados["conteudo"]["senha"])
        self.assertTrue(len(dados["conteudo"]["confirmacao_senha"]) >= config.TAMANHO_MINIMO_SENHA_USUARIO)
        self.assertIsNotNone(dados["conteudo"]["confirmacao_senha"])
        self.assertEqual(dados["conteudo"]["senha"], dados["conteudo"]["confirmacao_senha"])

    def test_obter_dados_cadastro_usuario(self):
        self.assertIsInstance(self.CADASTRO_USUARIO_JSON, str)
        dados = json.loads(self.CADASTRO_USUARIO_JSON)
        self.assertIsInstance(dados, dict)
        self.assertTrue(dados["tipo"], "cadastro_usuario")
        self.assertTrue(str(dados["conteudo"]["login_usuario"]).isascii())
        self.assertTrue(str(dados["conteudo"]["nome"]).isascii())
        self.assertTrue(str(dados["conteudo"]["sobrenome"]).isascii())
        self.assertTrue(str(dados["conteudo"]["email"]).isascii())
        self.assertTrue(str(dados["conteudo"]["senha"]).isascii())
        self.assertTrue(str(dados["conteudo"]["numero_telefone"]).isascii())
        self.assertTrue(str(dados["conteudo"]["endereco"]).isascii())
        self.assertIsNotNone(dados["conteudo"]["senha"])
        self.assertIsNotNone(dados["conteudo"]["confirmacao_senha"])
        self.assertTrue(len(dados["conteudo"]["login_usuario"]) >= config.TAMANHO_MINIMO_LOGIN_USUARIO)
        self.assertTrue(len(dados["conteudo"]["senha"]) >= config.TAMANHO_MINIMO_SENHA_USUARIO)
        self.assertTrue(len(dados["conteudo"]["confirmacao_senha"]) >= config.TAMANHO_MINIMO_SENHA_USUARIO)


class TesteLoginUsuario(unittest.TestCase):

    LOGIN_JSON = open("json/login.json", "r").read()

    def test_obter_dados_login(self):
        self.assertIsInstance(self.LOGIN_JSON, str)
        dados = json.loads(self.LOGIN_JSON)
        self.assertEqual(dados["tipo"], "login")
        self.assertIsNotNone(dados["conteudo"]["login"])
        self.assertTrue(str(dados["conteudo"]["login"]).isascii())
        self.assertIsNotNone(dados["conteudo"]["senha"])
        self.assertTrue(str(dados["conteudo"]["senha"]).isascii())
        self.assertTrue(len(dados["conteudo"]["login"]) >= config.TAMANHO_MINIMO_LOGIN_USUARIO)
        self.assertTrue(len(dados["conteudo"]["senha"]) >= config.TAMANHO_MINIMO_SENHA_USUARIO)


class TesteCadastroONG(unittest.TestCase):

    CADASTRO_ONG_JSON = open("json/cadastro_ong.json", "r").read()

    def test_obter_dados_cadastro_ong(self):
        self.assertIsInstance(self.CADASTRO_ONG_JSON, str)
        dados = json.loads(self.CADASTRO_ONG_JSON)
        self.assertIsInstance(dados, dict)
        self.assertTrue(dados["tipo"], "cadastro_ong")
        self.assertTrue(str(dados["conteudo"]["nome"]).isascii())
        self.assertTrue(str(dados["conteudo"]["representante"]).isascii())
        self.assertTrue(str(dados["conteudo"]["email"]).isascii())
        self.assertTrue(str(dados["conteudo"]["email"]).isascii())
        self.assertTrue(str(dados["conteudo"]["numero_contato_1"]).isascii())
        self.assertTrue(str(dados["conteudo"]["endereco"]).isascii())
        self.assertTrue(str(dados["conteudo"]["chave_pix"]).isascii())
        self.assertIsInstance(float(dados["conteudo"]["total_doacoes"]), float)
        self.assertIsInstance(float(dados["conteudo"]["total_valor_arrecadado"]), float)
        self.assertTrue(len(dados["conteudo"]["nome"]) >= config.TAMANHO_MINIMO_NOME_ONG)


class TesteRegistroDoacao(unittest.TestCase):

    DOACAO_JSON = open("json/doacao.json", "r").read()

    def test_obter_dados_doacao(self):
        self.assertIsInstance(self.DOACAO_JSON, str)
        dados = json.loads(self.DOACAO_JSON)
        self.assertIsInstance(dados, dict)
        self.assertTrue(dados["tipo"], "doacao")
        self.assertTrue(str(dados["conteudo"]["login_usuario"]).isascii())
        self.assertTrue(str(dados["conteudo"]["nome_ong"]).isascii())
        self.assertIsInstance(float(dados["conteudo"]["valor"]), float)
        self.assertTrue(str(dados["conteudo"]["metodo_pagamento"]).isascii())
        self.assertTrue(str(dados["conteudo"]["status_pagamento"]).isascii())
        self.assertTrue(len(dados["conteudo"]["login_usuario"]) >= config.TAMANHO_MINIMO_LOGIN_USUARIO)
        self.assertTrue(len(dados["conteudo"]["nome_ong"]) >= config.TAMANHO_MINIMO_NOME_ONG)


if __name__ == "__main__":
    unittest.main()
