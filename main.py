from bs4 import BeautifulSoup
import urllib
import webbrowser

r = urllib.urlopen('http://www.cs.rpi.edu/~zaki/www-new/pmwiki.php/IntroAlgorithms/Main').read()
soup = BeautifulSoup(r, "html.parser")
links = soup.findAll('a')

# Dictionary to hold and quickly access all homeworks and labs
homeworks = {}
labs = {}

for url in links:
    url = str(url)
    if "HW" in url:
        # Cleans out the HTML to clearly access links and homework numbers
        hwLink = url.split('<a class="wikilink" href="',1)[1]
        hwNum = hwLink.split('">',1)[1].split("</a>")[0]
        hwLink = hwLink.split('">')[0]
        homeworks[hwNum] = hwLink
    if "Lab" in url:
        labLink = url.split('<a class="wikilink" href="', 1)[1]
        labNum = labLink.split('">', 1)[1].split("</a>")[0]
        labLink = labLink.split('">', 1)[0]
        labs[labNum] = labLink

print homeworks
print
webbrowser.open(labs['Lab6'])
