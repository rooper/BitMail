import subprocess
import smtplib
import socket
from email.mime.text import MIMEText
import datetime

def sendmail(contents):
    to = 'logan.rooper@gmail.com'
    gmail_user = 'YOUR_USERNAME'
    gmail_password = 'YOUR_PASSWORD'
    smtpserver = smtplib.SMTP('smtp.gmail.com', 587)
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo
    smtpserver.login(gmail_user, gmail_password)
    today = datetime.date.today()

    msg = MIMEText(contents);
    msg['Subject'] = 'Bitcoin Notification from your RPI'
    msg['From'] = gmail_user
    msg['To'] = to
    smtpserver.sendmail(gmail_user, [to], msg.as_string())
    smtpserver.quit()
