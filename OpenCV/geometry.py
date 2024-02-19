import cv2

img = cv2.imread(r"data/lena.jpg", 1)
img = cv2.line(img, (0,0), (255,255), (35,200,35), 10)
img = cv2.arrowedLine(img, (255,0), (0,255), (35,200,35), 10)
# img = cv2.line(img, initial point, final point, color, thickness)

img = cv2.rectangle(img, (50,50), (255,255), (0,0,0), 10)
img = cv2.rectangle(img, (270,270), (300,300), (0,0,0), -1) # filled rectangle
img = cv2.circle(img, (370,270), 10, (0,0,0), 2)
img = cv2.circle(img, (470,270), 10, (0,0,0), -1) # filled circle


font = cv2.FACE_RECOGNIZER_SF_FR_COSINE

img = cv2.putText(img, "PutText", (200,200), font, 2, (255,0,0), 10, cv2.LINE_AA)

cv2.imshow("image", img)

while True:
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break

cv2.destroyAllWindows()