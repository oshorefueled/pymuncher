from muncher import Muncher
munch = Muncher("http://www.konga.com/canvas-painting-dancing-ladies-2779922", "span")
content = munch.getContent()

print("price of the product is %s" % (munch.find(content, "span", "price")))


