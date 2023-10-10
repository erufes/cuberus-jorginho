# import the necessary packages
import numpy as np														#codigo que identifica as cores do cubo
import argparse
import cv2

# load the image
image = cv2.imread("face3.png")

# define the list of boundaries
boundaries = [
	([0, 173, 192], [90, 220, 242]),      #amarelo
	([0, 153, 0], [110, 255, 102]),        #verde
	([0, 102, 230], [102, 178, 255]),      #laranja
	([20, 14, 180], [90, 80, 240]),        #vermelho
	([165, 170, 170], [210, 225, 220]),    #branco
	([86, 31, 4], [220, 155, 70]),         #azul 
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
