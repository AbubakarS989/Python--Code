
import json ,requests
from bs4 import BeautifulSoup


link="https://www.empireonline.com/movies/features/best-movies-2/"
data=requests.get(url=link)


# Make  a soup 
soup=BeautifulSoup(data.text,"html.parser")

# print(soup.prettify())


title=soup.find_all(name="h3",class_="listicleItem_listicle-item__title__BfenH")

title_name=[a.string for a in title]

top_movies_list=[]
file=open("100-top-movies.txt","w") 
#? Reverse a list: way 1
# for i in range(1,101):
    # file.write(f"{title_name[-i]}\n")
    
#? Reverse a list: way 2
for i in title_name[::-1]:
    file.write(f"{i}\n")
file.close()
    