# Import urlopen from request
from urllib.request import urlopen
import re

# define your url
url = "http://olympus.realpython.org/profiles/aphrodite"
url2 = "http://olympus.realpython.org/profiles/poseidon"

# open the webpage by passing it into urlopen
# This returns an HTTPResponse object
page = urlopen(url2)

# Extract the raw html with the read method
raw_html = page.read()

# Decode the raw html 
html = raw_html.decode("utf-8")

# print the decodes html
# print(html)

title_index = html.find("<title>")

start_index = title_index + len("<title>")
end_index = html.find("</title>")
# print(start_index, end_index)

web_page_title = html[start_index:end_index]
print(web_page_title)

print(re.findall("ab*c", "abcd"))
print(re.findall("ab*c", "abbc"))
print(re.findall("ab*c", "ac"))
print(re.findall("ab*c", "adc"))
