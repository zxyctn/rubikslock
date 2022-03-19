import cv2
import numpy as np
from pathlib import Path

from controlpanel.color_extraction import get_face
from controlpanel.turns import front, right, back, left, top, down

cube = {
    'f': None,
    'r': None,
    'b': None,
    'l': None,
    't': None,
    'd': None,
}

def solve_cube(solution, cube):
    turned = cube.copy()
    for i in range(len(solution)):
        clockwise = True

        if (solution[i] == '\''):
            continue
        elif (i + 1 < len(solution) and solution[i + 1] == '\''):
            clockwise = False

        if (solution[i] == 'F'):
            turned =  front(turned.copy(), clockwise)
        elif (solution[i] == 'R'):
            turned =  right(turned.copy(), clockwise)
        elif (solution[i] == 'B'):
            turned =  back(turned.copy(), clockwise)
        elif (solution[i] == 'L'):
            turned =  left(turned.copy(), clockwise)
        elif (solution[i] == 'T'):
            turned =  top(turned.copy(), clockwise)
        elif (solution[i] == 'D'):
            turned =  down(turned.copy(), clockwise)
        else:
            print("Wrong input: " + solution[i])
            continue
    
    return turned.copy()



def get_cube(f, r, b, l, t, d):
    # base_path = str(Path(__file__).resolve().parent.parent)
    # base_path = base_path.replace("\\", "/")
    
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

def compare_solutions(solution, solved_cube):
    for key in solution:
        if (str(solution[key]) != str(solved_cube[key])):
            return False
    return True

# img_f = cv2.imread("../../rubikslock/imgs/1.jpg")
# img_r = cv2.imread("../../rubikslock/imgs/2.jpg")
# img_b = cv2.imread("../../rubikslock/imgs/3.jpg")
# img_l = cv2.imread("../../rubikslock/imgs/4.jpg")
# img_t = cv2.imread("../../rubikslock/imgs/5.jpg")
# img_d = cv2.imread("../../rubikslock/imgs/6.jpg")


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
