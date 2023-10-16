import requests
import configparser
from PIL import Image 
import threading
import os

from rubik.cube             import Cube
from rubik.solve            import Solver

from classes.camera         import tirar_foto
from classes.camera         import video
from classes.recortaFace    import recortarall
from classes.cor            import getCorCubo

def ajustaIMG(rotate=False):
    for i in range(6):
        arquivo = "face"+str(i+1)+".png"

        # creating a object 
        image = Image.open(r"fotos/"+arquivo)

        MAX_SIZE = (500, 500)
        image.thumbnail(MAX_SIZE)

        image_rotated = image
        if rotate:
            image_rotated = image.rotate(-90, expand=True)

        # Crie o diretório de saída, se não existir
        os.makedirs("fotos/adjusted/", exist_ok=True)

        # creating thumbnail
        image_rotated.save("fotos/adjusted/"+arquivo)
        os.remove("fotos/"+arquivo)

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
    
    movimenta("Base-e")
    movimenta("Braco")
    movimenta("Base-e")
    
# Função para enviar dados para a URL de movimentação
def movimenta(data):
    url = f"{ev3_server_url}/movimenta"
    
    response = requests.post(url, data=data)
    return response.json()

# Função para enviar um os passos de solução do cubo para a URL de envio
def enviar(data):
    url = f"{ev3_server_url}/enviar"
    response = requests.post(url, data=data)
    return response.json()

# Exemplos de uso
if __name__ == "__main__":
    # URL do servidor no EV3
    config = configparser.RawConfigParser()
    config.read("configuration/config_core.ini")

    ev3_server_url = config['CONFIGURATION']['host_EV3']  # Substitua pelo IP correto do seu EV3
    
    # # Inicia camera
    # # cube_video = threading.Thread(target=video)
    # # cube_video.start()
    
    # # Scaneia as faces
    # scam_cubo()
    
    # Ajusta tamanho das imagens
    ajustaIMG(rotate=config.getboolean('CONFIGURATION','rotate'))
    
    recortarall(debug=config.getboolean('CONFIGURATION','debug_recort'))
    
    # Busca cores           
    c = Cube(getCorCubo())
    print(c)
    
    # Gera solução
    solver = Solver(c)
    solver.solve()
    
    print(solver.moves) # response = enviar(solver.moves)