import cv2
import numpy as np
import matplotlib.pyplot as plt

# img = np.zeros((500, 500), np.uint8) + 50
# cv2.rectangle(img, (0, 60), (200, 150), (255,255,255), -1)
# cv2.rectangle(img, (250, 170), (350, 200), (255,255,255), -1)

# cv2.imshow("img", img)

# plt.hist(img.ravel(), 256, [0, 256])
# plt.show()


img = cv2.imread("smile.jpg")
b, g, r = cv2.split(img)
cv2.imshow("img", img)

plt.hist(b.ravel(), 256, [0, 256], color='b')
plt.hist(g.ravel(), 256, [0, 256], color='g')
plt.hist(r.ravel(), 256, [0, 256], color='r')
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()