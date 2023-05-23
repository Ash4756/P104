import cv2
img = cv2.imread("solar-system.jpg")

t1 = "sun"
t2 = "mercury"
t3 = "venus"
t4 = "earth"
t5 = "mars"
t6 = "jupiter"
t7 = "saturn"
t8 = "uranus"
t9 = "neptune"
cv2.putText(img,t1,(110,100),fontFace = cv2.FONT_HERSHEY_COMPLEX,fontScale = 1,color = (0,0,255))
cv2.putText(img,t2,(110,200),fontFace = cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale = 0.5,color = (0,0,255))
cv2.putText(img,t3,(200,180),fontFace = cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale = 0.5,color = (0,0,255))
cv2.putText(img,t4,(280,180),fontFace = cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale = 0.5,color = (0,0,255))
cv2.putText(img,t5,(400,180),fontFace = cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale = 0.5,color = (0,0,255))
cv2.putText(img,t6,(500,90),fontFace = cv2.FONT_HERSHEY_COMPLEX,fontScale = 0.5,color = (0,0,255))
cv2.putText(img,t7,(800,150),fontFace = cv2.FONT_HERSHEY_COMPLEX,fontScale = 0.5,color = (0,0,255))
cv2.putText(img,t8,(980,150),fontFace = cv2.FONT_HERSHEY_COMPLEX,fontScale = 0.5,color = (0,0,255))
cv2.putText(img,t9,(1100,150),fontFace = cv2.FONT_HERSHEY_COMPLEX,fontScale = 0.5,color = (0,0,255))
cv2.imshow("output",img)
cv2.waitKey(0)