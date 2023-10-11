#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port, Direction

from classes.braco  import Braco
from classes.base   import Base
from classes.sensor import Sensor

# Create your objects here.
ev3 = EV3Brick()

import socket
import json
from threading import Thread

# Configurações do servidor
host = "0.0.0.0"  # Ouça em todas as interfaces de rede
port = 4040

# Função para lidar com a rota /movimenta
def handle_movimenta(data):
    # Lógica para processar os dados de movimenta aqui
    response_data = {"message": "Comando de movimenta recebido", "data": data}
    return json.dumps(response_data)

# Função para lidar com a rota /recebe
def handle_recebe(data):
    # Lógica para processar a rota de recebe aqui
    # Por exemplo, salvar os dados recebidos em um arquivo .txt
    with open("dados_recebidos.txt", "w") as file:
        file.write(data)
    return json.dumps({"message": "Dados recebidos com sucesso"})

def handle_client(client_socket):
    request = client_socket.recv(1024).decode('utf-8')
    
    # Verifique qual rota está sendo acessada na requisição
    if request.startswith("POST /movimenta"):
        request_data = request.split("\r\n\r\n", 1)[-1]
        response = handle_movimenta(request_data)
        content_type = "application/json"
    elif request.startswith("POST /recebe"):
        request_data = request.split("\r\n\r\n", 1)[-1]
        response = handle_recebe(request_data)
        content_type = "application/json"
    else:
        response = json.dumps({"error": "Rota desconhecida"})
        content_type = "application/json"
    
    # Envie a resposta
    response_headers = "HTTP/1.1 200 OK\n\n"
    client_socket.send(response_headers.encode('utf-8'))
    client_socket.send(response.encode('utf-8'))
    client_socket.close()

# Configure o socket do servidor
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen(5)

print("Aguardando conexões em "+str(host)+":"+str(port)+"...")

while True:
    client_socket, addr = server_socket.accept()
    print("Conexão de "+str(addr))
    client_handler = Thread(target=handle_client, args=(client_socket,))
    client_handler.start()