import time
import sys
import random
selection = 7
count = 0
print("You must choose. But choose wisely. For as the True Grail will bring you life -- the False Grail will take it from you.")
while True:
    selection = 7
    while selection == 0 or selection >= 7:
        randomnum = random.randint(1,6)
        selection = int(input("There are 6 goblets, pick a goblet: "))
        count += 1
        if selection == randomnum:
            print("You have chosen")
            time.sleep(1)
            print(".")
            time.sleep(1)
            print(".")
            time.sleep(1)
            print(".")
            time.sleep(1)
            print("wisely")
            time.sleep(2)
            print("Blessed are the cheesemakers!")
        elif selection == 0:
            print("why")
        elif selection >= 7:
            print("lol")
        else:
            print("You have chosen")
            time.sleep(1)
            print(".")
            time.sleep(1)
            print(".")
            time.sleep(1)
            print(".")
            time.sleep(1)
            print("poorly")
            time.sleep(2)
            print("correct answer: ", randomnum)
            randspeech = random.randint(1,5)
            if randspeech == 1:
                print("You are all individuals!")
            elif randspeech == 2:
                print("Cheer up, mate. You know what they say: some things in life are bad. They can really make you mad. Other things just make you swear and curse. When you're chewing on life's gristle, don't grumble; give a whistle, and this'll help things turn out for the best. And... always look on the bright side of life...")
            elif randspeech == 3:
                print("Crucifixion?")
            elif randspeech == 4:
                print("Thwow him to the floow")
            elif randspeech == 5:
                print("Wait until Biggus Dickus hears of this!!!")
            else:
                print("error")
        if count == 3:
            print("He's not the Messiah. He's a very naughty boy")
            break
        answer = input('Play again? (y/n): ')
        if answer in ("y", "n", "Y", "N"):
            if answer == "y" or answer == "Y":
                continue
            else:
                print ("Goodbye")
                sys.exit()
        else:
            print("I'll take that as a no then")
            time.sleep(5)
            sys.exit()