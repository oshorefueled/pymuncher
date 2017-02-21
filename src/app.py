import requests
from bs4 import BeautifulSoup
from muncher import Muncher


muncher = Muncher("http://www.konga.com/canvas-painting-dancing-ladies-2779922", "span")
content = muncher.getContent()

print("price of the product is %s" % (muncher.find(content, "span", "price")))


