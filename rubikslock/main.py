import cv2
import numpy as np

from color_extraction import get_face
import turns

# cube = {
#     'f': None,
#     'r': None,
#     'b': None,
#     'l': None,
#     't': None,
#     'd': None,
# }

def get_cube(f, r, b, l, t, d):
    img_f = cv2.imread(f)
    img_r = cv2.imread(r)
    img_b = cv2.imread(b)
    img_l = cv2.imread(l)
    img_t = cv2.imread(t)
    img_d = cv2.imread(d)

    cube['f'] = np.reshape(get_face(img_f), (3,3))
    cube['r'] = np.reshape(get_face(img_r), (3,3))
    cube['b'] = np.reshape(get_face(img_b), (3,3))
    cube['l'] = np.reshape(get_face(img_l), (3,3))
    cube['t'] = np.reshape(get_face(img_t), (3,3))
    cube['d'] = np.reshape(get_face(img_d), (3,3))

    return cube

# img_f = cv2.imread("imgs/1.jpg")
# img_r = cv2.imread("imgs/2.jpg")
# img_b = cv2.imread("imgs/3.jpg")
# img_l = cv2.imread("imgs/4.jpg")
# img_t = cv2.imread("imgs/5.jpg")
# img_d = cv2.imread("imgs/6.jpg")


# cube['f'] = np.reshape(get_face(img_f), (3,3))
# cube['r'] = np.reshape(get_face(img_r), (3,3))
# cube['b'] = np.reshape(get_face(img_b), (3,3))
# cube['l'] = np.reshape(get_face(img_l), (3,3))
# cube['t'] = np.reshape(get_face(img_t), (3,3))
# cube['d'] = np.reshape(get_face(img_d), (3,3))

# print(cube)

# for key in cube:
#     print(key + ": ")
#     for i in range(3):
#         print(cube[key][i*3] + " " + cube[key][i*3+1] + " " + cube[key][i*3+2])
