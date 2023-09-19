import cv2 as cv                                                 #esse codigo pega uma imagem em alta resolucao e a diminui, sendo possivel
                                                                 #de visualizar a imagem pelo pop-up do codigo que identifica as cores


# importing Image class from PIL package 
from PIL import Image
   
# creating a object 
image = Image.open(r"/home/dianamellorosi/Documentos/cucu (1)-20230913T175854Z-001/cucu (1)/WhatsApp Image 2023-09-08 at 17.00.25.jpeg")
MAX_SIZE = (500, 500)
  
image.thumbnail(MAX_SIZE)
  
# creating thumbnail
image.save('face6.png')

img = cv.imread("face6.png")

cv.imshow("Display window", img)
k = cv.waitKey(0) # Wait for a keystroke in the window
