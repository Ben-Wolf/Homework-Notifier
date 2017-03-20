from bs4 import BeautifulSoup
import holder
import urllib

class Csci2600():
    r = urllib.urlopen('http://www.cs.rpi.edu/~thompw4/CSCI-2600/Spring2017/Homework.html').read()
    soup = BeautifulSoup(r, "html.parser")
    # Gets all links on CSCI2600 page.
    links = soup.findAll('a')
    # Cache file
    cache = "assets/CSCI2600.txt"

    # Dictionary to hold and quickly access all homeworks
    homeworks = {}

    #<a href="Homework/hw0.pdf" target="_blank">hw0</a> :: need to add http://www.cs.rpi.edu/~thompw4/CSCI-2600/Spring2017/
    def __init__(self):
        for url in self.links:
            url = str(url)
            if "hw" in url:
                # Cleans out the HTML to clearly access links and homework numbers
                temp = url.split('<a href="',1)[1].split('" target="_blank">')
                hwLink = "http://www.cs.rpi.edu/~thompw4/CSCI-2600/Spring2017/" + temp[0]
                hwNum = temp[1].split("</a>")[0].split("<br/>")[0]
                self.homeworks[hwNum] = hwLink

    def addData(self):
        cache = open(self.cache, 'w')
        for key in self.homeworks:
            cache.write("%s : %s\n" %(key, self.homeworks[key]))
        cache.write("\n")

        return "Updated cache..."

    def checkData(self):
        oldData = []
        missing = {}
        x = False
        cache = open(self.cache, 'r')
        for line in cache:
            line = line.split(" : ")[0]
            oldData.append(line)

        for key in self.homeworks:
            if key not in oldData:
                x = True
                missing[key] = self.homeworks[key]

        return missing
