import random

status=''
keep='y'
while keep=='y':

    computer=random.randint(1,3)
    if computer==1:
        status="rock"
    elif computer==2:
        status="paper"
    elif computer==3:
        status="scissors"
    print status
    
    print "Choise: rock,paper,scissors"
    player=raw_input("Enter your choise:")
    
    if (player=="rock") & (status=="scissors"):
        print "player win (rock)"
        break
    elif (player=="scissors") & (status=="paper"):
        print "player win(scissors)"
        break
    elif (player=="paper") & (status=="rock"):
        print "player win(paper)"
        break
    elif player==status:
        keep='y'
        print "Both are same,so you have play again.."
    else:
        keep='y' 
    