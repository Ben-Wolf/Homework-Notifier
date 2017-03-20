import csci2300, csci2600, shelve, sys, holder
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

class Emailer():

    account = holder.Holder()
    password = account.password
    fromaddr = account.email
    toaddr = ""
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    classes = []
    csci2300 = {}
    csci2600 = {}
    body = ""
    # msg['Subject'] = "Homework Notification: CSCI 2300"

    def __init__(self, email, classes, csci2300, csci2600):
        self.toaddr = email
        self.msg['to'] = email
        self.classes = classes

        if (len(csci2300) > 0):
            self.body += "There are %d new assignments in Principles of Software:\n" %len(csci2300)

        if (len(csci2600) > 0):
            self.body += "There are %d new assignments in Introduction to Algorithms:\n" %len(csci2600)

    def sendEmail(self):
        print self.body
