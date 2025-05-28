from flask import Flask, jsonify, request
from faker import Faker
import random

#variáveis
app = Flask(__name__)
fake = Faker()

# Gerar usuários randômicos com a biblioteca Faker
usuarios = [
    {
        "id": i,
        "nome": fake.name(),
        "email": fake.email()
    }
    for i in range(1, 11)
]

# Rota para listar todos os usuários
@app.route('/usuarios', methods=['GET'])
def listar_usuarios():
    return jsonify(usuarios)

# Rota para obter um usuário por ID
@app.route('/usuarios/<int:id>', methods=['GET'])
def obter_usuario(id):
    usuario = next((u for u in usuarios if u["id"] == id), None)
    if usuario:
        return jsonify(usuario)
    return jsonify({"erro": "Usuário não encontrado"}), 404

# Rota para criar novo usuário
@app.route('/usuarios', methods=['POST'])
def criar_usuario():
    novo = request.json
    novo["id"] = max(u["id"] for u in usuarios) + 1 if usuarios else 1
    usuarios.append(novo)
    return jsonify(novo), 201

# Rota para atualizar um usuário
@app.route('/usuarios/<int:id>', methods=['PUT'])
def atualizar_usuario(id):
    usuario = next((u for u in usuarios if u["id"] == id), None)
    if not usuario:
        return jsonify({"erro": "Usuário não encontrado"}), 404

    dados = request.json
    usuario.update(dados)
    return jsonify(usuario)

# Rota para deletar um usuário
@app.route('/usuarios/<int:id>', methods=['DELETE'])
def deletar_usuario(id):
    global usuarios
    usuarios = [u for u in usuarios if u["id"] != id]
    return jsonify({"mensagem": "Usuário deletado"}), 200

if __name__ == '__main__':
    app.run(debug=True)
