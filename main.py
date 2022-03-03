import cv2

from color_extraction import get_face

cube = {
    'f': None,
    'r': None,
    'b': None,
    'l': None,
    't': None,
    'd': None,
}

img_f = cv2.imread("imgs/1.jpg")
img_r = cv2.imread("imgs/2.jpg")
img_b = cv2.imread("imgs/3.jpg")
img_l = cv2.imread("imgs/4.jpg")
img_t = cv2.imread("imgs/5.jpg")
img_d = cv2.imread("imgs/6.jpg")

cube['f'] = get_face(img_f)
cube['r'] = get_face(img_r)
cube['b'] = get_face(img_b)
cube['l'] = get_face(img_l)
cube['t'] = get_face(img_t)
cube['d'] = get_face(img_d)

# print(cube)

for key in cube:
    print(key + ": ")
    for i in range(3):
        print(cube[key][i*3] + " " + cube[key][i*3+1] + " " + cube[key][i*3+2])