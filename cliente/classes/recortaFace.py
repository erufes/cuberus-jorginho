import numpy as np
import cv2
import os

output_dir = "fotos/recortados"  # Diretório de saída para as faces do cubo

# Crie o diretório de saída, se não existir
os.makedirs(output_dir, exist_ok=True)

# Define as cores e seus limites em HSV
colors = {
	"blue": ([144, 32, 0], [255, 142, 12]),        	#azul
 
	"orange": ([17, 72, 245], [111, 164, 255]),     #laranja
	"yellow": ([59, 157, 201], [169, 237, 255]),   #amarelo
	"red": ([7, 8, 176], [63, 60, 255]),          #vermelho
 
	"white": ([175, 140, 144], [255, 255, 255]),    #branco
	"green": ([38, 103, 0], [202, 255, 155]),      #verde
}

# Função para identificar e destacar as cores na imagem
def identify_colors(image):
    identified_rectangles = []

    for color, (lower, upper) in colors.items():
        lower = np.array(lower, dtype="uint8")
        upper = np.array(upper, dtype="uint8")

        mask = cv2.inRange(image, lower, upper)
        contours = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
        
        for contour in contours:
            approx = cv2.approxPolyDP(contour, 0, False)
            x, y, w, h = cv2.boundingRect(approx)
            if w > 50 and h > 50 :
                if x > 0 and y > 0:
                    if x+w <= image.shape[1]-2 and y+h <= image.shape[0]-45:
                        identified_rectangles.append((x, y, w+x, h+y))
                        
                        # print(x, y, w+x, h+y)
                        # cv2.rectangle(image, (x, y), (w+x, h+y), (0, 255, 0), 2)
                        # cv2.imshow("Todos retangulos", image)
                        # cv2.waitKey(0)
                        # cv2.destroyAllWindows()
    return identified_rectangles

# Função para filtrar retângulos com base na distância
def filter_rectangles(rectangles, distance_threshold=10):
    filtered_rectangles = []
    
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

def recortarall(debug = False):
    # Redimensione todas as imagens para a mesma largura e altura
    margin = 0  # Margem em pixels
    distance_threshold = 10  # Limite de distância para filtrar retângulos

    for num in range(1, 7):
        # Carregue a imagem
        image = cv2.imread("fotos/adjusted/face" + str(num) + ".png")


        # Clone a imagem original
        original_image = image.copy()

        # Identifique as cores e destaque na imagem
        rectangles = identify_colors(image)
        
        rect = original_image.copy()
        for (x, y, w, h) in rectangles:
            # Desenhe um único retângulo que engloba todos os retângulos identificados
            cv2.rectangle(rect, (x, y), (w, h), (0, 255, 0), 2)

        # Filtrar retângulos com base na distância média
        filtered_rectangles = filter_rectangles(rectangles, distance_threshold)
        
        rect2 = original_image.copy()
        for (x, y, w, h) in filtered_rectangles:
            # Desenhe um único retângulo que engloba todos os retângulos identificados
            cv2.rectangle(rect2, (x, y), (w, h), (0, 255, 0), 2)

        # Encontre o menor x, o maior x, o menor y e o maior y dos retângulos filtrados
        x = min(filtered_rectangles, key=lambda x: x[0])[0]
        y = min(filtered_rectangles, key=lambda y: y[1])[1]
        w = max(filtered_rectangles, key=lambda w: w[2])[2]
        h = max(filtered_rectangles, key=lambda h: h[3])[3]

        # Desenhe um único retângulo que engloba todos os retângulos identificados
        cv2.rectangle(image, (x, y), (w, h), (0, 255, 0), 2)

        # Corte a imagem com base nas coordenadas do retângulo com margem
        cropped_image = original_image[y:h, x:w]

        altura, largura = 375, 217
        if debug:
            cima    = np.hstack([cv2.resize(rect, (altura, largura)), cv2.resize(rect2, (altura, largura))])
            baixo   = np.hstack([cv2.resize(image, (altura, largura)), cv2.resize(cropped_image, (altura, largura))])
            
            # Exiba a imagem resultante
            cv2.imshow("Todos retangulos", np.vstack([cima,baixo]))
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        
        # Salve a face do cubo com o mesmo tamanho
        cv2.imwrite(os.path.join(output_dir, f"face{num}.png"), cropped_image)