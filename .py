# Pythonproject
#python programming projec
# Import libraries
import cv2
import dlib

# Initialize face detector and shape predictor
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

# Define a function to get facial landmarks from an image
def get_landmarks(image):
    # Convert image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Detect faces in the image
    faces = detector(gray)
    # Loop through each face
    for face in faces:
        # Get the coordinates of the face rectangle
        x1 = face.left()
        y1 = face.top()
        x2 = face.right()
        y2 = face.bottom()
        # Draw a rectangle around the face
        cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
        # Get the facial landmarks
        landmarks = predictor(gray, face)
        # Loop through each landmark
        for n in range(0, 68):
            # Get the coordinates of the landmark
            x = landmarks.part(n).x
            y = landmarks.part(n).y
            # Draw a circle around the landmark
            cv2.circle(image, (x, y), 2, (0, 0, 255), -1)
    # Return the image with landmarks
    return image

# Create a video capture object
cap = cv2.VideoCapture(0)

# Loop until the user presses 'q' key
while True:
    # Read a frame from the camera
    _, frame = cap.read()
    # Get the facial landmarks from the frame
    frame = get_landmarks(frame)
    # Show the frame on the screen
    cv2.imshow("Facial Landmarks", frame)
    # Wait for 1 millisecond
    key = cv2.waitKey(1)
    # If 'q' key is pressed, break the loop
    if key == ord('q'):
        break

# Release the video capture object and close all windows
cap.release()
cv2.destroyAllWindows()
