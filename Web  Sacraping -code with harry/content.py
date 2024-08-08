
import requests
from bs4 import BeautifulSoup

URL="https://codewithharry.com/"

#! Step 2.  Get HTML from the required website
response=requests.get(url=URL)
response.raise_for_status()
#  Get Data in HTML format
HTML_Content=response.content
# print(HTML_Content)

# ! Step3. Parse the HTML
soup=BeautifulSoup(HTML_Content,"html.parser")
# print(soup)
# print(soup.prettify)

# ! Step4. HTML Tree Traversal

# commonly use type of objects
# 1. Tag
# 2. Navigable String- used by bs4
# 3. Beautiful Soup
# 4. Comment

# # find specific id data
nav_content=soup.find(id='nav-content')
print("------------------------------------------------------")
# print(nav_content.contents) #give all elements in the respective id
# elements(div,form,links,etc)


# .content -
# A Tag's Children are available as a list - store in memory
# .children -
# A Tag's Children are available as a generator -iterate using loops - not  store in memory



# for elem in nav_content.children:
#     print("------------------------------------------------------")
#     print(elem)
    
# for item in nav_content.strings:
# for item in nav_content.stripped_strings:
#     print("------------------------------------------------------")
#     print(item)
    
# get parent class of an id
# print(nav_content.parent)

#give generator so we can iterate
# print(nav_content.parents)
# for item in nav_content.parents:
#     print(item.name)
# it gives us the tree of html page  in reverse order

# Siblings in HTML
# print(nav_content.next_sibling.next_sibling)
# print(nav_content.previous_sibling)


# get specific id or class
# .-> class
# #-> id
elem=soup.select(".container")
# elem=soup.select("#search-toggle")
# elem=soup.select("#__next")
print(elem) #give data as list