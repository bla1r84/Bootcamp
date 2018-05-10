name=input ('Give me your nickname.\n')
age=input ('Give me your age '+name+ '\n')
age=int(age)
while age<=0:
    print ('It is impossible '+name+'.\n')
    age=input ('Give me your age '+name+ '\n')
    age=int(age)
if age>0 and age<18:
    print ('You will be available to access in', 18-age, 'years ' +name+ '.I\'m sorry!\n')
else:
    print ('Welcome to our community '+name+'!')
    a=''
    for i in range (10):
        a+='_'
    print (a)
    Food=input ('What is your favourite food '+name+'? \n')
    Sport=input ('What do you like to do in your spare time '+name+'? \n')
    sign=input ('What is your sign ' +name+ '? \n')
    profile=(name,age, sign, Food, Sport)
    print (profile)
shut_down= input ('Press enter to shut me down')
