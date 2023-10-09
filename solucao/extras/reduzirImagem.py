import cv2 as cv                                                 #esse codigo pega uma imagem em alta resolucao e a diminui, sendo possivel
                                                                 #de visualizar a imagem pelo pop-up do codigo que identifica as cores


# importing Image class from PIL package 
from PIL import Image

# creating a object 
image = Image.open(r"face2.png")


MAX_SIZE = (500, 500)
image.thumbnail(MAX_SIZE)
  
  
image_rotated = image.rotate(-90, expand=True)

# creating thumbnail
image_rotated.save('face2_t.png')

img = cv.imread("face2_t.png")

cv.imshow("Display window", img)
k = cv.waitKey(0) # Wait for a keystroke in the window
