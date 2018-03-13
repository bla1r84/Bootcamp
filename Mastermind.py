import random

print ("You should type 4 numbers of your choice between 1 to 6 and find the correct combination. Good luck!")
#Generate list
generatedList = []
for i in range (4):
    generatedNumber = random.randint(1,6)
    generatedList.append(generatedNumber)

while generatedList[0]==generatedList[1] or generatedList[0]==generatedList[2] or generatedList[0]==generatedList[3] or generatedList[1]==generatedList[2] or generatedList[1]==generatedList[3] or generatedList[2]==generatedList[3]:                
    for i in range (4):
        generatedList[i]=random.randint(1,6)

#Matches and correct positions of numbers
for i in range (15):
    #Read user's input
    userList=[]
    userList = (input(""))
    pos1 = int(userList[0])
    pos2 = int(userList[1])
    pos3 = int(userList[2])
    pos4 = int(userList[3])

    while pos1>6 or pos2>6 or pos3>6 or pos4>6 or pos1==pos2 or pos1==pos3 or pos1==pos4 or pos2==pos3 or pos2==pos4 or pos3==pos4:
        print ("Number range is between 1 to 6 and we don't have double numbers")
        userList=[]
        userList = (input(""))
        pos1 = int(userList[0])
        pos2 = int(userList[1])
        pos3 = int(userList[2])
        pos4 = int(userList[3])

    countPos=0
    countCorrect=0

    if (pos1 == generatedList[0]):
        countCorrect = 1
    elif (pos1== generatedList[1]):
          countPos = 1
    elif (pos1== generatedList[2]):
          countPos = 1
    elif (pos1== generatedList[3]):
          countPos = 1

    if (pos2 == generatedList[0]):
        countPos = countPos+1
    elif (pos2== generatedList[1]):
        countCorrect = countCorrect+1
    elif (pos2== generatedList[2]):
        countPos = countPos+1
    elif (pos2== generatedList[3]):
        countPos = countPos+1

    if (pos3 == generatedList[0]):
        countPos = countPos+1
    elif (pos3== generatedList[1]):
          countPos = countPos+1
    elif (pos3== generatedList[2]):
          countCorrect = countCorrect+1
    elif (pos3== generatedList[3]):
          countPos = countPos+1

    if (pos4 == generatedList[0]):
        countPos = countPos+1
    elif (pos4== generatedList[1]):
          countPos = countPos+1
    elif (pos4== generatedList[2]):
          countPos = countPos+1
    elif (pos4== generatedList[3]):
          countCorrect = countCorrect+1

    if countCorrect==4:
        print ("You won.")
        print ("The list was: ", generatedList)
    else:
        print ("You have", countCorrect, "numbers in place and",countPos, "numbers in wrong places.")
        print ("You have left", 14-i, "tries.")
        if i==14:
            print ("The code was: ", generatedList)
