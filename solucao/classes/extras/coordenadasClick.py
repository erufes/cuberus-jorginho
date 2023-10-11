import cv2

# Função para exibir as coordenadas e a faixa de cores no clique
def click_event(event, x, y, flags, params):
   if event == cv2.EVENT_LBUTTONDOWN:
      coordinates = f'({x},{y})'
      print(coordinates, end=" cor - ")

      # Obtenha os valores BGR do pixel clicado
      bgr_color = img[y, x]
      print(bgr_color)

      # Defina os limites 'lower' e 'upper' com base no valor BGR do pixel clicado
      lower = [max(0, c - 10) for c in bgr_color]
      upper = [min(255, c + 10) for c in bgr_color]

      print("Lower:", lower)
      print("Upper:", upper)

      cv2.putText(img, coordinates, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
      cv2.circle(img, (x, y), 3, (0, 255, 255), -1)

# Leia a imagem de entrada
img = cv2.imread("../../fotos/adjusted/face2.png")

# Crie uma janela
cv2.namedWindow('Point Coordinates')

# Associe a função de retorno de chamada à janela
cv2.setMouseCallback('Point Coordinates', click_event)

# Exiba a imagem
while True:
   cv2.imshow('Point Coordinates', img)
   k = cv2.waitKey(1) & 0xFF
   if k == 27:
      break

cv2.destroyAllWindows()