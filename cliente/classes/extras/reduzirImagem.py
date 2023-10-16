import cv2 as cv


# importing Image class from PIL package 
from PIL import Image

for num in range(1,7):

    # creating a object 
    image = Image.open(r"face"+str(num)+".png")


    MAX_SIZE = (500, 500)
    image.thumbnail(MAX_SIZE)
    
    
    image_rotated = image.rotate(-90, expand=True)

    # creating thumbnail
    image_rotated.save("face"+str(num)+".png")

    img = cv.imread("face"+str(num)+".png")

    # cv.imshow("Display window", img)
    # k = cv.waitKey(0) # Wait for a keystroke in the window
