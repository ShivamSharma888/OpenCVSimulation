import cv2
import streamlit as st

# Load the pre-trained vehicle detector (Haar Cascade)
cascade_path = r'C:\Users\Shivam\AppData\Roaming\JetBrains\PyCharmCE2024.1\scratches\haarcascade_cars.xml'
vehicle_cascade = cv2.CascadeClassifier(cascade_path)

if vehicle_cascade.empty():
    st.error("Error: Haar Cascade file not loaded.")
    st.stop()

# Traffic density thresholds
low_density_threshold = 5
medium_density_threshold = 15

# Function to process frames
def process_frame(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    vehicles = vehicle_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3, minSize=(50, 50))

    num_vehicles = len(vehicles)

    # Determine traffic density
    if num_vehicles > medium_density_threshold:
        traffic_density = 'High'
        color = (0, 0, 255)  # Red
    elif num_vehicles > low_density_threshold:
        traffic_density = 'Medium'
        color = (0, 255, 255)  # Yellow
    else:
        traffic_density = 'Low'
        color = (0, 255, 0)  # Green

    # Draw rectangles around detected vehicles
    for (x, y, w, h) in vehicles:
        cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)

    # Display traffic density status on the frame
    cv2.putText(frame, f'Traffic Density: {traffic_density}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2, cv2.LINE_AA)
    cv2.putText(frame, f'Vehicles Count: {num_vehicles}', (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2, cv2.LINE_AA)

    return frame

# Streamlit app
def main():
    st.title("Real-Time Traffic Density Detection System")

    # Capture video from file or camera
    video_source = st.text_input("Enter video file path or camera URL:", "http://192.168.43.1:4747/video")

    cap = cv2.VideoCapture(video_source)

    if not cap.isOpened():
        st.error(f"Error: Could not open video source: {video_source}")
        st.stop()

    stframe = st.empty()

    while True:
        ret, frame = cap.read()
        if not ret:
            st.write("End of video or frame not read.")
            break

        # Process the frame
        processed_frame = process_frame(frame)

        # Convert the frame to RGB
        processed_frame_rgb = cv2.cvtColor(processed_frame, cv2.COLOR_BGR2RGB)

        # Display the frame
        stframe.image(processed_frame_rgb, channels="RGB")

    # Release the video capture object
    cap.release()

if __name__ == "__main__":
    main()
