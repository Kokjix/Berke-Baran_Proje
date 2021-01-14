import cv2
import numpy as np

def color_detect(frame):
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    low_red = np.array([161, 155, 84])
    high_red = np.array([179, 255, 255])
    red_mask = cv2.inRange(hsv_frame, low_red, high_red)
    red = cv2.bitwise_and(frame, frame, mask=red_mask)
    red_count = np.count_nonzero(red)/red.size
    # Blue color
    low_blue = np.array([230, 100, 55])
    high_blue = np.array([237, 100, 100])
    blue_mask = cv2.inRange(hsv_frame, low_blue, high_blue)
    blue = cv2.bitwise_and(frame, frame, mask=blue_mask)
    blue_count = np.count_nonzero(blue) / blue.size
    # Green color
    low_green = np.array([110, 90, 57])
    high_green = np.array([113, 100, 100])
    green_mask = cv2.inRange(hsv_frame, low_green, high_green)
    green = cv2.bitwise_and(frame, frame, mask=green_mask)
    green_count = np.count_nonzero(green) / green.size
    """
    # Every color except white
    low = np.array([0, 42, 0])
    high = np.array([179, 255, 255])
    other_mask = cv2.inRange(hsv_frame, low, high)
    result = cv2.bitwise_and(frame, frame, mask=other_mask)
    """
    #white color
    lower_white = np.array([0,0,93], dtype=np.uint8)
    upper_white = np.array([359,2,100], dtype=np.uint8)

    # Threshold the HSV image to get only white colors
    white_mask = cv2.inRange(hsv_frame, lower_white, upper_white)
    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame,frame, mask= white_mask)
    white_count = np.count_nonzero(res) / res.size

    color_counts = {'red': red_count, 'blue': blue_count, 'green': green_count, 'white': white_count}

    color_is = max(color_counts, key = color_counts.get)

    print("car color is", color_is)
    color_is = " "

    #cv2.imshow('frame',frame)
    #cv2.imshow('mask',mask)
    cv2.imshow('White',res)
    #cv2.imshow("Frame", frame)
    cv2.imshow("Red", red)
    cv2.imshow("Blue", blue)
    cv2.imshow("Green", green)
    #cv2.imshow("Result", result)