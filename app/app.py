from flask import Flask, render_template, flash, redirect, url_for, request, session
from app.controllers.controlador_interface import ControladorInterface
from app.controllers.controlador_database import ControladorDatabase
from app.config import config
import json


controlador_interface = ControladorInterface()
controlador_database = ControladorDatabase(config.NOME_ARQUIVO_DATABASE)

app = Flask(__name__, template_folder='templates')
app.secret_key = 'super secret key'


@app.route("/", methods=['GET'])
def index():
    if request.method == 'GET':
        data = {
            'usuarios': controlador_database.obter_usuarios_cadastrados(),
            'ongs': controlador_database.obter_ongs_cadastradas(),
            'doacoes': controlador_database.obter_doacoes_realizadas()
        }
        return render_template('index.html', **data)


@app.route('/cadastro-usuario', methods=['POST'])
def cadastro_usuario():
    requisicao_json = {
        "tipo": "cadastro_usuario",
        "conteudo": {
            "login_usuario": request.form.get('login_usuario'),
            "nome": request.form.get('nome'),
            "sobrenome": request.form.get('sobrenome'),
            "email": request.form.get('email'),
            "senha": request.form.get('senha'),
            "confirmacao_senha": request.form.get('confirmacao_senha'),
            "endereco": "",
            "numero_telefone": "",
            "total_doacoes": 0
        }
    }
    validacao_senha_cadastro = controlador_interface.validar_senha_cadastro(requisicao_json)
    if validacao_senha_cadastro["status"]:
        print(json.dumps(validacao_senha_cadastro, indent=4))
        usuario = controlador_interface.obter_dados_cadastro_usuario(requisicao_json)
        resposta = json.dumps(controlador_database.cadastrar_usuario(usuario), indent=4)
        flash(resposta)
        print(resposta)
    else:
        resposta = json.dumps(validacao_senha_cadastro, indent=4)
        flash(resposta)
        print(resposta)
    return redirect(url_for("index"))


@app.route('/cadastro-ong', methods=['POST'])
def cadastro_ong():
    requisicao_json = {
      "tipo": "cadastro_ong",
      "conteudo": {
        "nome_ong": request.form.get('nome_ong'),
        "representante": request.form.get('representante'),
        "email_ong": request.form.get('email_ong'),
        "numero_contato_1": request.form.get('numero_contato_1'),
        "numero_contato_2": request.form.get('numero_contato_2') if 'numero_contato_2' in request.form.keys() else "",
        "endereco": request.form.get('endereco'),
        "chave_pix": request.form.get('chave_pix'),
        "total_doacoes": 0,
        "total_valor_arrecadado": 0.0
      }
    }
    ong = controlador_interface.obter_dados_cadastro_ong(requisicao_json)
    resposta = json.dumps(controlador_database.cadastrar_ong(ong), indent=4)
    flash(resposta)
    print(resposta)
    return redirect(url_for("index"))


@app.route('/registro-doacao', methods=['POST'])
def registro_doacao():
    requisicao_json = {
        "tipo": "doacao",
        "conteudo": {
            "login_usuario_ong": request.form.get('login_usuario_ong'),
            "nome_ong": request.form.get('doacao_nome_ong'),
            "valor": request.form.get('valor'),
            "metodo_pagamento": request.form.get('metodo_pagamento')
        }
    }
    doacao = controlador_interface.obter_dados_doacao(requisicao_json)
    resposta = json.dumps(controlador_database.registrar_doacao(doacao), indent=4)
    flash(resposta)
    print(resposta)
    return redirect(url_for("index"))



# @app.route('/cadastro-ong')
# def form_example():
#     return 'Form Data Example'
#
#
# @app.route('/registro-doacao')
# def json_example():
#     return 'JSON Object Example'
#
#
# @app.route("/logout")
# @login_required
# def logout():
#     logout_user()
#     flash("Pesquisa concluida. Obrigado por participar!")
#     return redirect(url_for("results"))
