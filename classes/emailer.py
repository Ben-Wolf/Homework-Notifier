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
    msg['Subject'] = "Homework Notification"
    classes = []
    csci2300 = {}
    csci2600 = {}
    body = ""
    # msg['Subject'] = "Homework Notification: CSCI 2300"

    def __init__(self, email, classes, csci2300, csci2600, test):
        if (self.fromaddr == ""):
            print "ERROR: Holder info not set."
            print "Please put the email you plan to send updates from and the password in holder.py"
            sys.exit()

        self.toaddr = email
        self.msg['to'] = email
        self.classes = classes

        if (len(csci2300) > 0 and len(csci2600) > 0 and not test):
            self.body += "Hi, here are your assignment updates."

        if (test):
            self.msg['Subject'] = "Homework Notifier: Test"
            self.body = "This is a test, if you don't know why you're seeing this, neither do I."

        if (len(csci2300) > 0 and '2300' in classes and not test):
            self.body += "\n\nThere are %d new assignments in Intro to Algorithms:\n\n" %len(csci2300)
            for key in csci2300:
                self.body += "%s : %s\n" %(key, csci2300[key])

        if (len(csci2600) > 0 and '2600' in classes and not test):
            self.body += "\n\nThere are %d new assignments in Principles of Software:\n\n" %len(csci2600)
            for key in csci2600:
                self.body += "%s : %s\n" %(key, csci2600[key])

        self.msg.attach(MIMEText(self.body, 'plain'))


    def sendEmail(self):
        # print "Sending: "
        # print self.body
        # print "to %s" %self.toaddr

        # Server code to send email
        if self.body == "":
            return None
            
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(self.fromaddr, self.password)
        text = self.msg.as_string()
        server.sendmail(self.fromaddr, self.toaddr, text)
        server.quit()
