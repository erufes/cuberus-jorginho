# import the necessary packages
import argparse
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="/home/dianamellorosi/Documentos/cucu (1)-20230913T175854Z-001/cucu (1)/pythonthumb.png",
	help="path to the input image")
args = vars(ap.parse_args())

# load the image, grab its spatial dimensions (width and height),
# and then display the original image to our screen
image = cv2.imread(args["image"])
(h, w) = image.shape[:2]
cv2.imshow("Original", image)

cor = image[169, 50]
# images are simply NumPy arrays -- with the origin (0, 0) located at
# the top-left of the image
(b, g, r) = image[169, 50]                                                      #coordenada 0,0
print("Pixel at (50, 169) - Red: {}, Green: {}, Blue: {}".format(r, g, b))

(b, g, r) = image[219, 51]                                                     #coordenada 0,1
print("Pixel at (51, 219) - Red: {}, Green: {}, Blue: {}".format(r, g, b))

(b, g, r) = image[280, 47]                                                     #coordenada 0,2
print("Pixel at (47, 280) - Red: {}, Green: {}, Blue: {}".format(r, g, b))

(b, g, r) = image[165, 111]                                                     #coordenada 1,0
print("Pixel at (111, 165) - Red: {}, Green: {}, Blue: {}".format(r, g, b))

(b, g, r) = image[217, 112]                                                      #coordenada 1,1
print("Pixel at (47, 280) CENTRO - Red: {}, Green: {}, Blue: {}".format(r, g, b))

(b, g, r) = image[280, 116]                                                     #coordenada 1,2
print("Pixel at (116, 280) - Red: {}, Green: {}, Blue: {}".format(r, g, b))

(b, g, r) = image[165, 171]                                                     #coordenada 2,0
print("Pixel at (171, 165) - Red: {}, Green: {}, Blue: {}".format(r, g, b))

(b, g, r) = image[216, 178]                                                     #coordenada 2,1
print("Pixel at (178, 216) - Red: {}, Green: {}, Blue: {}".format(r, g, b))

(b, g, r) = image[275, 182]                                                     #coordenada 2,2
print("Pixel at (182, 275) - Red: {}, Green: {}, Blue: {}".format(r, g, b))