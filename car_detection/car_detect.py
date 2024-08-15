import cv2

# Capture video from file
cap = cv2.VideoCapture('cars.mp4')

# Load the pre-trained car classifier
car_cascade = cv2.CascadeClassifier('haarcascade_cars.xml')

# Initialize car count
car_count = 0

# Set traffic density thresholds
high_traffic_threshold = 10  # Adjust based on your scenario
low_traffic_threshold = 5  # Adjust based on your scenario

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Break if the video has ended
    if not ret:
        break

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect cars in the frame
    cars = car_cascade.detectMultiScale(gray, 1.1, 3)

    # Draw rectangles around detected cars and count them
    num_cars = len(cars)
    car_count += num_cars

    for (x, y, w, h) in cars:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Determine traffic density
    if num_cars > high_traffic_threshold:
        traffic_status = 'High Traffic'
    elif num_cars < low_traffic_threshold:
        traffic_status = 'Low Traffic'
    else:
        traffic_status = 'Moderate Traffic'

    # Display traffic status on the frame
    cv2.putText(frame, f'Traffic Status: {traffic_status}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2,
                cv2.LINE_AA)

    # Show the frame with detected cars
    cv2.imshow('Video', frame)

    # Exit on 'Q' key press
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

# Release the video capture object and close all frames
cap.release()
cv2.destroyAllWindows()

# Print the total count of detected cars
print(f'Total number of cars detected: {car_count}')
