import datetime as dt

current_date=dt.datetime.now()  #entire date
year=current_date.year
month=current_date.month
date=current_date.day
day=current_date.weekday()
second=current_date.second
microsecond=current_date.microsecond
print(current_date)
# print(year)
# print(month)
# print(date)
# print(day) #0-monday 1-tuesday....
# print(second)
# print(microsecond)



# check it works or not!
if year==2024 :
    print("hi")

# create our own dt object
date_of_birth=dt.datetime(year=2004,month=10,day=20,hour=5)
print(date_of_birth)


