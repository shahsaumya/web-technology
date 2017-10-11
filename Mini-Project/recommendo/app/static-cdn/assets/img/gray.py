from numpy import *
import cv2
mazeImg = cv2.imread('film.jpg')
grayImg = cv2.cvtColor(mazeImg, cv2.COLOR_BGR2GRAY)
cv2.imwrite( "film.jpg", grayImg );
cv2.imshow("final",grayImg)
cv2.waitKey(0)
cv2.destroyAllWindows()
