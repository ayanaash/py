#1
import datetime

today=datetime.date.today()
print(today-datetime.timedelta(days=5))


#2
import datetime

x=datetime.datetime.now()
today=datetime.date.today()
yesterday=today-datetime.timedelta(days=1)
tomorrow=today+datetime.timedelta(days=1)
print("Yesterday: ", yesterday)
print("Today: ", x)
print("Tomorrow: ", tomorrow)


#3
import datetime

now=datetime.datetime.now()
print(now.replace(microsecond=0))


#4
import datetime

d1=datetime.datetime(2026,2,25,9,0,0)
d2=datetime.datetime(2026,2,25,10,0,0)

print((d2-d1).total_seconds())   #3600