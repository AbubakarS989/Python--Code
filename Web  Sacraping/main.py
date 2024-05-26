# Web Scraping->
    # ! get html file from server,but browser(chrome) ko dyn ki bajeee ap apny python ma usy ly aty ha,jo html file ka data hota ha  us ko apny computer ma store kr lyty ha
    # ! is sary process ko web scarping kehty ha
    
#! IMportant Libraries
# pip install bs4 ->beautify soup-provide functions for parsing 
# pip install html5lib -> for parsing data 
# pip install request -> for making request of data and extract data for use.. to the website server

# we can access any tag in html (anchor,div,img,)
# ! Web scraping in two ways:
# 1. Using API
# 2. HTML Web scraping using some tool like bs4(beautify soap)

# TODO  Important functions are written at the bottom
#! Step 1. Download all requirements

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
 

title=soup.title
print(type(title)) #1 <class 'bs4.element.Tag'>s
print(type(title.string)) #2 <class 'bs4.element.Tag'>
print(type(soup)) #3 <class 'bs4.BeautifulSoup'>

# get the title of HTML Page
# print(title)

# get all paragraphs from the HTML pages
paras=soup.find_all("p")
# print(paras)



print("----------------- get first paragraph----------------------")
# get first paragraph
print(soup.find("p"))
comments = soup.find_all(string=lambda text: isinstance(text, Comment))
print(comments)
exit()
print("----------------- get first paragraph class----------------------")
# get first paragraph class
print(soup.find("p")["class"])

# Find all elements of specific class (mt-2 ) for example:
# All paragraphs of specified class
print("------------------All paragraphs of specified class---------------------")
print(soup.find("p",class_="mt-2"))
print("-------------------All divs of specified class--------------------")
# All divs of specified class
print(soup.find("div",class_="mt-2").get_text())


# Get the TEXT from the Tags like div , paragraph
print("------------------Get the TEXT from the Tags like div , paragraph---------------------")
print(soup.find('p').get_text())
print("------------------Get the TEXT from the DIV---------------------")
print(soup.find("div",class_="mt-2").get_text())

print("------------------Get All Text from the Website---------------------")
# Get All Text from the Website
print(soup.get_text())



# Get all Anchor Tags from the HTML pages
print("-----------------get all Anchor Tags from the HTML pages----------------------")
anchor=soup.find_all("a")
print(anchor)
print("-----------------get all the links from Anchor Tags from the HTML pages----------------------")
# append links in a set for non repeated links
links=set()
for link in anchor:
    print(link.get("href"))
    links.add("https://codewithharry.com"+link.get("href"))

print(links)
# with open("links.txt","w") as r:
#     r.write(link)
 




# comment
markup="<p><!-- This is a comment --></p>"

comment_soup=BeautifulSoup(markup)
print(comment_soup)
print(comment_soup.p)
print(comment_soup.p.string)  # to get a text from comment




# !Functions

# [HTML_Content]=response.content
# soup=BeautifulSoup([html content])
# get_text()
# get_all()
# anchor=soup.find_all("a")
# link.get("href")
# print(soup.get_text())
# soup.find("div",class_="mt-2").get_text()
# soup.find('p').get_text()
# soup.find("p")
# soup.find("p")["class"]
# soup.title