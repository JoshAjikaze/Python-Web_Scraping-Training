from bs4 import BeautifulSoup
from urllib.request import urlopen

url = "http://olympus.realpython.org/profiles/dionysus"
raw_html =  urlopen(url)
html = raw_html.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")

print(soup.get_text())