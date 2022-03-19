import cv2
import numpy as np

def get_components(img):
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    no_black_low = np.array([0, 0, 144])
    no_black_up = np.array([180, 255, 255])
    no_black_mask = cv2.inRange(img_hsv, no_black_low, no_black_up)
    no_black = cv2.bitwise_and(img, img, mask=no_black_mask)

    # img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # no_black_low = np.array([0, 0, 0])
    # no_black_up = np.array([30, 30, 30])
    # no_black_mask = cv2.inRange(img_rgb, no_black_low, no_black_up)
    # no_black = cv2.bitwise_and(img, img, mask=no_black_mask)

    no_black_and = no_black & img

    no_black_gray = cv2.cvtColor(no_black_and, cv2.COLOR_BGR2GRAY)
    ret, no_black_binary = cv2.threshold(no_black_gray, 0, 255, cv2.THRESH_BINARY)

    kernel = np.ones((15, 15),np.uint8)
    opening = cv2.morphologyEx(no_black_binary, cv2.MORPH_OPEN, kernel)

    # cv2.imshow("No black", opening)
    # cv2.waitKey(0)   

    return cv2.connectedComponentsWithStats(opening, 8, cv2.CV_32S)

def get_masks_hsv(img):
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    white_low = np.array([0, 0, 90])
    white_up = np.array([179, 130, 255])
    white_mask = cv2.inRange(img_hsv, white_low, white_up)
    white = cv2.bitwise_and(img, img, mask=white_mask)

    yellow_low = np.array([0, 50, 200])
    yellow_up = np.array([179, 200, 255])
    yellow_mask = cv2.inRange(img_hsv, yellow_low, yellow_up)
    yellow = cv2.bitwise_and(img, img, mask=yellow_mask)

    orange_low = np.array([0, 50, 225])
    orange_up = np.array([25, 255, 255])
    orange_mask = cv2.inRange(img_hsv, orange_low, orange_up)
    orange = cv2.bitwise_and(img, img, mask=orange_mask)

    red_low_1 = np.array([0, 230, 0])
    red_up_1 = np.array([10, 255, 255])
    red_mask_1 = cv2.inRange(img_hsv, red_low_1, red_up_1)

    red_low_2 = np.array([160, 100, 20])
    red_up_2 = np.array([179, 255, 255])
    red_mask_2 = cv2.inRange(img_hsv, red_low_2, red_up_2)

    red_mask = red_mask_1 | red_mask_2

    red = cv2.bitwise_and(img, img, mask=red_mask)

    blue_low = np.array([75, 100, 100])
    blue_up = np.array([179, 255, 255])
    blue_mask = cv2.inRange(img_hsv, blue_low, blue_up)
    blue = cv2.bitwise_and(img, img, mask=blue_mask)

    green_low = np.array([40, 100, 100])
    green_up = np.array([100, 255, 255])
    green_mask = cv2.inRange(img_hsv, green_low, green_up)
    green = cv2.bitwise_and(img, img, mask=green_mask)

    kernel = np.ones((15, 15),np.uint8)

    yellow_opening = cv2.morphologyEx(yellow_mask, cv2.MORPH_OPEN, kernel)
    red_opening = cv2.morphologyEx(red_mask, cv2.MORPH_OPEN, kernel)
    green_opening = cv2.morphologyEx(green_mask, cv2.MORPH_OPEN, kernel)
    blue_opening = cv2.morphologyEx(blue_mask, cv2.MORPH_OPEN, kernel)
    white_opening = cv2.morphologyEx(white_mask, cv2.MORPH_OPEN, kernel)
    orange_opening = cv2.morphologyEx(orange_mask, cv2.MORPH_OPEN, kernel)

    cv2.imshow("Red", red_mask)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return [
        yellow_opening,
        red_opening,
        green_opening,
        blue_opening,
        white_opening,
        orange_opening 
    ]

def get_masks_rgb(img):
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    white_low = np.array([172, 159, 141])
    white_up = np.array([223, 211, 212])
    white_mask = cv2.inRange(img_rgb, white_low, white_up)
    white = cv2.bitwise_and(img_rgb, img, mask=white_mask)

    yellow_low = np.array([201, 140, 0])
    yellow_up = np.array([255, 255, 87])
    yellow_mask = cv2.inRange(img_rgb, yellow_low, yellow_up)
    yellow = cv2.bitwise_and(img_rgb, img, mask=yellow_mask)

    orange_low = np.array([220, 71, 2])
    orange_up = np.array([255, 150, 40])
    orange_mask = cv2.inRange(img_rgb, orange_low, orange_up)
    orange = cv2.bitwise_and(img_rgb, img, mask=orange_mask)

    red_low_1 = np.array([167, 0, 0])
    red_up_1 = np.array([242, 85, 56])
    red_mask_1 = cv2.inRange(img_rgb, red_low_1, red_up_1)

    # red_low_2 = np.array([190, 0, 0])
    # red_up_2 = np.array([255, 65, 235])
    # red_mask_2 = cv2.inRange(img_rgb, red_low_2, red_up_2)

    # red_low_3 = np.array([179, 0, 0])
    # red_up_3 = np.array([255, 170, 100])
    # red_mask_3 = cv2.inRange(img_rgb, red_low_3, red_up_3
    # red_mask = red_mask_1 + red_mask_2 + red_mask_3

    red = cv2.bitwise_and(img_rgb, img, mask=red_mask_1)

    blue_low = np.array([0, 0, 127])
    blue_up = np.array([55, 255, 255])
    blue_mask = cv2.inRange(img_rgb, blue_low, blue_up)
    blue = cv2.bitwise_and(img_rgb, img, mask=blue_mask)

    green_low = np.array([0, 175, 0])
    green_up = np.array([88, 255, 255])
    green_mask = cv2.inRange(img_rgb, green_low, green_up)
    green = cv2.bitwise_and(img_rgb, img, mask=green_mask)

    kernel = np.ones((15, 15),np.uint8)

    yellow_opening = cv2.morphologyEx(yellow_mask, cv2.MORPH_OPEN, kernel)
    red_opening = cv2.morphologyEx(red_mask_1, cv2.MORPH_OPEN, kernel)
    green_opening = cv2.morphologyEx(green_mask, cv2.MORPH_OPEN, kernel)
    blue_opening = cv2.morphologyEx(blue_mask, cv2.MORPH_OPEN, kernel)
    white_opening = cv2.morphologyEx(white_mask, cv2.MORPH_OPEN, kernel)
    orange_opening = cv2.morphologyEx(orange_mask, cv2.MORPH_OPEN, kernel)

    # cv2.imshow("Red", red_opening)

    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    return [
        # red_mask_1,
        yellow_opening,
        red_opening,
        green_opening,
        blue_opening,
        white_opening,
        orange_opening 
    ]

def get_mapped_face(img, cells):
    (yellow_opening, red_opening, green_opening, blue_opening, white_opening, orange_opening) = get_masks_rgb(img)

    cube = []

    colors = [
        ["White", white_opening],
        ["Red", red_opening],
        ["Yellow", yellow_opening],
        ["Orange", orange_opening],
        ["Blue", blue_opening],
        ["Green", green_opening],
    ]

    # for (x, y) in colors:
    #     cv2.imshow(x, y)
    #     cv2.waitKey(0)
    #     cv2.destroyAllWindows()

    # cv2.imshow("White", white_opening)
    # cv2.imshow("Yellow", yellow_opening)
    # cv2.imshow("Red", red_opening)
    # cv2.imshow("Green", green_opening)
    # cv2.imshow("Blue", blue_opening)
    # cv2.imshow("Orange", orange_opening)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    for cell in cells:
        if yellow_opening[cell.cY][cell.cX]:
            cube.append('y')
        elif orange_opening[cell.cY][cell.cX]:
            cube.append('o')
        elif red_opening[cell.cY][cell.cX]:
            cube.append('r')
        elif blue_opening[cell.cY][cell.cX]:
            cube.append('b')
        elif green_opening[cell.cY][cell.cX]:
            cube.append('g')
        elif white_opening[cell.cY][cell.cX]:
            cube.append('w')
        
        # image = cv2.circle(img, (cell.cX, cell.cY), radius=10, color = (0, 0, 255), thickness=-1)
        # cv2.imshow("Red Opening", image)
        # cv2.waitKey(0)
    
    return cube


# img = cv2.imread("imgs/5.jpg")
# scale_percent = 20# percent of original size
# width = int(img.shape[1] * scale_percent / 100)
# height = int(img.shape[0] * scale_percent / 100)
# dim = (width, height)

# # resize image
# img = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)

# (yellow_opening, red_opening, green_opening, blue_opening, white_opening, orange_opening) = get_masks_rgb(img)

# cv2.imshow("REDMEASK", red_mask_1)
# cv2.imshow("White", white_opening)
# cv2.imshow("Yellow", yellow_opening)
# cv2.imshow("Red", red_opening)
# cv2.imshow("Green", green_opening)
# cv2.imshow("Blue", blue_opening)
# cv2.imshow("Orange", orange_opening)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# img = cv2.imread("imgs/5.jpg")

# scale_percent = 20# percent of original size
# width = int(img.shape[1] * scale_percent / 100)
# height = int(img.shape[0] * scale_percent / 100)
# dim = (width, height)

# # resize image
# img = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)

# get_components(img)