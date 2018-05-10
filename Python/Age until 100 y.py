import datetime
name=input ('What is your name? ')
age=input ('What is your age? ')
age=int(age)
currentDate = datetime.datetime.now()
currentYear = currentDate.year
Birth_Date= currentYear-age
dif_age= 100-age
Y100=currentYear+dif_age
times=input('How many times you need the message to be printed in the screen? ')
times=int(times)
Y100=str(Y100)
print (times*(' You will become 100 years in the year ' +Y100+ '. \n'))
for i in range (times):
    print ('You will become 100 years in the year', Y100+ '.')
