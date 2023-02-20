import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

"""
        disclaimer!!!!!!!! 
        developer: vurudi  
this project is entirely functional  make sure to go through the READme file on the 
repository to successfully set up your environment and run this script 
uses python 2.7 and later versions
"""

SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587


class EmailAutomation:

    def send_email(sender, recipient):
        """ Send email message """
        msg = MIMEMultipart()
        msg['Subject'] = 'Email from vurudi100 emailautomation project'
        msg['To'] = recipient
        msg['From'] = sender

        # areading the message stored in message.txt into the project
        with open('message.txt', 'r') as f:
            messege = f.read()
        msg.attach(MIMEText(messege, 'plain'))
        # attach image files
        filename = 'vurudi100.jpg'  # can replace with your desire file 
        attachment = open(filename, 'rb')
        p = MIMEBase('application', 'octet-stream')
        p.set_payload(attachment.read())
        encoders.encode_base64(p)  # we have to encode
        p.add_header('Content-Disposition', f'attachment; filename={filename}')

        # we have to add the image as an attachment to the message
        msg.attach(p)

        # treat the whole message as a string
        text = msg.as_string()

        # create smtp session
        session = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        session.ehlo()
        session.starttls()
        session.ehlo()
        with open('emailpassword.txt', 'r') as f:
            password = f.read()
        session.login(sender, password)
        session.sendmail(sender, recipient, text)
        print("Email sent successfully check you inbox or spam folder")
        session.quit()
