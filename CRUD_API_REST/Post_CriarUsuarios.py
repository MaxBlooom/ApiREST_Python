import requests

dados = {"nome": "Ana Gabriela", "email": "ana.silva@email.com"}
res = requests.post("http://127.0.0.1:5000/usuarios", json=dados)

# Se o status code for 201, significa que o usuário foi criado com sucesso
print(res.status_code)
print(res.json())