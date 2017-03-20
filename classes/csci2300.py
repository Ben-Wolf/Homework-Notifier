from bs4 import BeautifulSoup
import holder
import urllib
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
# import webbrowser

def addData(cache, homeworks, labs):
    cache = open(cache, 'w')
    for key in homeworks:
        cache.write("%s : %s\n" %(key, homeworks[key]))

    cache.write("\n")
    for key in labs:
        cache.write("%s : %s\n" %(key, labs[key]))

def checkData(cache, homeworks, labs):
    oldData = []
    missing = {}
    x = False
    cache = open(cache, 'r')
    for line in cache:
        line = line.split(" : ")[0]
        oldData.append(line)

    for key in homeworks:
        if key not in oldData:
            x = True
            missing[key] = homeworks[key]

    for key in labs:
        if key not in oldData:
            x = True
            missing[key] = labs[key]

    return missing


if __name__ == '__main__':
    r = urllib.urlopen('http://www.cs.rpi.edu/~zaki/www-new/pmwiki.php/IntroAlgorithms/Main').read()
    soup = BeautifulSoup(r, "html.parser")
    # Gets all links on CSCI2600 page.
    links = soup.findAll('a')
    # Cache file
    cache = "cache/cacheCSCI2300.txt"

    # Dictionary to hold and quickly access all homeworks and labs
    homeworks = {}
    labs = {}
    x = holder.Holder()

    for url in links:
        url = str(url)
        if "HW" in url:
            # Cleans out the HTML to clearly access links and homework numbers
            hwLink = url.split('<a class="wikilink" href="',1)[1]
            hwNum = hwLink.split('">',1)[1].split("</a>")[0]
            hwLink = hwLink.split('">')[0]
            homeworks[hwNum] = hwLink
        if "Lab " in url:
            labLink = url.split('<a class="wikilink" href="', 1)[1]
            labNum = labLink.split('">', 1)[1].split("</a>")[0]
            labLink = labLink.split('">', 1)[0]
            labs[labNum] = labLink

    send = checkData(cache, homeworks, labs)
    addData(cache, homeworks, labs)

    fromaddr = x.getEmail()
    toaddr = "notreal"
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Homework Notification: CSCI 2300"

    body = "There are %d new assignments in class: CSCI 2300\n" %len(send)

    for key in send:
        body += "\n%s : %s" %(key, send[key])

    print body
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, x.getPassword())
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()
