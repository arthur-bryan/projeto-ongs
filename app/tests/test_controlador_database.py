from app import ControladorDatabase
from app import Database
from app import Usuario
from app import config
import unittest


controlador_databse = ControladorDatabase()
controlador_databse.database = Database("teste.db")
controlador_databse.database.criar_tabela_usuarios()
controlador_databse.database.criar_tabela_ongs()
controlador_databse.database.criar_tabela_doacoes()


class TesteCadastroUsuario(unittest.TestCase):

    CADASTRO_USUARIO_JSON = open("json/cadastro_usuario.json", "r").read()

    def test_cadastrar_usuario_existente(self):
        usuario = Usuario()
        usuario.login_usuario = "teste_usuario"
        usuario.nome = "teste"
        usuario.sobrenome = "sobreteste"
        usuario.email = "teste_usuario@email.com"
        resultado = controlador_databse.cadastrar_usuario(usuario)
        self.assertTrue(resultado["codigo"] in config.CODIGOS_HTTP.values())
        if resultado["status"]:
            self.assertLessEqual(resultado["codigo"], 399)
        else:
            self.assertGreaterEqual(resultado["codigo"], 400)


if __name__ == "__main__":
    unittest.main()
