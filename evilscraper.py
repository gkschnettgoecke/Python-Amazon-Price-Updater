import requests
from bs4 import BeautifulSoup
import smtplib
import time

def send_mail(to, s):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('grant.schnettgoecke@gmail.com', 'nvrrtwnrkexpovzg')

    subject = s

    body = 'Hahahaha'

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'grant.schnettgoecke@gmail.com',
        to,
        msg
    )
    print(f"Email has been sent to {to}")

    server.quit()

#evil
subject = ['Assignment 1 Due', 'Exam 1 Next Week', 'Lab Report Due', 'Project 1 Due', 'Quiz On Blackboard', 'Weekly Remainders', 'Due This Week', 'Assignment Update', 'CLASS UPDATE']

for i in range(len(subject)):
    send_mail('gkschnett@ku.edu', subject[i])
    time.sleep(5)


print("End script")