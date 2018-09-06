import urllib, requests
from urllib.parse import unquote
from urllib.request import urlopen

html=urlopen("http://www.globalrewriter.com/synpairs/swedish")
print(html.read())
