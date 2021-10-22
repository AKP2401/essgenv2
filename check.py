import requests
from readability import Document

g = requests.get("https://realpython.com/python-web-scraping-practical-introduction/").text
gg = Document(g)

print(gg.title())
with open("asd.txt", 'w') as f:
    f.write(gg.summary())