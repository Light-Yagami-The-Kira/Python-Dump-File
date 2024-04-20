import cv2
# img = cv2.imread(r"data/lena.jpg", 0)
img = cv2.imread(r"data/lena.jpg", )
print(img)
## IF IMAGE DOES NOT EXIST, THEN THE PRINT WILL GIVE NONE

cv2.imshow("image", img)

# cv2.waitKey(5000) 5000 MILISECONDS = 5 SECONDS
k = cv2.waitKey(0)
if k == 27:
    cv2.destroyAllWindows()
else:
    print(f"I pressed {k}.")

cv2.destroyAllWindows()

cv2.imwrite("CopyOUput.jpg", img)