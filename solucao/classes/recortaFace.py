import numpy as np
import cv2
import os

output_dir = "fotos/recortados"  # Diretório de saída para as faces do cubo

# Crie o diretório de saída, se não existir
os.makedirs(output_dir, exist_ok=True)

# Define as cores e seus limites em HSV
colors = {
    "yellow": ([0, 173, 192], [195, 248, 255]),
    "green": ([0, 103, 0], [198, 255, 113]),
    "orange": ([0, 60, 230], [160, 178, 255]),
    "red": ([20, 9, 180], [115, 80, 255]),
    "white": ([165, 170, 170], [210, 225, 220]),
    "blue": ([86, 31, 0], [255, 155, 70]),
}

# Função para identificar e destacar as cores na imagem
def identify_colors(image):
    hsv_img = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    identified_rectangles = []

    for color, (lower, upper) in colors.items():
        lower = np.array(lower, dtype="uint8")
        upper = np.array(upper, dtype="uint8")

        mask = cv2.inRange(hsv_img, lower, upper)

        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        for contour in contours:
            x, y, w, h = cv2.boundingRect(contour)
            if w > 50 and h > 50 and 0 <= x <= image.shape[1] and 0 <= y <= image.shape[0]:
                identified_rectangles.append((x, y, w, h))

    return identified_rectangles

# Função para filtrar retângulos com base na distância média
def filter_rectangles(rectangles, distance_threshold):
    # Calcule a média das coordenadas x e y dos retângulos identificados
    mean_x = sum(x for (x, _, _, _) in rectangles) / len(rectangles)
    mean_y = sum(y for (_, y, _, _) in rectangles) / len(rectangles)

    # Filtrar retângulos com base na distância média
    filtered_rectangles = [
        rect
        for rect in rectangles
        if ((rect[0] - mean_x) ** 2 + (rect[1] - mean_y) ** 2) ** 0.5 < distance_threshold
    ]

    return filtered_rectangles

def recortarall(debug = False):
    # Redimensione todas as imagens para a mesma largura e altura
    target_width = 400
    target_height = 500
    margin = 2  # Margem em pixels
    distance_threshold = 180  # Limite de distância para filtrar retângulos

    for num in range(1, 7):
        # Carregue a imagem
        image = cv2.imread("fotos/adjusted/face" + str(num) + ".png")

        # Redimensione a imagem para o tamanho alvo
        image = cv2.resize(image, (target_width, target_height))

        # Clone a imagem original
        original_image = image.copy()

        # Identifique as cores e destaque na imagem
        rectangles = identify_colors(image)

        # Filtrar retângulos com base na distância média
        filtered_rectangles = filter_rectangles(rectangles, distance_threshold)

        # Encontre o menor x, o maior x, o menor y e o maior y dos retângulos filtrados
        min_x = min(filtered_rectangles, key=lambda x: x[0])[0] - margin
        aux = max(filtered_rectangles, key=lambda x: x[0] + x[2])
        max_x = aux[0] +aux[2] + margin
        
        min_y = min(filtered_rectangles, key=lambda x: x[1])[1] - margin
        aux = max(filtered_rectangles, key=lambda x: x[1] + x[3])
        max_y = aux[1] + aux[3] + margin

        # Desenhe um único retângulo que engloba todos os retângulos identificados
        cv2.rectangle(image, (min_x, min_y), (max_x, max_y), (0, 255, 0), 2)

        # Corte a imagem com base nas coordenadas do retângulo com margem
        cropped_image = original_image[min_y:max_y, min_x:max_x]

        if debug:
            # Exiba a imagem resultante
            cv2.imshow("Identified Colors", image)
            cv2.imshow("Cropped Image", cropped_image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        
        # Salve a face do cubo com o mesmo tamanho
        cv2.imwrite(os.path.join(output_dir, f"face{num}.png"), cropped_image)
