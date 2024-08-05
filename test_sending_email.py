import cv2
import numpy as np
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText

def capture_image():
    # Capture image using OpenCV
    #try:
    cap = cv2.VideoCapture(0)
    cap.set(480, 640)
    #cap.set(4, 480)

    ret, frame = cap.read()
    cv2.imwrite('frame.jpg', frame)
    # Display the frame
    #cv2.imshow("frame", frame)

    image_path = "frame.jpg" #"/home/amd1/Pictures/Webcam/test_img.jpg"
    return image_path
    if not ret:
        print("Failed to capture frame.")

    #except Exception as e:
        #print(f"An error has occured check your web camera connection: {e}")

# Function to send an email with the captured image as an attachment
def send_email(image_path):
    # Email configuration
    sender_email = "robert.lyttle32@gmail.com"
    receiver_email = "robert.lyttle32@hotmail.com" # "lyttle_79_hotmail.com"
    password = "ivrj quas dbil jyfs"  #          "July25@2022"

    # Create a multipart message
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = "Face Capture"

    # Add the image as an attachment
    with open(image_path, "rb") as f:
        image_data = f.read()
        image_type = "jpeg"  # Assuming the image is in JPEG format
        image_name = f.name

    image_attachment = MIMEImage(image_data, image_type)
    image_attachment.add_header("Content-Disposition", "attachment", filename=image_name)
    message.attach(image_attachment)

    # Send the email
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender_email, password)
        server.send_message(message)
        print("Email sent successfully!")

# Capture the image
image_path = capture_image()

# Send the email with the captured image
send_email(image_path)
