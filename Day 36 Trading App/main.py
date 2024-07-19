
import requests
from twilio.rest import Client
import os





# News API
# https://newsapi.org/account

Stock_Name = "TSLA"
Company_Name = "Tesla Inc"


Stock_End_Point = "https://www.alphavantage.co/query"
Stock_KEy = "H14ON4IV8JYG7VVN"

News_Endpoint = "https://newsapi.org/v2/everything"
NEws_API_KEY = "39e0e4c3cc79457894600c735a544436"

# Yesterday closing stoock price
# "Time Series (Daily)": {
# "2024-05-24": {
# "1. open": "174.8350",
# "2. high": "180.0800",
# "3. low": "173.7300",
# "4. close": "179.2400",
# "5. volume": "65584478"
# },
stock_params = {

    "function": "TIME_SERIES_DAILY",
    "symbol": Stock_Name,
    "apikey": Stock_KEy

}


#! Our standard API rate limit is 25 requests per day
# Stock  Data
response = requests.get(Stock_End_Point, params=stock_params)
response.raise_for_status()
# print(response)

# my method -> yesterday stock closing price
# stock_data=response.json()["Time Series (Daily)"]
# date="2024-05-24"
# # data could be any
# yesterday_st_data=stock_data[date]
# # parameter could be close,open,high,low that u want
# open_D=yesterday_st_data["1. open"]
# close_D=yesterday_st_data["4. close"]
# print(open_D)
# print(close_D)


# course method -> yesterday stock closing price

# data=response.json()
# print(data)




data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]
print("------------yesterday stock closing price--------------")
print(yesterday_closing_price)
close_list = []
# append into a list
close_list.append(yesterday_closing_price)

# TODO: get one day before  yesterday closing stock price
before_yesterday_data = data_list[1]
before_yesterday_closing_price = before_yesterday_data["4. close"]
print("------------before yesterday stock closing price--------------")
print(before_yesterday_closing_price)
# append into a list
close_list.append(before_yesterday_closing_price)

print("------------list of before yesterday and yesterday stock closing price--------------")
print(close_list)

print("------------iterate the list of stock closing price--------------")
for i in range(len(close_list)):
    print(close_list[i])

# TODO: get the difference btw both princes
difference = float(yesterday_closing_price) -float(before_yesterday_closing_price)
up_down=None
if difference >1:
    up_down="🔺"
else:
    up_down="🔻"



print("------------difference of stock closing price--------------")


# TODO: get the percentage % of  difference  btw before and yesterday
print("------------difference percentage  of stock closing price--------------")
diff_percentage = (difference/float(yesterday_closing_price))*100
print(diff_percentage)


# TODO:  if percentage greater than 5  then print 'get news' from the NEWS API
print("------------News Articles--------------\n")
# QIn-Title= To search for particular article
if abs(diff_percentage) > 0.1:
    news_params = {
        "apiKey": NEws_API_KEY,
        "qInTitle": Company_Name
    }
    news_response = requests.get(News_Endpoint, params=news_params)
    news_response.raise_for_status()
    # get list of articles
    articles=news_response.json()["articles"]
    # list slicing get first 3 articles
    three_articles=articles[:3]  #list of three articles
    # print 3 article one by one    
    headline=[]
    for i in range(3):
        print(f"Article:  {i+1}")
        print(f"{three_articles[i]}\n")
        
        # title description
        # article=three_articles[i]
        # title=article["title"]
        # print(title)
        # description=article["description"]
        # print(description)
        # headline.append([f"Headline:{title}.\nBrief: {description}"])
        # todo create a list of three articles with their respective (title,description)
        # list comprehension
        headline=[f"{Stock_Name}:{up_down} {diff_percentage}%Headline:{article["title"]}.\nBrief:{article["description"]}" for article in three_articles]
        
      
      
print(headline)  #return ist of three articles
# # Msg setup   

account_sid='AC3bec8567c443a97e6fd714945e9fec8a'
auth_token='e0ae3304415de5f8551d444cebe64778'
client = Client(account_sid, auth_token)
for i in range(3):
    message = client.messages.create(
    from_='+16364518304',
    body=headline[i],
    to='+923187764396'
    )
    print(message.sid)


    
#! basic structure of news Data dictionary
# {   {status}, 
#     {total-result},
#      {"articles":
#         [
#             {
#                 {source, {id }, {name}},
#                 {author},
#                 {title},
#                 {description},
#                 {url},
#                 {urltoimage},
#                 {publishment},
#                 {content}
#                 }
#         ]
        
#     }
# }
# {
# "status": "ok",
# "totalResults": 1723,
# -"articles": [
# -{
# -"source": {
# "id": null,
# "name": "Yahoo Entertainment"
# },
# "author": "Lawrence Bonk",
# "title": "VR classics Job Simulator and Vacation Simulator come to Apple Vision Pro",
# "description": "The Apple Vision Pro was marketed primarily as a productivity machine, but as any active VR user can tell you, it’s the games that sell these devices. Apple’s headset offers access to hundreds of games, but mostly as quick and dirty iPad ports that show up as…",
# "url": "https://consent.yahoo.com/v2/collectConsent?sessionId=1_cc-session_6a6ab0dd-00f8-4399-ad8d-1d7bc76dd1bb",
# "urlToImage": null,
# "publishedAt": "2024-05-28T19:05:45Z",
# "content": "If you click 'Accept all', we and our partners, including 237 who are part of the IAB Transparency &amp; Consent Framework, will also store and/or access information on a device (in other words, use … [+678 chars]"
# },
