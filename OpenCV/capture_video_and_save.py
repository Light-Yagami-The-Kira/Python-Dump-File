import cv2

# Initialize the VideoCapture object to capture video from the default camera (i.e., webcam)
cap = cv2.VideoCapture(0)

# Get the default frame size
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Define the codec and create the VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output_video.avi', fourcc, 20.0, (frame_width, frame_height))

while True:
    # Read a frame from the camera
    ret, frame = cap.read()

    # Check if the frame was successfully read
    if ret:
        # Flip the frame horizontally for a more natural view
        frame = cv2.flip(frame, 1)

        # Write the frame to the output video file
        out.write(frame)

        # Display the frame in a window
        cv2.imshow('Webcam Feed', frame)

        # Exit the loop if the user presses the 'q' key
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release the VideoCapture and VideoWriter objects and close all windows
cap.release()
out.release()
cv2.destroyAllWindows()