import random as ran

tar_score = int(input("Enter target score: "))
print("Let's get started...")
addp1 = 0
addp2 = 0

while True:
    print("\nPlayer 1 press ENTER to roll the DICE ", end="")
    input()
    p1 = ran.randint(1, 6)
    print("Player 1: ", p1)
    addp1 = addp1 + p1
    if addp1 < tar_score:
        print("Total score - [", addp1, ",", addp2, "]", sep="")
    elif addp1 > tar_score:
        addp1 = addp1 - p1
        print("Total score - [", addp1, ",", addp2, "]", sep="")
    elif addp1 == tar_score:
        print("\nPlayer 1 wins...\n")
        break

    print("\nPlayer 2 press ENTER to roll the DICE ", end="")
    input()
    p2 = ran.randint(1, 6)
    print("Player 2: ", p2)
    addp2 = addp2 + p2
    if addp2 < tar_score:
        print("Total score - [", addp1, ",", addp2, "]", sep="")
    elif addp2 > tar_score:
        addp2 = addp2 -p2
        print("Total score - [", addp1, ",", addp2, "]", sep="")
    elif addp2 == tar_score:
        print("\nPlayer 2 wins...\n")
        break
