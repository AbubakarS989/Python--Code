
import requests
from bs4 import BeautifulSoup
# website 
link="https://appbrewery.github.io/news.ycombinator.com/"


data=requests.get(url=link)

html_data=data.text

# make a soup
soup=BeautifulSoup(html_data,"html.parser")

# print(soup.prettify())


# title
print(soup.title)
print(soup.title.string)

# TODO: Names 
# TODO: Links
# TODO: Rank [upvote]
# TODO: Sort the data and print according to the highest upvote with respect to the name 
# TODO: Store data into dict.

print("================= Anchor Tags ===============")
all_a=soup.find_all(name="a",class_="storylink") #return list


print("=============== Name  ==============")
rank_name_list=[]
for i in all_a:
    rank_name_list.append(i.string)
    
print("=============== Link  ==============")
all_links=[]
for i in all_a:
    all_links.append(i.get("href"))
print(len(all_links))
print(all_links[29])
print("========================================")
all_score=soup.find_all(name="span",class_="score")
# print(all_score)
print("================= Upvote  =================")

point_lst=[] # not sorted
for i in all_score:
    score=i.string
    point_lst.append(int(score.split(' ')[0]))


# print(point_lst)
sort=sorted(point_lst,reverse=True)

ran_dict={}
for i,rank in enumerate(sort):
    indexs=point_lst.index(rank)
    name=rank_name_list[indexs]
    ran_dict[i+1]={"Name":name,"Upvote":sort[i],"Links":all_links[indexs]}

print(ran_dict)
print("========================================")


