#!/usr/bin/python3

# See https://en.wikipedia.org/wiki/Missionaries_and_cannibals_problem

# to-do: enter solution matrix to check solution to either puzzle

people_dict = {"h1": 0, "h2": 0, "h3": 0, "w1": 0, "w2": 0, "w3": 0}
people_names = list(people_dict.keys())
boat = 0

def alterbit(bit):
    return abs(bit - 1)

def jealousy(d):
    for i in [1,2,3]:
        if d["h" + str(i)] != d["w" + str(i)]:
        # husband is not with his wife
            if (d["h1"] == d["w" + str(i)]) or (d["h2"] == d["w" + str(i)]) or (d["h3"] == d["w" + str(i)]):
            # another husband is with the wife, so jealousy occurs
                return 1
    return 0

def turn():
    draw(people_dict)
    global boat
    # people on the same side as the boat are "good"
    good_people = []
    for i in people_names:
        if people_dict[i] == boat:
            good_people.append(i)
    print("Available to choose from: " + ', '.join(good_people))
    move = input("Choose your move. ")
    # check that people on a different side than the boat are not moved
    boat_other = 0
    for i in people_names:
        if i in move:
            if not (i in good_people):
                boat_other = 1
                print("Cannot move " + i + "; the boat is on the wrong side!\n")
                return 0
    # check that not more than two people are moved
    counter = 0
    for i in people_names:
        if i in move:
            counter += 1
    if counter > 2:
        print("Cannot move more than two!\n")
        return 0
    # check that when the move is completed, there are not more cannibals
    # than missionaries on each side
    temp_people_dict = dict(people_dict)
    # dry-run to see if there are any jealous husbands
    for i in people_names:
        if i in move:
            temp_people_dict[i] = alterbit(temp_people_dict[i])
    if jealousy(temp_people_dict):
        print("A wife cannot be left with another man unless her husband is present.")
        return 0
    # perform the move for real
    counter = 0
    for i in people_names:
        if i in move:
            people_dict[i] = alterbit(people_dict[i])
            counter += 1
    if counter != 0:
        boat = alterbit(boat) # don't move the boat if no one crossed

def draw(position_dict):
    global boat
    not_crossed = []
    crossed = []
    for i in people_names:
        if position_dict[i] == 0:
            not_crossed.append(i)
        else:
            crossed.append(i)
    print("\n" + ' '.join(not_crossed))
    if not boat:
        print('''~~B~~~~~~~~~~~~~~
    R i v e r
~~~~~~~~~~~~~~~~~''')
    else:
        print('''~~~~~~~~~~~~~~~~~
    R i v e r
~~B~~~~~~~~~~~~~~''')
    print(' '.join(crossed) + "\n")

turn_number = 0
while not (sum(people_dict[i] for i in people_names) == 6):
    turn()
    turn_number += 1
print("Congratulations! You won in " + str(turn_number) + " turns. (Minimum 11)")
