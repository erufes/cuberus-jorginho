# import the necessary packages
import numpy as np														#codigo que identifica as cores do cubo
import argparse
import cv2
# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--C:/Users/Arthur/Desktop/cuberus-jorginho-T2/cuberus-jorginho-T2/identificaCor/face1_t.png", help = "path to the image")
args = vars(ap.parse_args())
# load the image
image = cv2.imread("face1_t.png")

# define the list of boundaries
boundaries = [
	([50, 180, 210], [90, 210, 240]),      #amarelo
	([0, 153, 0], [110, 255, 102]),        #verde
	([0, 102, 230], [102, 178, 255]),      #laranja
	([30, 30, 200], [90, 80, 230]),        #vermelho
	([180, 180, 204], [255, 255, 255]),    #branco
	([86, 31, 4], [220, 135, 70]),         #azul 
]


# loop over the boundaries 
for (lower, upper) in boundaries:
	# create NumPy arrays from the boundaries
	lower = np.array(lower, dtype = "uint8")
	upper = np.array(upper, dtype = "uint8")
	# find the colors within the specified boundaries and apply
	# the mask
	mask = cv2.inRange(image, lower, upper)
	output = cv2.bitwise_and(image, image, mask = mask)
	# show the images
	cv2.imshow("images", np.hstack([image, output]))
	cv2.waitKey(0)
