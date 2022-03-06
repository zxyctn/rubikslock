import cv2
import numpy as np

def nothing(x):
    pass

# Load image
image = cv2.imread('imgs/1.jpg')
image2 = cv2.imread('imgs/2.jpg')
image3 = cv2.imread('imgs/3.jpg')
image4 = cv2.imread('imgs/4.jpg')
image5 = cv2.imread('imgs/5.jpg')
image6 = cv2.imread('imgs/6.jpg')

scale_percent = 10# percent of original size
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
    rgb1 = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    mask1 = cv2.inRange(rgb1, lower, upper)
    result1 = cv2.bitwise_and(image, image, mask=mask1)

    rgb2 = cv2.cvtColor(image2, cv2.COLOR_BGR2HSV)
    mask2 = cv2.inRange(rgb2, lower, upper)
    result2 = cv2.bitwise_and(image2, image2, mask=mask2)

    rgb3 = cv2.cvtColor(image3, cv2.COLOR_BGR2HSV)
    mask3 = cv2.inRange(rgb3, lower, upper)
    result3 = cv2.bitwise_and(image3, image3, mask=mask3)

    rgb4 = cv2.cvtColor(image4, cv2.COLOR_BGR2HSV)
    mask4 = cv2.inRange(rgb4, lower, upper)
    result4 = cv2.bitwise_and(image4, image4, mask=mask4)

    rgb5 = cv2.cvtColor(image5, cv2.COLOR_BGR2HSV)
    mask5 = cv2.inRange(rgb5, lower, upper)
    result5 = cv2.bitwise_and(image5, image5, mask=mask5)

    rgb6 = cv2.cvtColor(image6, cv2.COLOR_BGR2HSV)
    mask6 = cv2.inRange(rgb6, lower, upper)
    result6 = cv2.bitwise_and(image6, image6, mask=mask6)

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

    result = np.concatenate(
        (
            result1,
            result2,
            result3,
            result4,
            result5,
            result6
        ), axis=1
    )

    cv2.imshow('image', result)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()