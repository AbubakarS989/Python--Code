

# importing our parser
from bs4 import BeautifulSoup

# in case of our parser not working
import lxml

with open("index.html","r") as f:
    html_data=f.read()
    # html_data=f.readlines() -> give data into list 
    soup1=BeautifulSoup(f,"html.parser")


# print(html_data)

# print(soup1)



# make a soup
# ? lxml parser way
# soup=BeautifulSoup(html_data,"lxml")

soup=BeautifulSoup(html_data,"html.parser")

# print(soup.prettify())





# get title

print(soup.title)   # entire element
print(soup.title.name)  # name of element
print(soup.title.string) # name of title


#? extract one target tg
# anchor tag -a
print(soup.a)

# paragraph tag -p
print(soup.p)

# unordered tag - ul
print(soup.ul)

# ordered tag - ol
print(soup.ol)

# heading tag - h1
print(soup.h1)

# heading tag - h2
print(soup.h2)


# heading tag - h3
print(soup.h3.string)

# extract all text from a page

# print(soup.get_text())

# ? extract all specified tags using tag name

all_anchor_tags=soup.find_all(name="a")  #return list 
# print(all_anchor_tags)
for link in soup.find_all("a"):
    print(link.getText()) # text of link
    
for link in soup.find_all("a"):
    print(link.get("href")) #get the actual link
    
    
    
# ? target on a specific tag of their specific attribute
# with id
specific_id_attribute=soup.find(name="h1",id="target_class")  
print(specific_id_attribute)



# ? target on a specific tag of their specific attribute
# with class
specific_class_attribute=soup.find(name="p",class_="story")  
print(specific_clas_attribute)







