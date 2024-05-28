
import requests
# News API
# https://newsapi.org/account
Stock_Name = "TSLA"
Company_Name = "Tesla Inc"
Stock_End_Point = "https://www.alphavantage.co/query"
News_Endpoint = "https://newsapi.org/v2/everything"

Stock_API = "H14ON4IV8JYG7VVN"
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
    "symbol":Stock_Name,
    "apikey":Stock_API

}
#! Our standard API rate limit is 25 requests per day
response=requests.get(Stock_End_Point,params=stock_params)
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

data=response.json()
# print(data)
# exit()
data=response.json()["Time Series (Daily)"]
data_list=[value  for  (key,value) in data.items() ]
yesterday_data=data_list[0]
yesterday_closing_price=yesterday_data["4. close"]
print("------------yesterday stock closing price--------------")
print(yesterday_closing_price)
close_list=[]
# append into a list
close_list.append(yesterday_closing_price)

#TODO: get one day before  yesterday closing stock price
before_yesterday_data=data_list[1]
before_yesterday_closing_price=before_yesterday_data["4. close"]
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
difference=abs(float(yesterday_closing_price)-float(before_yesterday_closing_price))
# abs return +ev value

print("------------difference of stock closing price--------------")
print(difference)

# TODO: get the percentage % of  difference  btw before and yesterday
print("------------difference percentage  of stock closing price--------------")
diff_percentage=(difference/float(yesterday_closing_price))*100
print(diff_percentage)


# TODO:  if percentage greater than 5  then print 'get news' from the NEWS API
if diff_percentage>3.0:
    print("Get News")


