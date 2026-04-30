# roi => region of interest => ilgi alanı
import cv2

img = cv2.imread("klon.jpg")
# print(img.shape[:2])

roi = img[20:200, 200:400]

cv2.imshow("Klon", img)
cv2.imshow("ROI", roi)

cv2.waitKey(0)
cv2.destroyAllWindows()