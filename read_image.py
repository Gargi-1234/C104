import cv2
import numpy as np

image = cv2.imread("poster.jpg")
rocket = image[120:280,400:500]
image[30:190,480:580] = rocket

text_to_show = "I love Coding"

# black = np.zeros([600,600])
# black[200:400,200:400]=255
#cv2.imshow("image", image)
# print(black)


cv2.imshow("image", image)
cv2.putText(image,text_to_show,(20,220),fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale=1,color=(0,0,255))
cv2.imwrite("Greetings",image)
cv2.waitKey(0)
