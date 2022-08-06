import random
import json
import os

users = []
ongs = []
doacoes = []


def _round(number):
    for i in range(0, number):
        random_number = random.randint(1000, 9999)
        users.append(random_number)
        file_usuario = open(f"scripts/usuario{random_number}.json", "w")
        cadastro_usuario_template = {
            "tipo": f"cadastro_usuario",
            "conteudo": {
                "login_usuario": "login_usuario{random_number}",
                "nome": "Nome Usuario{random_number}",
                "sobrenome": "Sobrenome Usuario{random_number}",
                "email": "usuario{random_number}@email.com",
                "senha": "s3nh4_usu4r10{random_number}",
                "confirmacao_senha": "s3nh4_usu4r10{random_number}",
                "numero_telefone": "({random_number}) 11111-1111",
                "endereco": "Rua do Usuario{random_number}",
                "total_doacoes": 0
            }
        }
        string = json.dumps(cadastro_usuario_template).replace("{random_number}", str(random_number))
        file_usuario.write(string)
        file_usuario.close()

    for i in range(3, 5):
        random_number = random.randint(1000, 9999)
        ongs.append(random_number)
        file_ong = open(f"scripts/ong{random_number}.json", "w")
        cadastro_usuario_template = {
            "tipo": "cadastro_ong",
            "conteudo": {
                "nome": "Nome ONG {random_number}",
                "representante": "Representante ONG{random_number}",
                "email": "representante{random_number}@ong.com.br",
                "numero_contato_1": "({random_number}) 00000-0000",
                "numero_contato_2": "",
                "endereco": "Rua da ONG {random_number}",
                "chave_pix": "ch4v3p1x0ngnumber{random_number}",
                "total_doacoes": 0,
                "total_valor_arrecadado": 0.0
            }
        }
        string = json.dumps(cadastro_usuario_template).replace("{random_number}", str(random_number))
        file_ong.write(string)
        file_ong.close()

    for i in range(5, 20):
        random_user = random.choice(users)
        random_ong = random.choice(ongs)
        random_number = random.randint(1000, 9999)
        file_doacao = open(f"scripts/doacao{random_number}.json", "w")
        cadastro_usuario_template = {
            "tipo": "doacao",
            "conteudo": {
                "login_usuario": f"login_usuario{random_user}",
                "nome_ong": f"Nome ONG {random_ong}",
                "valor": round(random.uniform(1.5, 75.5), 2),
                "metodo_pagamento": "PIX",
                "status_pagamento": "Concluído"
            }
        }
        string = json.dumps(cadastro_usuario_template).replace("{random_number}", str(random_number))
        file_doacao.write(string)
        file_doacao.close()


number = random.randint(5, 15)
print(number)
_round(number)
