# first of all dont call this one with any library that will screw everything up 


import cv2

img = cv2.imread("../DATA/00-puppy.jpg")

while True:
    cv2.imshow("puppy", img)
    
    #if we've waited atleast 1ms and we've pressed an escape key
    if cv2.waitKey(1) & 0xFF == 27:
        break
        
cv2.destroyAllWindows()