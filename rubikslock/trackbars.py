import cv2
import numpy as np

def nothing(x):
    pass

def no_black(img):
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    no_black_low = np.array([0, 0, 144])
    no_black_low = np.array([0, 20, 170])
    no_black_up = np.array([179, 255, 255])
    no_black_mask = cv2.inRange(img_hsv, no_black_low, no_black_up)
    no_black = cv2.bitwise_and(img, img, mask=no_black_mask)

    # img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # no_black_low = np.array([0, 0, 0])
    # no_black_up = np.array([30, 30, 30])
    # no_black_mask = cv2.inRange(img_rgb, no_black_low, no_black_up)
    # no_black = cv2.bitwise_and(img, img, mask=no_black_mask)

    no_black_and = no_black & img

    return no_black_and

# Load image
image = cv2.imread('../rubikslockweb/media/solved_f.jpeg')
image2 = cv2.imread('../rubikslockweb/media/solved_r.jpeg')
image3 = cv2.imread('../rubikslockweb/media/solved_b.jpeg')
image4 = cv2.imread('../rubikslockweb/media/solved_l.jpeg')
image5 = cv2.imread('../rubikslockweb/media/solved_t.jpeg')
image6 = cv2.imread('../rubikslockweb/media/solved_d.jpeg')

image7 = cv2.imread('../rubikslockweb/media/reference_f.jpeg')
image8 = cv2.imread('../rubikslockweb/media/reference_r.jpeg')
image9 = cv2.imread('../rubikslockweb/media/reference_b.jpeg')
image10 = cv2.imread('../rubikslockweb/media/reference_l.jpeg')
image11 = cv2.imread('../rubikslockweb/media/reference_t.jpeg')
image12 = cv2.imread('../rubikslockweb/media/reference_d.jpeg')

scale_percent = 12# percent of original size
width = int(image.shape[1] * scale_percent / 100)
height = int(image.shape[0] * scale_percent / 100)
dim = (width, height)
  
# resize image
image = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
image2 = cv2.resize(image2, dim, interpolation = cv2.INTER_AREA)
image3 = cv2.resize(image3, dim, interpolation = cv2.INTER_AREA)
image4 = cv2.resize(image4, dim, interpolation = cv2.INTER_AREA)
image5 = cv2.resize(image5, dim, interpolation = cv2.INTER_AREA)
image6 = cv2.resize(image6, dim, interpolation = cv2.INTER_AREA)

image7 = cv2.resize(image7, dim, interpolation = cv2.INTER_AREA)
image8 = cv2.resize(image8, dim, interpolation = cv2.INTER_AREA)
image9 = cv2.resize(image9, dim, interpolation = cv2.INTER_AREA)
image10 = cv2.resize(image10, dim, interpolation = cv2.INTER_AREA)
image11 = cv2.resize(image11, dim, interpolation = cv2.INTER_AREA)
image12 = cv2.resize(image12, dim, interpolation = cv2.INTER_AREA)

# Create a window
cv2.namedWindow('image')

# Create trackbars for color change
# Hue is from 0-179 for Opencv
cv2.createTrackbar('RMin', 'image', 0, 255, nothing)
cv2.createTrackbar('GMin', 'image', 0, 255, nothing)
cv2.createTrackbar('BMin', 'image', 0, 255, nothing)
cv2.createTrackbar('RMax', 'image', 0, 255, nothing)
cv2.createTrackbar('GMax', 'image', 0, 255, nothing)
cv2.createTrackbar('BMax', 'image', 0, 255, nothing)

# Set default value for Max HSV trackbars
cv2.setTrackbarPos('RMax', 'image', 255)
cv2.setTrackbarPos('GMax', 'image', 255)
cv2.setTrackbarPos('BMax', 'image', 255)

# Initialize HSV min/max values
hMin = sMin = vMin = hMax = sMax = vMax = 0
prMin = pgMin = pbMin = prMax = pgMax = pbMax = 0

while(1):
    # Get current positions of all trackbars
    rMin = cv2.getTrackbarPos('RMin', 'image')
    gMin = cv2.getTrackbarPos('GMin', 'image')
    bMin = cv2.getTrackbarPos('BMin', 'image')
    rMax = cv2.getTrackbarPos('RMax', 'image')
    gMax = cv2.getTrackbarPos('GMax', 'image')
    bMax = cv2.getTrackbarPos('BMax', 'image')

    # Set minimum and maximum HSV values to display
    lower = np.array([rMin, gMin, bMin])
    upper = np.array([rMax, gMax, bMax])

    # Convert to HSV format and color threshold
    rgb1 = cv2.cvtColor(no_black(image), cv2.COLOR_BGR2HSV)
    mask1 = cv2.inRange(rgb1, lower, upper)
    result1 = cv2.bitwise_and(no_black(image), no_black(image), mask=mask1)

    rgb2 = cv2.cvtColor(no_black(image2), cv2.COLOR_BGR2HSV)
    mask2 = cv2.inRange(rgb2, lower, upper)
    result2 = cv2.bitwise_and(no_black(image2), no_black(image2), mask=mask2)

    rgb3 = cv2.cvtColor(no_black(image3), cv2.COLOR_BGR2HSV)
    mask3 = cv2.inRange(rgb3, lower, upper)
    result3 = cv2.bitwise_and(no_black(image3), no_black(image3), mask=mask3)

    rgb4 = cv2.cvtColor(no_black(image4), cv2.COLOR_BGR2HSV)
    mask4 = cv2.inRange(rgb4, lower, upper)
    result4 = cv2.bitwise_and(no_black(image4), no_black(image4), mask=mask4)

    rgb5 = cv2.cvtColor(no_black(image5), cv2.COLOR_BGR2HSV)
    mask5 = cv2.inRange(rgb5, lower, upper)
    result5 = cv2.bitwise_and(no_black(image5), no_black(image5), mask=mask5)

    rgb6 = cv2.cvtColor(no_black(image6), cv2.COLOR_BGR2HSV)
    mask6 = cv2.inRange(rgb6, lower, upper)
    result6 = cv2.bitwise_and(no_black(image6), no_black(image6), mask=mask6)

    rgb7 = cv2.cvtColor(no_black(image7), cv2.COLOR_BGR2HSV)
    mask7 = cv2.inRange(rgb7, lower, upper)
    result7 = cv2.bitwise_and(no_black(image7), no_black(image7), mask=mask7)

    rgb8 = cv2.cvtColor(no_black(image8), cv2.COLOR_BGR2HSV)
    mask8 = cv2.inRange(rgb8, lower, upper)
    result8 = cv2.bitwise_and(no_black(image8), no_black(image8), mask=mask8)

    rgb9 = cv2.cvtColor(no_black(image9), cv2.COLOR_BGR2HSV)
    mask9 = cv2.inRange(rgb9, lower, upper)
    result9 = cv2.bitwise_and(no_black(image9), no_black(image9), mask=mask9)

    rgb10 = cv2.cvtColor(no_black(image10), cv2.COLOR_BGR2HSV)
    mask10 = cv2.inRange(rgb10, lower, upper)
    result10 = cv2.bitwise_and(no_black(image10), no_black(image10), mask=mask10)

    rgb11 = cv2.cvtColor(no_black(image11), cv2.COLOR_BGR2HSV)
    mask11 = cv2.inRange(rgb11, lower, upper)
    result11 = cv2.bitwise_and(no_black(image11), no_black(image11), mask=mask11)

    rgb12 = cv2.cvtColor(no_black(image12), cv2.COLOR_BGR2HSV)
    mask12 = cv2.inRange(rgb12, lower, upper)
    result12 = cv2.bitwise_and(no_black(image12), no_black(image12), mask=mask12)

    # Print if there is a change in HSV value
    if((prMin != rMin) | (pgMin != gMin) | (pbMin != bMin) | (prMax != rMax) | (pgMax != gMax) | (pbMax != bMax) ):
        print("(rMin = %d , gMin = %d, bMin = %d), (rMax = %d , gMax = %d, bMax = %d)" % (rMin , gMin , bMin, rMax, gMax , bMax))
        prMin = rMin
        pgMin = gMin
        pbMin = bMin
        prMax = rMax
        pgMax = gMax
        pbMax = bMax

    # Display result image

    result_row1 = np.concatenate(
        (
            result1,
            result2,
            result3,
            result4,
            result5,
            result6
        ), axis=1
    )

    result_row2 = np.concatenate(
        (
            result7,
            result8,
            result9,
            result10,
            result11,
            result12
        ), axis=1
    )

    result = np.concatenate(
        (
            result_row1,
            result_row2
        ), axis=0
    )

    cv2.imshow('image', result)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()