# Scrapper
class wrapper around beautifulsoup4 and requests

### How to use:
1. Initiate Object
    scrapObj = Scrapper("https://www.google.com") 
2. set the root element
    scrapObj.setRootElement("body")
3. Then you can print it, iterate through its children, etc