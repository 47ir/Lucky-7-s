#make lucky 7's
import random
import sys
start = raw_input("There is a one dollar fee each time you roll. Click 'enter' to start the game: ")
rounds = 0
if start in ['q','quit','exit']:
    sys.exit(0)
elif start == '':
    print 'WELCOME TO LUCKY SEVENS! You have $10 to play with. Each time you roll you will virtually roll a pair of six sided dice. If you just so happen to get a total of seven, you will gain five dollars. If you do NOT roll seven, you will lose one dollar, it will cost one dollar.'
#Here we go, you have $10 to play with. Each time you type roll, 
    currency = 10
    print "You have", currency,"dollars"
elif start != '':
            sys.exit(0)
best = 0
while currency>0:
    roll = raw_input("You can type anything if you want to quit. Click the 'enter' button to roll the dice: ")
    while currency > 0:
        die1 = random.randint(1,6)
        die2 = random.randint(1,6)
        print "First die: ", die1
        print "Second die:", die2
        print "Total: ", die1 + die2
        if die1 + die2 == 7:
            print 'You rolled a seven. Here\'s five dollars'
            currency  += 4
            rounds += 1
            print "You now have",currency, "dollars"
        elif die1 + die2 != 7:
            currency -= 1
            rounds += 1
            print "You didn\'t roll a seven, there goes one of your dollars.\n"
            print "You now have", currency, "dollar[s]."
        elif roll != '':
            print 'You have exited the game. Run the kernal again to start the game.'
        if currency > best:
            best = currency  
print 'You lasted', rounds, 'rounds.'
print 'The most amount of money you had was', best, 'dollars.'
    

sys.exit(0)