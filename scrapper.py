# static member class python?
from bs4 import BeautifulSoup
import requests

class Scrapper(object):
    # Public member
    url = ""
    requestObj = None
    statusCode = 0
    tag = None

    # Private member
    _webContent = ""
    _soup = None

    def __init__(self, url):
        self.url = url
        self.loadPage()

    def setUrl(self, url):
        self.url = url

    def loadPage(self):
        self.requestObj = requests.get(self.url)
        self.statusCode = self.requestObj.status_code
        self._webContent = self.requestObj.text
        self._soup = BeautifulSoup(self._webContent, "lxml")

    def setRootElement(self, tagName):
        self.rootElement = self._soup.find(tagName)

    def findAll(self, filter):
        self.arrayTag = self.rootElement.find_all(filter)
        return self.arrayTag

    def find(self, tag):
        self.tag = self.rootElement.find(tag)
        return self.tag


if __name__ == "__main__":
    scrap1 = Scrapper("https://www.google.com")

    scrap1.setRootElement("body")
    print(scrap1.find("div"))

