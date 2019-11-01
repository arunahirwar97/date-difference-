import datetime
x = datetime.date.today()
print("Current date = ",x)
y = x - datetime.timedelta(days = 1)
print("Date of Yesterday :",y)
t = x + datetime.timedelta(days = 1)
print("Date of Tomorrow :",t)