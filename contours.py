import cv2
import numpy as np

src = cv2.imread('first.jpg', cv2.IMREAD_COLOR)

scale_percent = 25# percent of original size
width = int(src.shape[1] * scale_percent / 100)
height = int(src.shape[0] * scale_percent / 100)
dim = (width, height)
  
# resize image
src = cv2.resize(src, dim, interpolation = cv2.INTER_AREA)


#Transform source image to gray if it is not already
if len(src.shape) != 2:
    gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
else:
    gray = src

ret, thresh = cv2.threshold(gray, 190, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
hierarchy = hierarchy[0]



blank = 255 * np.ones(shape=[height, width, 3], dtype=np.uint8)
for i, c in enumerate(contours):
    if hierarchy[i][2] < 0 and hierarchy[i][3] < 0:
        cv2.drawContours(blank, contours, i, (0, 0, 255), 2)
    else:
        cv2.drawContours(blank, contours, i, (0, 255, 0), 2)
#write to the same directory



cv2.imshow("result.png", blank)
cv2.waitKey(0)
cv2.destroyAllWindows()













# import numpy as np
# import cv2

# img = cv2.imread('first.jpg')
# imgGrey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# _, thrash = cv2.threshold(imgGrey, 200, 255, cv2.THRESH_BINARY)
# contours, _ = cv2.findContours(thrash, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

# cv2.imshow("img", img)
# for contour in contours:
#     approx = cv2.approxPolyDP(contour, 0.01* cv2.arcLength(contour, True), True)
#     cv2.drawContours(img, [approx], 0, (0, 0, 0), 5)
#     x = approx.ravel()[0]
#     y = approx.ravel()[1] - 5
#     if len(approx) == 3:
#         cv2.putText(img, "Triangle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
#     elif len(approx) == 4:
#         x1 ,y1, w, h = cv2.boundingRect(approx)
#         aspectRatio = float(w)/h
#         print(aspectRatio)
#         if aspectRatio >= 0.95 and aspectRatio <= 1.05:
#           cv2.putText(img, "square", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
#         else:
#           cv2.putText(img, "rectangle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
#     elif len(approx) == 5:
#         cv2.putText(img, "Pentagon", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
#     elif len(approx) == 10:
#         cv2.putText(img, "Star", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
#     else:
#         cv2.putText(img, "Circle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))


# cv2.imshow("shapes", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()