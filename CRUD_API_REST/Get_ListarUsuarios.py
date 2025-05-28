import requests

# listando todos os usuários
res = requests.get("http://127.0.0.1:5000/usuarios")

#Atribuindo o retorno da requisição GET para uma lista de usuários
usuarios = res.json()  

for usuario in usuarios:
    print(usuario)
