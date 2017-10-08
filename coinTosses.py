
def coin():
    head = 0
    tail = 0
    for i in range (1,5000):
        from random import randint
        random = (randint(0, 1))

        if random == 1:
            head = head + 1
            print "Attmpt #", i, "it's a head!", "Got", head, "heads so far and", tail, "tails so far"
        if random == 0:
            tail = tail + 1
            print "Attmpt #", i, "it's a Tail!", "Got", head, "heads so far and", tail, "tails so far"
    print "end of the program!"

coin()
