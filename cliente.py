import requests
import json

# URL do servidor no EV3
ev3_server_url = "http://192.168.0.123:4040"  # Substitua pelo IP correto do seu EV3

# Função para enviar dados para a URL de movimentação
def movimenta(data):
    url = f"{ev3_server_url}/movimenta"
    response = requests.post(url, data=data)
    return response.json()

# Função para enviar um arquivo .txt para a URL de recebimento
def recebe(file_path):
    with open(file_path, "r") as file:
        data = file.read()
    url = f"{ev3_server_url}/recebe"
    response = requests.post(url, data=data)
    return response.json()

# Exemplos de uso
if __name__ == "__main__":
    # Solicitar movimentação
    # movimenta_data = "Base"
    movimenta_data = "Braco"
    response = movimenta(movimenta_data)
    print("Resposta de movimenta:", response)

    # Enviar um arquivo .txt
    # arquivo_txt = "solucao/solucao.txt"  # Substitua pelo caminho do seu arquivo
    # response = recebe(arquivo_txt)
    # print("Resposta de recebe:", response)