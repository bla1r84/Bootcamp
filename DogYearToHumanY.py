textCheck=False
rangeCheck=False
while rangeCheck==False:
    while textCheck==False:
        dogYears=(input("Give me your dog's age: \n"))
        if dogYears.isdigit():
            dogYears=int(dogYears)
            textCheck=True
            if dogYears<0 or dogYears>=30:
                  print("This is not a valid value.")
                  textCheck=False
            else:
                  rangeCheck=True
        else:
            print ("Not number.")
            

def dogToHuman(dogYears):
    if dogYears<=2:
        print ("Your dog is actually:", dogYears)
    else:
        dogYears=((dogYears-2)*5)+2
        print ("Your dog is actually:",dogYears)

dogToHuman(dogYears)
