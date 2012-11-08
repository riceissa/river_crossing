#!/usr/bin/python3

# See https://en.wikipedia.org/wiki/Missionaries_and_cannibals_problem

# todo: - jealous husbands or c-m
        #- enter solution matrix t check solution to either puzzle
        #- interactive mode to play
            #+ graphic display

side0 = ["m1", "m2", "m3", "c1", "c2", "c3"]
side1 = []
boat0 = ["boat"]
boat1 = []

def move(obj):
    '''move an object to the other side of the river'''
    if obj in boat0:
        # the object is the boat on side0, so move to side1
        boat1.append(boat0.pop(boat0.index(obj)))
    elif obj in boat1:
        # the object is the boat on side1, so move to side0
        boat0.append(boat1.pop(boat1.index(obj)))
    elif obj in side0:
        # the object is a person on side0 so move to side1
        side1.append(side0.pop(side0.index(obj)))
    else:
        # the object is a person on side1 so move to side0
        side0.append(side1.pop(side1.index(obj)))

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
    draw(side0, side1)
    # people on the same side as the boat are "good"
    good_people = []
    if "boat" in boat0:
        good_people = side0
    else:
        good_people = side1
    print("Available to choose from: " + ', '.join(good_people))
    player_move = input("Choose your move: ")
    # check that people on a different side than the boat are not moved
    for i in side0.extend(side1):
        if i in player_move:
            if not (i in good_people):
                print("Cannot move " + i + "; the boat is on the wrong side!\n")
    # check that not more than two people are moved
    counter = 0
    for i in side0.extend(side1):
        if i in player_move:
            counter += 1
    if counter > 2:
        print("Cannot move more than two!\n")
    # check that when the move is completed, there are not more cannibals
    # than missionaries on each side
    temp_people_dict = dict(people_dict)
    for i in people_names:
        if i in player_move:
            temp_people_dict[i] = alterbit(temp_people_dict[i])
    for side in [0,1]:
        if missionary_on_side(side, temp_people_dict):
            if cannibal_number(side, temp_people_dict) > missionary_number(side, temp_people_dict):
                if side == 0:
                    print("Cannibals may not outnumber missionaries on top side!")
                else:
                    print("Cannibals may not outnumber missionaries on bottom side!")
                return 0
    # perform the move for real
    for i in good_people:
        if i in player_move:
            move(i)
    move("boat")

def draw(top, bottom):
    print("\n" + ' '.join(top))
    if "boat" in top:
        print('''~~B~~~~~~~~~~~~~~
    R i v e r
~~~~~~~~~~~~~~~~~''')
    else:
        print('''~~~~~~~~~~~~~~~~~
    R i v e r
~~B~~~~~~~~~~~~~~''')
    print(' '.join(bottom) + "\n")

turn_number = 0
while not (sum(people_dict[i] for i in people_names) == 6):
    turn()
    turn_number += 1
print("Congratulations! You won in " + str(turn_number) + " turns. (Minimum 11)")
