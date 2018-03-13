import random

#Generate list
generatedList = []
for i in range (4):
    generatedNumber = random.randint(1,6)
    generatedList.append(generatedNumber)
print (generatedList)

#Read input
userList=[]
userList = (input("Enter numbers: "))
pos1 = int(userList[0])
pos2 = int(userList[1])
pos3 = int(userList[2])
pos4 = int(userList[3])

countCorrect = 0
if (pos1 == generatedList[0]):
    countCorrect += 1
if (pos2 == generatedList[1]):
    countCorrect += 1
if (pos3 == generatedList[2]):
    countCorrect += 1
if (pos4 == generatedList[3]):
    countCorrect += 1
print ("Exact matches: " + str(countCorrect))
