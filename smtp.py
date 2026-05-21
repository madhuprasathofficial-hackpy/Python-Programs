import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os

def send_email():
    # --- Email Configuration ---
    # It is highly recommended to use environment variables for sensitive data
    # Example: sender_email = os.environ.get("SENDER_EMAIL")
    sender_email = "abcdef@gmail.com"
    app_password = "dmjv ayas gpyg zqww" 
    receiver_email = "123@gmail.com"
    
    # --- Message Content ---
    subject = "Automated Python Email"
    body = " "

    
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject

    # Attach the body of the email to the MIME message
    message.attach(MIMEText(body, ""))

    try:
        # --- Connecting to the Server ---
        # Port 587 is used for TLS (Transport Layer Security)
        print("Connecting to the SMTP server...")
        server = smtplib.SMTP("smtp.gmail.com", 587)
        
        # Start TLS for security
        server.starttls()
        
        # --- Logging in and Sending ---
        print("Logging in...")
        server.login(sender_email, app_password)
        
        print("Sending email...")
        # Convert the multipart message into a string format for the server
        text = message.as_string()
        server.sendmail(sender_email, receiver_email, text)
        
        print("Email sent successfully!")

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Always ensure the server connection is closed
        server.quit()

if __name__ == "__main__":
    send_email()
