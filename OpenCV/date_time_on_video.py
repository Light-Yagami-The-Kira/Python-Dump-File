import datetime
import cv2

font = cv2.FONT_HERSHEY_SIMPLEX

cap = cv2.VideoCapture(0)
while cap.isOpened():
    ret, frame = cap.read()
    if ret == True:

        date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        frame = cv2.putText(frame, date, (5,30), font, 1, (255,0,0), 1, cv2.LINE_AA )

        cv2.imshow("Your Video", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    else:
        break

cap.release()
cv2.destroyAllWindows()