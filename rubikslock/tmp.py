import cv2
import numpy as np

# function to display the coordinates of
# of the points clicked on the image
def click_event(event, x, y, flags, params):
 
    # checking for left mouse clicks
    if event == cv2.EVENT_LBUTTONDOWN:
 
        # displaying the coordinates
        # on the Shell
        print(x, ' ', y)
 
        # displaying the coordinates
        # on the image window
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(frame, str(x) + ',' +
                    str(y), (x,y), font,
                    1, (255, 0, 0), 2)
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        print(hsv[x][y])
 
    # checking for right mouse clicks    
    if event==cv2.EVENT_RBUTTONDOWN:
 
        # displaying the coordinates
        # on the Shell
        print(x, ' ', y)
 
        # displaying the coordinates
        # on the image window
        font = cv2.FONT_HERSHEY_SIMPLEX
        b = frame[y, x, 0]
        g = frame[y, x, 1]
        r = frame[y, x, 2]
        cv2.putText(frame, str(b) + ',' +
                    str(g) + ',' + str(r),
                    (x,y), font, 1,
                    (255, 255, 0), 2)
        # cv2.imshow('Input', frame)

cap = cv2.VideoCapture(0)

# Check if the webcam is opened correctly
if not cap.isOpened():
    raise IOError("Cannot open webcam")

def nothing(x):
    pass

cv2.namedWindow('Edges')
cv2.createTrackbar('min', 'Edges', 0, 255, nothing)
cv2.createTrackbar('max', 'Edges', 0, 255, nothing)

while True:
    ret, frame = cap.read()
    # frame = cv2.resize(frame, [2560, 1440], fx=1, fy=1, interpolation=cv2.INTER_AREA)
    
    frame_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # green_low = np.array([65, 90, 85])
    # green_up = np.array([80, 255, 255])
    # green_mask = cv2.inRange(frame_hsv, green_low, green_up)
    # green = cv2.bitwise_and(frame, frame, mask=green_mask)

    yellow_low = np.array([25, 0, 0])
    yellow_up = np.array([43, 255, 255])
    yellow_mask = cv2.inRange(frame_hsv, yellow_low, yellow_up)
    yellow = cv2.bitwise_and(frame, frame, mask=yellow_mask)

    orange_low = np.array([6, 47, 75])
    orange_up = np.array([25, 255, 255])
    orange_mask = cv2.inRange(frame_hsv, orange_low, orange_up)
    orange = cv2.bitwise_and(frame, frame, mask=orange_mask)

    green_low = np.array([55, 68, 155])
    green_up = np.array([78, 255, 255])
    green_mask = cv2.inRange(frame_hsv, green_low, green_up)
    green = cv2.bitwise_and(frame, frame, mask=green_mask)

    # cv2.imshow('Input', green)
    

    lab= cv2.cvtColor(frame, cv2.COLOR_BGR2LAB)
    # cv2.imshow("lab",lab)

    #-----Splitting the LAB image to different channels-------------------------
    l, a, b = cv2.split(lab)
    # cv2.imshow('l_channel', l)
    # cv2.imshow('a_channel', a)
    # cv2.imshow('b_channel', b)

    #-----Applying CLAHE to L-channel-------------------------------------------
    clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8,8))
    cl = clahe.apply(l)

    #-----Merge the CLAHE enhanced L-channel with the a and b channel-----------
    limg = cv2.merge((cl,a,b))

    #-----Converting image from LAB Color model to RGB model--------------------
    final = cv2.cvtColor(limg, cv2.COLOR_LAB2BGR)

    
    minn = cv2.getTrackbarPos('min', 'Edges')
    maxx = cv2.getTrackbarPos('max', 'Edges')
    
    gray = cv2.cvtColor(final, cv2.COLOR_BGR2GRAY)
    normal = cv2.equalizeHist(gray)
    edges = cv2.Canny(frame,minn,maxx)

    ret, thresh = cv2.threshold(gray, 190, 255, cv2.THRESH_BINARY_INV)
    # if (type(minn) != None and type(maxx) != None):
    #     ret, thresh = cv2.threshold(gray, minn, maxx, cv2.THRESH_BINARY_INV)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
    hierarchy = hierarchy[0]

    for i, c in enumerate(contours):
        if hierarchy[i][2] < 0 and hierarchy[i][3] < 0:
            cv2.drawContours(frame, contours, i, (0, 0, 255), 2)
        else:
            cv2.drawContours(frame, contours, i, (0, 255, 0), 2)
    #write to the same directory
    cv2.imshow("result.png", green)
    # edges_green = cv2.Canny(green,1,255)
    # edges_yellow = cv2.Canny(yellow,50,90)
    # edges_orange = cv2.Canny(orange,20,90)
    # edges_all = edges_green + edges_yellow + edges_orange

    # cv2.imshow("Edges", edges)
    cv2.setMouseCallback('Edges', click_event)
    
    c = cv2.waitKey(1)
    if c == 27:
        break

cap.release()
cv2.destroyAllWindows()