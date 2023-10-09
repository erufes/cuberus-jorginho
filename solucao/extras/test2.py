import numpy as np
import argparse
import cv2

# Argumentos da linha de comando
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--C:/Users/Arthur/Desktop/cuberus-jorginho-T2/cuberus-jorginho-T2/identificaCor/face2_t.png", help = "path to the image")
args = vars(ap.parse_args())

# Carregue a imagem
image = cv2.imread("face2_t.png")

# Define as cores e seus limites em HSV
colors = {
    "yellow": ([20, 100, 100], [30, 255, 255]),
    "green": ([35, 100, 100], [85, 255, 255]),
    "orange": ([0, 100, 100], [20, 255, 255]),
    "red": ([0, 100, 100], [10, 255, 255]),
    "white": ([0, 0, 200], [180, 30, 255]),
    "blue": ([100, 100, 100], [140, 255, 255]),
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
            if w > 50 and h > 50:  # Filtre retângulos pequenos
                identified_rectangles.append((x, y, w, h))

    return identified_rectangles

# Identifique as cores e destaque na imagem
rectangles = identify_colors(image)

# Encontre o menor x, o maior x, o menor y e o maior y
min_x = min(rectangles, key=lambda x: x[0])[0]
max_x = max(rectangles, key=lambda x: x[0] + x[2])[0] + max(rectangles, key=lambda x: x[0] + x[2])[2]
min_y = min(rectangles, key=lambda x: x[1])[1]
max_y = max(rectangles, key=lambda x: x[1] + x[3])[1] + max(rectangles, key=lambda x: x[1] + x[3])[3]

# Desenhe um único retângulo que engloba todos os retângulos identificados
cv2.rectangle(image, (min_x, min_y), (max_x, max_y), (0, 255, 0), 2)

# Exiba a imagem resultante
cv2.imshow("Identified Colors", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
