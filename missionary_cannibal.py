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

def missionary_on_side(bit, d):
    # min == 0 implies there is a missionary on side 0
    # min == 1 implies there is no missionary on side 0
    # max == 0 implies there is no missionary on side 1
    # max == 1 implies there is a missionary on side 1
    if bit:
    # is there a missionary on side 1?
        if max(d["m1"], d["m2"], d["m3"]):
        # so there is a missionary on side 1; return yes
            return 1
        else:
            return 0
    else:
    # is there a missionary on side 0?
        if  0 == min(d["m1"], d["m2"], d["m3"]):
        # so there is a missionary on side 0; return yes
            return 1
        else:
            return 0

def missionary_number(bit, d):
    count = 0
    if d["m1"] == bit: count += 1
    if d["m2"] == bit: count += 1
    if d["m3"] == bit: count += 1
    return count

def cannibal_number(bit, d):
    count = 0
    if d["c1"] == bit: count += 1
    if d["c2"] == bit: count += 1
    if d["c3"] == bit: count += 1
    return count

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
                print("Cannot move " + i + "; the boat is on the other side!\n")
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
    temp_people_dict = people_dict
    for i in people_names:
        if i in move:
            temp_people_dict[i] = alterbit(temp_people_dict[i])
    for side in [0,1]:
        if missionary_on_side(side, temp_people_dict):
            if cannibal_number(side, temp_people_dict) > missionary_number(side, temp_people_dict):
                print("Cannibals may not outnumber missionaries on side " + str(side) + "!")
                #return 0
                break
    # perform the move for real
    counter = 0
    for i in people_names:
        if i in move:
            people_dict[i] = alterbit(people_dict[i])
            counter += 1
    #print(people_dict)
    if counter != 0:
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
