from operator import xor
from time import sleep
import requests
import configparser
from PIL import Image 
import threading
import os
import shutil

from rubik.cube     import Cube
from rubik.solve    import Solver

from classes.camera         import camera
from classes.recortaFace    import recortarall
from classes.cor            import getCorCubo

from classes.movimentacao import *

def ajustaIMG(rotate=False, delete=False):
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
        
        if delete:
            os.remove("fotos/"+arquivo)

def scam_cubo(url, can): 
    
    # Face 1
    can.tirar_foto()
        
    # Face 2
    movimenta("Braco", url)
    can.tirar_foto()
    
    # Face 3
    movimenta("Braco", url)
    can.tirar_foto()
    
    # Face 4
    movimenta("Braco", url)
    can.tirar_foto()
   
    # Face 5
    movimenta("Base", url)
    movimenta("Braco", url)
    can.tirar_foto()
    
    # Face 6
    movimenta("Braco", url)
    movimenta("Braco", url)
    can.tirar_foto()
    
    movimenta("Base-e", url)
    movimenta("Braco", url)
    movimenta("Base-e", url)
    
# Função para enviar dados para a URL de movimentação
def movimenta(data, url):
    url = str(url) + '/movimenta'
    response = requests.post(url, data=data)
    return response.json()

# Função para enviar um os passos de solução do cubo para a URL de envio
# def enviar(data, url):
#     url = str(url) + '/enviar'
#     response = requests.post(url, data=str(data))
#     return response.json()

def traduz(dates):
    # mapeando funções
    func = {
        "X":giraCuboEixoX,
        "Y":giraCuboEixoY,
        "Z":giraCuboEixoZ,
        "L":movimentaFace,
        "B":movimentaFaceTras,
        "F":movimentaFaceFrente,
        "R":movimentaFaceDireita,
        "U":movimentaFaceSuperior,
        "D":movimentaFaceInferior,
        "M":movimentaMeridiano,
        "E":movimentaEquador,
        "S":movimentaMeridianoY,
    }
    
    movs = []
    for date in dates:
        direcao = 'Horario'
        
        if "i" in date:
            date = date[0]
            direcao = 'Antihorario'
        movs += func[date](direcao)
    return movs

def filtra(lista):
    filtrar_novamente = False
    
    i = 0
    while i < len(lista)-4:
        if lista[i:i+4] == [lista[i]] * 4:
            lista[i:i+4] = []
            i -= 1
            filtrar_novamente = True
        i += 1
    
    i = 0
    while i < len(lista)-1:
        if ('i' in lista[i]) != ('i' in lista[i+1]) and lista[i].replace('i', '') == lista[i+1].replace('i', ''):
            lista[i:i+2] = []
            i -= 1
            filtrar_novamente = True
        i += 1
    
    if filtrar_novamente:
        return filtra(lista)
    
    return lista
        
# Exemplos de uso
if __name__ == "__main__":
    # URL do servidor no EV3
    config = configparser.RawConfigParser()
    config.read("configuration/config_core.ini")

    ev3_server_url = config['CONFIGURATION']['host_EV3']  # Substitua pelo IP correto do seu EV3
    can = camera()
    # can.video()
    # Inicia camera
    # cube_video = threading.Thread(target=can.video)
    # cube_video.start()
    # sleep(2)
    
    # # Scaneia as faces
    # scam_cubo(ev3_server_url, can)
    
    # can.free()
    
    # Ajusta tamanho das imagens
    ajustaIMG(rotate=config.getboolean('CONFIGURATION','rotate'),delete=config.getboolean('CONFIGURATION','apagar_image'))
    
    recortarall(debug=config.getboolean('CONFIGURATION','debug_recort'))
    
    try:
        # Busca cores           
        c = Cube(getCorCubo())
        print(c)
        
        if config.getboolean('CONFIGURATION','apagar_image'):
            shutil.rmtree("fotos/adjusted")
            shutil.rmtree("fotos/recortados")
        
        # Gera solução
        solver = Solver(c)
        solver.solve()

        movs = solver.moves
        
        
        traducao = traduz(solver.moves)
        antes = len(traducao)
        filt = filtra(traducao)
        print(f"filtrados - {antes - len(filt)}")
        
        print(filt)
        # print(filt)
        
        # for mov in solver.moves:
        #     print(mov)
        #     response = enviar(mov, ev3_server_url)
            # input()
        # c.Zi()
        # print(c)
        # response = enviar("E", ev3_server_url)
        
    except:
        print("problema na identificação de cores")
        
