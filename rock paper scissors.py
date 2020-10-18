import random
WORDS=("rock","paper","scissors")

while 1:
    x=input().casefold()
    y=random.choice(WORDS)
    print("Computer :" + y)
    print('Press any key to break')
    if x==y:
        print('Tie')
    elif (x=='rock' and y=='paper'):
        print('Computer won!!!!')
    elif (x=='rock' and y=='scissors'):
        print('You won!!!!')
    elif (x=='paper' and y=='rock'):
        print('You won!!!!')
    elif (x=='paper' and y=='scissors'):
        print('Computer won!!!!')
    elif (x=='scissors' and y=='paper'):
        print('You won!!!!')
    elif (x=='scissors' and y=='rock'):
        print('Computer won!!!!')
            #print('Press any key to break')
    else:
        print('Thank you for playing!')

#capital letters

        #to break the game for users
