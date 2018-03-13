import random

#Generate list
generatedList = []
for i in range (4):
    generatedNumber = random.randint(1,6)
    generatedList.append(generatedNumber)
print (generatedList)

a=True
while a==True:
    for i in range (4):
        for j in range (i+1):
            if generatedList[i]==generatedList[j]:
                generatedList[i]=random.randint(1,6)
    a=False
print (generatedList)
            
    

#Read user's input
userList=[]
userList = (input("Enter four numbers of your choice from 1 to 6: "))
pos1 = int(userList[0])
pos2 = int(userList[1])
pos3 = int(userList[2])
pos4 = int(userList[3])
#userList = [pos1,pos2,pos3,pos4]

#Matches and correct positions of numbers
if (pos1 == generatedList[0]):
    countCorrect = 1
elif (pos1== generateList[1]):
      countPos = 1
elif (pos1== generateList[2]):
      countPos = 1
elif (pos1== generateList[3]):
      countPos = 1

if (pos2 == generatedList[0]):
    countPos+ = 1
elif (pos2== generateList[1]):
    countCorrect+ = 1
elif (pos2== generateList[2]):
    countPos+ = 1
elif (pos2== generateList[3]):
    countPos+ = 1

if (pos3 == generatedList[0]):
    countPos+ = 1
elif (pos3== generateList[1]):
      countPos+ = 1
elif (pos3== generateList[2]):
      countCorrect+ = 1
elif (pos3== generateList[3]):
      countPos+ = 1

if (pos4 == generatedList[0]):
    countPos+ = 1
elif (pos4== generateList[1]):
      countPos+ = 1
elif (pos4== generateList[2]):
      countPos+ = 1
elif (pos4== generateList[3]):
      countCorrect+ = 1

if countCorrecr==4:
    print ("You won.")
else:
    print ("You have", countCorrect, "numbers in place and",countPos, "numbers in wrong places.")
