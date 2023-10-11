# import the necessary packages
import numpy as np														#codigo que identifica as cores do cubo
import argparse
import cv2

# load the image
image = cv2.imread("../../fotos/face6.png")

# define the list of boundaries
boundaries = [
	("Amarelo", [103, 190, 240], [194, 255, 255]),      #amarelo
	("Verde", [55, 140, 10], [202, 255, 155]),     #verde
	("Laranja", [19, 84, 240], [188, 190, 255]),     #laranja
	("Vermelho", [12, 7, 190], [110, 87, 255]),        #vermelho
	("Branco", [187, 154, 161], [255, 255, 255]),    #branco
	("Azul", [188, 54, 0], [255, 142, 12]),         #azul 
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
