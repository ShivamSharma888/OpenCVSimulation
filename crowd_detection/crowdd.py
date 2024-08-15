import streamlit as st
import cv2
import numpy as np

# Load the pre-trained people detector (Haar Cascade)
people_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_fullbody.xml')

if people_cascade.empty():
    st.error("Error: Haar Cascade file not loaded.")
    st.stop()

# Function to process frames
def process_frame(frame):
    # Resize the frame for faster processing
    frame = cv2.resize(frame, (640, 480))

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect people in the frame
    people = people_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3, minSize=(30, 30))

    # Draw rectangles around detected people
    for (x, y, w, h) in people:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Determine crowd density
    num_people = len(people)
    if num_people > medium_density_threshold:
        crowd_status = 'High Density'
    elif num_people > low_density_threshold:
        crowd_status = 'Medium Density'
    else:
        crowd_status = 'Low Density'

    # Display crowd status and people count on the frame
    cv2.putText(frame, f'Crowd Status: {crowd_status}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2, cv2.LINE_AA)
    cv2.putText(frame, f'People Count: {num_people}', (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2, cv2.LINE_AA)

    return frame, num_people

# Streamlit app
def main():
    st.title("Crowd Detection with Streamlit")

    # Capture video from DroidCam
    camera_url = st.text_input("Enter DroidCam URL:", "http://192.168.53.30:4747/video")
    if st.button("Start Camera"):
        cap = cv2.VideoCapture(camera_url, cv2.CAP_FFMPEG)

        if not cap.isOpened():
            st.error(f"Error: Could not open camera feed at {camera_url}.")
            st.stop()

        # Resize factor to reduce processing load
        resize_factor = 0.5
        frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH) * resize_factor)
        frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT) * resize_factor)

        stframe = st.empty()
        total_people_count = 0
        frame_count = 0

        while True:
            ret, frame = cap.read()
            if not ret:
                st.write("End of video or frame not read.")
                break

            # Process the frame
            processed_frame, num_people = process_frame(frame)

            # Update people count and frame count
            total_people_count += num_people
            frame_count += 1

            # Convert the frame to RGB
            processed_frame_rgb = cv2.cvtColor(processed_frame, cv2.COLOR_BGR2RGB)

            # Display the frame
            stframe.image(processed_frame_rgb, channels="RGB")

            # Display running totals
            st.write(f"Total People Detected: {total_people_count}")
            st.write(f"Average People per Frame: {total_people_count / frame_count if frame_count > 0 else 0:.2f}")

        # Release the video capture object
        cap.release()

if __name__ == "__main__":
    low_density_threshold = 5
    medium_density_threshold = 15
    main()
