import cv2

# Open the default camera (usually the built-in webcam, 0 is the default index)
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FPS, 10)


while True:
    # Read a frame from the camera
    ret, frame = cap.read()

    # Display the frame
    cv2.imshow('Webcam', frame)

    # Break the loop if 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close the OpenCV window
cap.release()
cv2.destroyAllWindows()
