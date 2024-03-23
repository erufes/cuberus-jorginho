# Manipulação de Imagem 
import cv2
from PIL import Image

# Operações do sistema operacional 
import os
from distutils.util import strtobool

# Carrega as variaveis de ambiente
from dotenv import load_dotenv 
load_dotenv()

# Outras Libs
import numpy as np

# Define as cores e seus limites em HSV
colors = {
	"blue": ([144, 32, 0], [255, 207, 11]),        	#azul
	"green": ([60, 173, 36], [202, 255, 155]),      #verde
 
	"orange": ([52, 100, 245], [108, 211, 255]),     #laranja
	"yellow": ([59, 157, 201], [169, 255, 255]),   #amarelo
	"red": ([7, 8, 176], [104, 107, 255]),          #vermelho
 
	"white": ([175, 140, 144], [255, 255, 255]),    #branco
}

# - Função Interna para identificar e destacar as cores na imagem
# Imput : Objeto da imagem a ser lida e id da imagem
# Output : Lista de Retangulos identificados
def identify_colors(image, n):
    identified_rectangles = []
    
    for color, (lower, upper) in colors.items():
        lower = np.array(lower, dtype="uint8")
        upper = np.array(upper, dtype="uint8")
        
        # Cria mascara com a cor selecionada
        mask = cv2.inRange(image, lower, upper)
        
        # Encontra o contorno desejado de acordo com a cor da mascara
        contours = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
        
        for contour in contours:
            approx = cv2.approxPolyDP(contour, 0, False)
            x, y, w, h = cv2.boundingRect(approx)
            if w > 50 and h > 50 :
                if x > 30 and y > 60:
                    if x+w <= image.shape[1]-75 and y+h <= image.shape[0]-45:
                        identified_rectangles.append((x, y, w+x, h+y))
                    
                    if strtobool(os.environ.get("DEBUG", "false")):
                        # print(color, x, y, w+x, h+y)
                        cv2.rectangle(image, (x, y), (w+x, h+y), (0, 255, 0), 2)
                        
                        # Coordenadas para posicionar o texto
                        text_x = x + 5  # Ajuste para posicionar dentro do retângulo
                        text_y = y + 20  # Ajuste para posicionar dentro do retângulo

                        # Largura máxima permitida para o texto dentro do retângulo
                        largura_max = w - 10

                        # Quebra o texto em linhas
                        linhas = []
                        linha_atual = ''
                        for palavra in color:
                            if cv2.getTextSize(linha_atual + ' ' + palavra, cv2.FONT_HERSHEY_SIMPLEX, 0.5, 1)[0][0] <= largura_max:
                                linha_atual += ' ' + palavra if linha_atual else palavra
                            else:
                                linhas.append(linha_atual)
                                linha_atual = palavra
                        if linha_atual:
                            linhas.append(linha_atual)

                        # Adiciona as linhas de texto dentro do retângulo na imagem
                        for i, linha in enumerate(linhas):
                            cv2.putText(image, linha, (text_x, text_y + i*20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
        
        if strtobool(os.environ.get("DEBUG", "false")):
            tam_x   = int(os.environ.get("WIDTH", 0))
            tam_y   = int(os.environ.get("HEIGHT", 0))
            offset  = int(os.environ.get("OFFSET", 100))
            
            # Define a posição da janela (x, y)
            if n <= 3:
                x, y = offset + (tam_x)*(n-1), offset
            else:
                x, y = offset + (tam_x)*(n-4), tam_y + offset
            
            thumbnail  = cv2.resize(image, (tam_x, tam_y))
            cv2.imshow("Identificação: face-0"+str(n), thumbnail)
            cv2.moveWindow("Identificação:  face-0"+str(n), x, y)
                    
    return identified_rectangles

# - Função Interna para filtrar retângulos com base na distância
# Imput : Objeto com a posição dos pontos de todos os retângulos
# Output : Objeto com a posição dos pontos de todos os retângulos dentro da distancia de threshold
def filter_rectangles(rectangles):
    filtered_rectangles = []
    distance_threshold = os.environ.get("ROTATE", 10) # Limite de distância para filtrar retângulos
    
    for (x_min, y_min, w, h) in rectangles:
        x_max = w
        y_max = h
        
        # Variável para rastrear se encontrou outro retângulo próximo
        found_nearby_rectangle = False
        for (x2_min, y2_min, w2, h2) in rectangles:
            if (x_min, y_min) == (x2_min, y2_min):
                continue  # Ignora o próprio retângulo
            
            x2_max = w2
            y2_max = h2
            
            dist_x = min([abs(x_min-x2_max), abs(x_max-x2_min)])
            dist_y = min([abs(y_min-y2_max), abs(y_max-y2_min)])
            
            if (x_min != x2_min):
                dist_x = min([abs(x_min-x2_min), dist_x])
            if (x_max != x2_max):
                dist_x = min([abs(x_max-x2_max), dist_x])
            if (y_min != y2_min):
                dist_y = min([abs(y_min-y2_min), dist_y])
            if (y_max != y2_max):
                dist_y = min([abs(y_max-y2_max), dist_y])
                
                
            if (x_min == x2_min) or (x_max == x2_max):
                if(dist_y <= distance_threshold):
                    found_nearby_rectangle = True
                    break
                continue
            if (y_min == y2_min) or (y_max == y2_max):
                if (dist_x <= distance_threshold):
                    found_nearby_rectangle = True
                    break
                continue
            
            # Inscrito
            if (x2_min <= x_min <= x2_max) and (y2_min <= y_min <= y2_max):
                found_nearby_rectangle = True
                break
            elif (x2_min <= x_max <= x2_max) and (y2_min <= y_max <= y2_max):
                found_nearby_rectangle = True
                break
            if (x2_min >= x_min >= x2_max) and (y2_min >= y_min >= y2_max):
                found_nearby_rectangle = True
                break
            elif (x2_min >= x_max >= x2_max) and (y2_min >= y_max >= y2_max):
                found_nearby_rectangle = True
                break
            
            # Inscreve
            if (x_min <= x2_min <= x_max) and (y_min <= y2_min <= y_max):
                found_nearby_rectangle = True
                break
            elif (x_min <= x2_max <= x_max) and (y_min <= y2_max <= y_max):
                found_nearby_rectangle = True
                break
            elif (x_min >= x2_min >= x_max) and (y_min >= y2_min >= y_max):
                found_nearby_rectangle = True
                break
            elif (x_min >= x2_max >= x_max) and (y_min >= y2_max >= y_max):
                found_nearby_rectangle = True
                break
            
            
            if dist_x <= distance_threshold and dist_y <= distance_threshold:
                found_nearby_rectangle = True
                break
                
        if found_nearby_rectangle:
            filtered_rectangles.append((x_min, y_min, w, h))

    return filtered_rectangles

# - 
# Imput : None
# Output : pasta /fotos/cropped e face recortadas das imagens dos cubos
def cut_all():
    # Redimensione todas as imagens para a mesma largura e altura
    margin              = 0     # Margem em pixels

    for num in range(1, 7):
        # Carregue a imagem
        image = cv2.imread("fotos/adjusted/face" + str(num) + ".png")

        # Clona a imagem original
        original_image = image.copy()

        # Identifique as cores e destaque na imagem em forma de retangulos
        rectangles = identify_colors(image, num)
    
    
        rect = original_image.copy()
        # for (x, y, w, h) in rectangles:
        #     # Desenha os retângulos identificados
        #     cv2.rectangle(rect, (x, y), (w, h), (0, 255, 0), 2)

        # Filtrar retângulos com base na distância média mandendo somente retangulos próximos um dos outros
        # if len(rectangles) == 1:
        #     filtered_rectangles = rectangles
        # else:
        #     filtered_rectangles = filter_rectangles(rectangles)
        
    # Espera comando para fechar todas as janelas
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    #     rect2 = original_image.copy()
    #     for (x, y, w, h) in filtered_rectangles:
    #         # Desenhe um único retângulo que engloba todos os retângulos identificados
    #         cv2.rectangle(rect2, (x, y), (w, h), (0, 255, 0), 2)

    #     # Encontre o menor x, o maior x, o menor y e o maior y dos retângulos filtrados
    #     x = min(filtered_rectangles, key=lambda x: x[0])[0]
    #     y = min(filtered_rectangles, key=lambda y: y[1])[1]
    #     w = max(filtered_rectangles, key=lambda w: w[2])[2]
    #     h = max(filtered_rectangles, key=lambda h: h[3])[3]

    #     # Desenhe um único retângulo que engloba todos os retângulos identificados
    #     cv2.rectangle(image, (x, y), (w, h), (0, 255, 0), 2)

    #     # Corte a imagem com base nas coordenadas do retângulo com margem
    #     cropped_image = original_image[y:h, x:w]

    #     altura, largura = 375, 217
    #     if strtobool(os.environ.get("DELETE_IMAGE", "false")):
    #         cima    = np.hstack([cv2.resize(rect, (altura, largura)), cv2.resize(rect2, (altura, largura))])
    #         baixo   = np.hstack([cv2.resize(image, (altura, largura)), cv2.resize(cropped_image, (altura, largura))])
            
    #         # Exiba a imagem resultante
    #         cv2.imshow("Todos retangulos", np.vstack([cima,baixo]))
    #         cv2.waitKey(0)
    #         cv2.destroyAllWindows()
        
    #     cropped_image_resized = cv2.resize(cropped_image, (300, 200))
    #     # Salve a face do cubo com o mesmo tamanho
    #     cv2.imwrite(os.path.join(output_dir, f"face{num}.png"), cropped_image_resized)
    
    # output_dir = "fotos/cropped"  # Diretório de saída para as faces do cubo
    # # Crie o diretório de saída, se não existir
    # os.makedirs(output_dir, exist_ok=True)
        
# - Pega as imagens da pasta /fotos e ajusta o tamanho para 500x500 de todas as imagens
# Imput : None
# Output : pasta /fotos/adjusted e imagens com thumbnail ajustada
def adjust_IMG():
    for i in range(6):
        arquivo = "face"+str(i+1)+".png"

        # creating a object 
        image = Image.open(r"fotos/"+arquivo)

        MAX_SIZE = (500, 500)
        image.thumbnail(MAX_SIZE)

        image_rotated = image
        if strtobool(os.environ.get("ROTATE", "false")):
            image_rotated = image.rotate(-90, expand=True)

        # Crie o diretório de saída, se não existir
        os.makedirs("fotos/adjusted/", exist_ok=True)

        # creating thumbnail
        image_rotated.save("fotos/adjusted/"+arquivo)
        
        if strtobool(os.environ.get("DELETE_IMAGE", "false")):
            os.remove("fotos/"+arquivo)