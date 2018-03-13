P1= input ('What is your name?\n')
P2= input ('What is your name?\n')
print ('RULES \nRock wins Scissors \nScissors wins Paper \nPaper wins Rock \nGood Luck!\n')
print ('1:Rock \n2:Scissors \n3:Paper')

def checkValidInput(player):
    a_1=False
    b_1=False
    while a_1==False:
        while b_1==False:
            choice= input('Type 1-3 your choice '+player+ ': ')
            if choice.isdigit():
                choice=int(choice)
                b_1=True
                if not (choice>=1 and choice<=3):
                    b_1=False
                    print ('You are not within range')
                else:
                    a_1=True
            else:
                print ('This is not a digit 1-3.')
    return int(choice)

def checkWinner (C1,C2):
    if C1==1:
        if C2==1:
            print ('No one wins!')
        elif C2==2:
            print (P1+" wins")
        else:
            print (P2+" wins")
    elif C1==2:
        if C2==1:
            print (P2+" wins")
        elif C2==2:
            print ('No one wins!')
        else:
            print (P1+" wins")
    elif C1==3:
        if C2==1:
            print (P1+" wins")
        elif C2==2:
            print (P2+" wins")
        else:
            print ('No one wins!')
            
replay=True
while replay==True:
        C1=checkValidInput(P1)
        C2=checkValidInput(P2)
        checkWinner(C1,C2)
        R= input ('Do you want to play again?[Y/N] ')
        while R!="Y" and R!="N":
            R= input ('Do you want to play again? Just type Y:Yes and N:No [Y/N] ')
        if R=='Y':
            replay=True
        else:
            replay=False
            print ('We don\'t care! Goodbye')

