print ('Welcome to Triliza')
a=0
PN1= input ('Give me your name Player 1: ')
PN2= input ('Give me your name Player 2: ')

#Appear of triliza game in the screen
def screen(l):
	print (l[0],'|',l[1],'|',l[2])
	print (l[3],'|',l[4],'|',l[5])
	print (l[6],'|',l[7],'|',l[8])

#Player sequence
def players():
    l=[1,2,3,4,5,6,7,8,9]
    screen(l)
    a=0
    # In Player 1 finishes Triliza, with no winning in 5th round, so in order to
    # not continue running for Player 2, we use parameter a!=5.
    while a!=5:
        a+=1
        checkWithinRange = False
        check = False
        #Check for out of range numbers and already occupied. Good luck!
        while (check == False):
                while (checkWithinRange == False):
                        P1=input (PN1+ ': ')
                        P1=int(P1)
                        if (P1>=1 and P1<=9):
                                checkWithinRange=True
                                if  l[P1-1]=='x' or l[P1-1]=='o':
                                        print ('This number exists already and has the value',l[P1-1], '.Please retype number: ')
                                        checkWithinRange=False
                                else:
                                        check=True
                        else:
                                checkWithinRange=False
                                print ('Type a number in range 1 to 9')
                                
        l[P1-1]='x'
        screen(l)
        
        #Necessary function for winning message for Player 1
        if (l[0]==l[4]==l[8] or l[2]==l[4]==l[6] or l[0]==l[3]==l[6] or l[1]==l[4]==l[7] or l[2]==l[5]==l[8] or l[0]==l[1]==l[2] or l[3]==l[4]==l[5] or l[6]==l[7]==l[8]):
            print ('Well done '+PN1+ ' you won')
            #Action of letting Player 1 to restart Triliza
            Restart= input ('Do you want to play again?[Y/N] ')
            if Restart=='Y':
                a=0
                l=[1,2,3,4,5,6,7,8,9]
                screen (l)
            else:
                a=5
        # Parameter 5 is only enabled if Triliza finishes with no winner and
        # parameter 0 enables if Player 1 wins and we do that so as to
        # restart the while without code continues to execute 
        if a!=5 and a!=0:
            checkWithinRange = False
            check = False
            #Check for out of range numbers and already occupied. Good luck!
            while (check == False):
                while (checkWithinRange == False):
                        P2=input (PN2+ ': ')
                        P2=int(P2)
                        if (P2>=1 and P2<=9):
                                checkWithinRange=True
                                if  l[P2-1]=='x' or l[P2-1]=='o':
                                        print ('This number exists already and has the value',l[P2-1], '.Please retype number: ')
                                        checkWithinRange=False
                                else:
                                        check=True
                        else:
                                checkWithinRange=False
                                print ('Type a number in range 1 to 9')
            l[P2-1]='o'
            screen(l)
            #Necessary function for winning message for Player 2
            if (l[0]==l[4]==l[8] or l[2]==l[4]==l[6] or l[0]==l[3]==l[6] or l[1]==l[4]==l[7] or l[2]==l[5]==l[8] or l[0]==l[1]==l[2] or l[3]==l[4]==l[5] or l[6]==l[7]==l[8]):
                print ('Well done '+PN2+ ' you won')
                Restart= input ('Do you want to play again?[Y/N] ')
                #Action of letting Player 2 to restart Triliza
                if Restart=='Y':
                    a=0
                    l=[1,2,3,4,5,6,7,8,9]
                    screen(l)
                else:
                    a=5

players()
Restart= input ('Do you want to play again?[Y/N] ')
if Restart=='Y':
        players()

    
