from urllib.request import urlopen
from urllib.request import urlretrieve
html = urlretrieve('index.html')
print(html.read())