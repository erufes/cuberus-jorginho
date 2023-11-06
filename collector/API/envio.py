import requests

# URL da rota de upload da sua API Flask
url = 'http://192.168.1.105:5000/upload'  # Substitua pela URL correta, se necessário
name = "face-1"

# Arquivo de imagem que você deseja enviar
imagem = open(name + '.jpg', 'rb')  # Substitua 'exemplo.jpg' pelo caminho para sua imagem

# Nome opcional para a imagem (deixe em branco se não quiser fornecer um nome)

# Dados para a solicitação POST
file    = {'file': (name + '.jpg', imagem)}

# Faça a solicitação POST
response = requests.post(url, files=file)

# Verifique a resposta da API
if response.status_code == 200:
    print('Imagem enviada com sucesso!')
else:
    print('Erro ao enviar imagem:', response.status_code)