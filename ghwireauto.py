import os, sys, subprocess
import pyautogui 
from datetime import date
import time
from email.message import EmailMessage
import ssl
import smtplib
from os.path import basename
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart 
from email.mime.application import MIMEApplication
import os

print("\nHello, welcome to wireshark automator!")
user_time = input("\nHow long should the program capture packets? (In minutes): ")
user_file = date.today()

filename = (r"/Applications/Wireshark.app")

opener = "open" if sys.platform == "darwin" else "xdg-open"
subprocess.call([opener, filename]) 

time.sleep(2.5)

pyautogui.moveTo(250, 665)

pyautogui.click(button='left')
pyautogui.click(button='left')

#Wireshark is running for duration of user input

time.sleep((int(user_time) * 60))

pyautogui.moveTo(57, 60)
pyautogui.click(button='left')

pyautogui.moveTo(150, 10)
pyautogui.click(button='left')

pyautogui.moveTo(180, 160)
pyautogui.click(button='left')
time.sleep(.25)
pyautogui.write(str(user_file) + " Report")
pyautogui.press('enter')

from_addr = "example@gmail.com"
email_password = "password"
to_addr = "example@gmail.com"
subject = 'Wireshark Report for ' + str(user_file) 
content = "Here is your Wireshark report: "

msg = MIMEMultipart()
msg['From'] = from_addr
msg['To'] = to_addr
msg['Subject'] = subject
body = MIMEText(content, 'plain')
msg.attach(body)

filename = str(user_file) + ' Report.pcapng'

with open(filename, 'rb') as f:
    attachment = MIMEApplication(f.read(), Name=basename(filename))
    attachment['Content-Disposition'] = 'attachment; filename="{}"'.format(basename(filename))

msg.attach(attachment)

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(from_addr, email_password)
    smtp.sendmail(from_addr, to_addr, msg.as_string())

print("Report sent to email!")
