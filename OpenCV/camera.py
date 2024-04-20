import cv2

# cap = cv2.VideoCapture(1)
# cap = cv2.VideoCapture("Path/to/video")
cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output_video.mp4', fourcc, 30.0, (cv2.CAP_PROP_FRAME_WIDTH, cv2.CAP_PROP_FRAME_HEIGHT))

print(
    cap.get(cv2.CAP_PROP_FRAME_WIDTH),
    cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    )
while cap.isOpened():
    return_value,frame = cap.read()
    if return_value == True:
        out.write(frame)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow("Window Title", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
else:
    print("There is no Camera Avaialble")

cap.release()
out.release()
cv2.destroyAllWindows()