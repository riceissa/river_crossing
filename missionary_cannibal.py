#!/usr/bin/python3

# See https://en.wikipedia.org/wiki/Missionaries_and_cannibals_problem

# todo: - jealous husbands or c-m
        #- enter solution matrix t check solution to either puzzle
        #- interactive mode to play
            #+ graphic display

m1 = 0
m2 = 0
m3 = 0
c1 = 0
c2 = 0
c3 = 0
people_dict = {"m1": m1, "m2": m2, "m3": m3, "c1": c1, "c2": c2, "c3": c3}
people_names = list(people_dict.keys())
boat = 0

def alterbit(bit):
    return abs(bit - 1)

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
    boat_other = 0
    for i in people_names:
        if i in move:
            if not (i in good_people):
                boat_other = 1
                print("Cannot move " + i + "; the boat is on the other side!\n")
                return 0
    counter = 0
    for i in people_names:
        if i in move:
            counter += 1
    if counter > 2:
        print("Cannot move more than two!\n")
        return 0
    for i in people_names:
        if i in move:
            people_dict[i] = alterbit(people_dict[i])
    print(people_dict)
    boat = alterbit(boat)

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

while not (sum(people_dict[i] for i in people_names) == 6):
    turn()
print("Congratulations you won!")
