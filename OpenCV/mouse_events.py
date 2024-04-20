import numpy as np
import cv2 
from screeninfo import get_monitors

primary_monitor = get_monitors()[0]
width = primary_monitor.width * 0.9
height = primary_monitor.height * 0.9

image_path = r"C:\Users\Krishanu\Proton Drive\quasarx.dev.krishanu\My files\my_love.png"
a = cv2.imread(image_path, 1)
a = cv2.resize(a, (int(width), int(height)))

def clickEvent(event, x, y, flags, param):
    img = a.copy()  # Make a copy of the original image
    if event == cv2.EVENT_LBUTTONDOWN:
        print(f"{x},{y}")
        font = cv2.FONT_HERSHEY_COMPLEX
        cv2.putText(img, f"{x},{y}", (x,y), font, 1, (255,255,0), 2)
        cv2.imshow("image", img)

    if event == cv2.EVENT_RBUTTONDOWN:
        blue = img[y, x, 0]
        green = img[y, x, 1]
        red = img[y, x, 2]
        print(f"{blue},{green},{red}")
        font = cv2.FONT_HERSHEY_COMPLEX
        cv2.putText(img, f"{blue},{green},{red}", (x,y), font, 0.5, (0,0,255), 1)
        cv2.imshow("image", img)
        
bb = a.copy()
cv2.imshow("image", bb)
cv2.setMouseCallback("image", clickEvent)
cv2.waitKey(0)
cv2.destroyAllWindows()
