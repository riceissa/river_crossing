# README

`missionary_cannibal.py` is an interactive version of the ["missionaries and cannibals" puzzle](https://en.wikipedia.org/wiki/Missionaries_and_cannibals_problem). (A river crossing puzzle where the boat carries a maximum of two people and requires at least one, and the cannibals cannot outnumber the missionaries on either side (unless there are no missionaries on that side).)

`jealous_husbands.py` is an interactive version of the similar "jealous husbands" puzzle. (Each wife cannot be with a man who is not her husband, unless her husband accompanies her.)

## Example

Below is an example from the "missionaries and cannibals" puzzle. `m`*n* for *n* = 1, 2, 3 represents the missionaries and similarly for cannibals. The top (above the river) represents the people who have not yet crossed, and similarly for the bottom. The `B` shows the location of the boat (The `Available to choose from` text also gives the same information.).

    m1 m3 m2 c3 c2 c1
    ~~B~~~~~~~~~~~~~~
        R i v e r
    ~~~~~~~~~~~~~~~~~


    Available to choose from: m1, m3, m2, c3, c2, c1
    Choose your move. m3 c1

    m1 m2 c3 c2
    ~~~~~~~~~~~~~~~~~
        R i v e r
    ~~B~~~~~~~~~~~~~~
    m3 c1

    Available to choose from: m3, c1
    Choose your move.
