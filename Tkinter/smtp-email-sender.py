import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Email configuration
sender_email = "ataullah.behesti@gmail.co"
receiver_email = "ataullah.behesti@ecomond.com"
subject = "Test Email"
message = "This is a test email sent from a Windows Server."

# SMTP server configuration
smtp_server = "smtp.gmail.com"  # Use the SMTP server of your email provider
smtp_port = 587  # Port may vary based on your email provider
smtp_username = "ataullah.behesti@gmail.com"
smtp_password = "thomasbarbey"

# Create the email
msg = MIMEMultipart()
msg["From"] = sender_email
msg["To"] = receiver_email
msg["Subject"] = subject
msg.attach(MIMEText(message, "plain"))

# Send the email
try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(smtp_username, smtp_password)
    server.sendmail(sender_email, receiver_email, msg.as_string())
    server.quit()
    print("Email sent successfully.")
except Exception as e:
    print(f"An error occurred: {str(e)}")
