import requests
from camera import tirar_foto
from camera import video
from solucao.collector import ajustaIMG

import threading

from rubik.cube             import Cube
from rubik.solve            import Solver

from solucao.classes.recortaFace    import recortarall
from solucao.classes.cor            import getCorCubo

# URL do servidor no EV3
ev3_server_url = "http://192.168.0.123:4040"  # Substitua pelo IP correto do seu EV3
def scam_cubo(): 
    
    # Face 1
    tirar_foto()
        
    # Face 2
    movimenta("Braco")
    tirar_foto()

    
    # Face 3
    movimenta("Braco")
    tirar_foto()
    
    # Face 4
    movimenta("Braco")
    tirar_foto()
   
    # Face 5
    movimenta("Base")
    movimenta("Braco")
    tirar_foto()
    
    # Face 6
    movimenta("Braco")
    movimenta("Braco")
    tirar_foto()
    
# Função para enviar dados para a URL de movimentação
def movimenta(data):
    url = f"{ev3_server_url}/movimenta"
    response = requests.post(url, data=data)
    return response.json()

# Função para enviar um arquivo .txt para a URL de recebimento
def enviar(data):
    url = f"{ev3_server_url}/enviar"
    response = requests.post(url, data=data)
    return response.json()

# Exemplos de uso
if __name__ == "__main__":
    # Inicia camera
    # cube_video = threading.Thread(target=video)
    # cube_video.start()
    
    # Scaneia as faces
    scam_cubo()
    
    # Ajusta tamanho das imagens
    ajustaIMG()
    
    # recortarall(debug=True)
    
    # Busca cores
    c = Cube(getCorCubo())
    print(c)
    
    # Gera solução
    # solver = Solver(c)
    # solver.solve()    
    # response = enviar(solver.moves)