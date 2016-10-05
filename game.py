import time
import random



def tuthack():
    fail = 0
    win = 0
    tutpass = "back"
    print('The password hint is "chair"')
    for x in range(0,4):
        hackTry = input("Type password here\n")
        if hackTry == tutpass:
            print("Access Granted")
            win = 1
            break
        else:
            print("Access Denied")
            fail += 1
    if fail == 4 and win == 0:
        print("Unfortunately, you failed.")
    else:
        print("Congratulations, You Have Successfully Finished the Tutorial!")
        win = 0
        fail = 0

def hack(answer, hint):
    fail = 0
    password = answer
    print('The password hint is ', '"', hint, '"')
    for x in range(0,4):
        hackTry = input("Type password here\n")
        if hackTry == password:
            print("Access Granted")
            print("Success!")
            return True
        else:
            print("Access Denied")
            fail += 1

    print("Unfortunately, you failed.")
    return False

def storymode():
    print("FRIEND: Nick, I've heard Nuke-clear Labs will destroy Mars in an Hour!! ")
    time.sleep(1.5)
    print("WATCH: beepbeep")
    time.sleep(0.5)
    print("FRIEND: No! The Nuke is already in Mars Orbit! I know you're a good Hacker!\n Could you hack the probe to get it away from Mars?")
    time.sleep(5)
    print("YOU: I sure can, Jack!")
    time.sleep(1)
    print("KEYBOARD: clickclickclickclickclickclickclick")
    time.sleep(0.5)
    print("PROBE: Breach in level 1 security.")
    win = hack("kitchen", "oven")
    if win == False:
        time.sleep(2)
        print("Mars Exploded. Game Over.")
    else:
        win = 0
        time.sleep(1)
        print("YOU, JACK: Yes!")
        time.sleep(1)
        print("PROBE: Ready to deorbit weapon.")
        time.sleep(1)
        print("YOU, JACK: Ungh!")
        time.sleep(1)
        print("PROBE: To destroy bomb, you must authenticate")
        time.sleep(0.9)
        win = hack("high", "balcony")
        if win == False:
            time.sleep(2)
            print("Mars Exploded. Game Over.")
            fail = 0
        else:
            win = 0
            fail = 0
            time.sleep(1)
            print("PROBE: Disassembled weapon into 3lem3n7ary particg3uc")
            time.sleep(0.5)
            print("YOU, JACK: Hurray!")
            time.sleep(1)
            print("And that concludes the amazing story of Nick and Jack.")



def tutorial():
    print("Welcome to the Tutorial!")
    time.sleep(1)
    print("In WTH, you'll have to hack (duh) into Nuke-clear NRL and\n find out what they're up to.")
    time.sleep(3)
    print("To do that, You're going to have to do some logical thinking.")
    time.sleep(2)
    print('''If you got a hint saying "bathtub", you'll need to think\n of something that goes together with bathtubs.''')
    time.sleep(3)
    print('You might think, "faucet" or "water". Try out all the results. One of them will be the password.')
    time.sleep(3)
    print("Let's try an example.")
    time.sleep(2)
    tuthack()

print('Hello, and welcome to What the Hack.')
startTut = input("Do you wish to see the Tutorial?\n(y,n) ").lower()
if startTut == "y":
    tutorial()
    time.sleep(1)
    print("\nAnd now, Time for the story mode!\n")
    time.sleep(1)
    storymode()
elif startTut == "n":
    storymode()
else:
    print("Error: unrecognized value")
