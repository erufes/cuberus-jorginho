# import the necessary packages
import numpy as np														#codigo que identifica as cores do cubo
import cv2

# load the image 3
image = cv2.imread("../../fotos/recortados/face4.png")

# define the list of boundaries
boundaries = [
	("Azul",  [144, 32, 0], [255, 207, 11]),        	#azul 
	("Verde", [60, 173, 36], [202, 255, 155]),      #verde
	("Laranja", [52, 100, 245], [108, 211, 255]),    #laranja
	("Amarelo", [59, 157, 201], [169, 255, 255]),  #amarelo
	("Vermelho", [7, 8, 176], [104, 107, 255]),     #vermelho
	("Branco", [175, 140, 144], [255, 255, 255]),   #branco
]

# loop over the boundaries 
for (cor, lower, upper) in boundaries:
	# create NumPy arrays from the boundaries
	lower = np.array(lower, dtype = "uint8")
	upper = np.array(upper, dtype = "uint8")
	# find the colors within the specified boundaries and apply
	# the mask
	mask = cv2.inRange(image, lower, upper)
	output = cv2.bitwise_and(image, image, mask = mask)
	# show the images
	cv2.imshow(cor, np.hstack([image, output]))
	cv2.waitKey(0)
