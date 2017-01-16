
from sys import exit

def gold_room():
    print "This room is full of gold. ......"

    choice = raw_input()
    if "0" in choice or "1" in choice:
        how_much = int(choice)
    else:
        dead("Man, learn to type a number.")

    if how_much < 50:
        print "Nice, you're not greedy, you win!"
        exit(0)
    else:
        dead("You greedy bastard!")

def bear_room():
    print "There is a bear here."
    print "The bear has ......"
    print "The fat bear ......"
    print "How are you ......"
    bear_moved = False

    while True:
        choice = raw_input("> ")

        if choice == "take money":
            dead("The bear looks ......")
        elif choice == "taunt bear" and not bear_moved:
            print "The bear has ......"
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            dead("The bear gets ......")
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print "I got no ......"


def cthulhu_room():
    print "Here you see ......"
    print "He, it, whatever ......"
    print "Do you flee ......"

    choice = raw_input("> ")

    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("Well that was tasty!")
    else:
        cthulhu_room()

def dead(why):
    print why, "Good job!"
    exit(0)

def start():
    print "You are in a dark room."
    print "There is a door to your right and left."
    print "Which one do you take?"

    choice = raw_input("> ")

    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulhu_room()
    else:
        dead("You stumble around ......")

start()
