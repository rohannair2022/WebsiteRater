#Importing the library that deals with the retrieval of info from a url online
from urllib.request import urlopen
#Importing the library that deals with the retrieval of info from a file locally.
from urllib.request import urlretrieve

# Throw an error when there is an issue occured while retrieving the data
from urllib.error import HTTPError
# Used to throw the error when the server is not found at all
from urllib.error import URLError

#This is the library for the web scraper
from bs4 import BeautifulSoup 

try:
    html = urlretrieve('index.html')
except HTTPError as e:
    print(e)

# For the paramter of Beaitiful soup we can either use html.parser or lxml 
#lxml is useful for sites that have html code that is unfinished or not properly alligned.
bs = BeautifulSoup(html.read(), 'html.parser')

# Findall and Find
# What this does is it finds all the tags with a certain 'tagName' and 'tagAttribute'
# It stores all the objects with the criteria onto a list 

# The function also has a recursive nature. We can pass in a parent tag.
# It would then perform the function on the parent and then on the children.

# It helps us find the number of times individual ids occur by setting the text paramter.
# It allows us to pick the first n entiries by setting the limit parameter.

list_of_requried = bs.findAll('span', {'class':'green'})
for i in list_of_requried:
    print(i.get_text())

# we can add a .children tag to make sure we access onl the children.

# Working with tabular data :
# find().tr would give us the first row in the table
# we can also a dd a .next_siblings tag to make sure we print only elements from the same tag.
# an example of this is working with data in a table.

# we can find the parents data if incase we need to traverse down to find a particular element 

for i in bs.find('table',{'id':'row_name'}).tr.next_siblings:
    print(i.get_text())

print(html.read())