

# Get the product data from amazon
# get the current price [float]
# if the price drop from the current price
    # : send email to the user of [price day drop]
    # Email MSG: The product is now 99$, below the target price, Buy now!
    
    
    
#? imports

import json,requests
from bs4 import BeautifulSoup
from Email_emplate import Send_Email

link="https://appbrewery.github.io/instant_pot/"
data=requests.get(url=link)

# Make a soup
soup=BeautifulSoup(data.text,"html.parser")

# print(soup.prettify())

#TODO: get product title
# refine then paragraph and get the title
description_list=soup.find_all(name="span", id="productTitle")
description_text=description_list[0].string
text_list=description_text.strip().split(' ')

# list of required words from the text list
text=[]
for i in range(0,4):
    text.append(text_list[i])
    
# finally i got the title
Title=" ".join(text)
print(Title)


#TODO: get product link
# ? link in request is used as a product links

#TODO: get price

price=soup.find_all(name="span", class_="aok-offscreen")
get_price=[float((item.getText()).split("$")[1]) for item in price]


static_price=get_price[0]

# The product is now 99$, below the target price, Buy now!
    
BUY_PRICE=100
if static_price<BUY_PRICE:
    content=f"The {Title} is now {static_price} RS, below the target price, Buy now!"
    Subject="Price Alert 📢"
    print(Send_Email(content=content,Subject=Subject))
    
