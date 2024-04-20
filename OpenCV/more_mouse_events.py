from cv2.typing import Point
import numpy as np
import cv2 
from screeninfo import get_monitors

points = []

primary_monitor = get_monitors()[0]
width = primary_monitor.width * 0.9
height = primary_monitor.height * 0.9

image_path = r"C:\Users\Krishanu\Proton Drive\quasarx.dev.krishanu\My files\my_love.png"
a = cv2.imread(image_path, 1)
a = cv2.resize(a, (int(width), int(height)))

def clickEvent(event, x, y, flags, param):
    img = bb
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x, y), 3, (0,255,255), -1)
        points.append((x, y))
        if len(points) >= 2:
            cv2.line(img, points[-2], points[-1], (0,0,0), 5)
        cv2.imshow("image", img)
    
    ## COLOR PICKER
    if event == cv2.EVENT_RBUTTONDOWN :
        blue = img[x, y, 0]
        green = img[x, y, 1]
        red = img[x, y, 0]
        
        myColorImage = np.zeros((512,512,3), np.uint8)
        myColorImage[:] = [blue, green, red]
        myColorImage = cv2.resize(myColorImage, (500,500))
        cv2.imshow("Color Picker", myColorImage)
        
bb = a.copy()
cv2.imshow("image", bb)
cv2.setMouseCallback("image", clickEvent)
cv2.waitKey(0)
cv2.destroyAllWindows()
