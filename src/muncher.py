import requests
from bs4 import BeautifulSoup


class Muncher:

    def __init__(self, url, attr):
        self.url = url
        self.attr = attr

    def getContent(self):
        content = requests.get(self.url)
        content = content.text
        return content

    def find(self, content, tag,  class_name):
        soup = BeautifulSoup(content, "html.parser")
        stew = soup.find(tag, {"class": class_name})
        return stew.text
