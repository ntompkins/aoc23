#!/usr/bin/env python3
with open("input") as f:
    maxcolors = { "red":12,"green":13,"blue":14 }
    possibleround = []
    maxneeded = {}
    totalpossible = 0
    totalpower = 0
    for line in f.read().splitlines():
        possibleround.append(True)
        cur_round = line.split(':')[0].split(' ')[1]
        maxneeded[cur_round] = {"red":0,"green":0,"blue":0}
        for reveal in line.split(':')[1].split(';'):
            for cubes in reveal.split(','):
                num_col = cubes.strip().split(' ')
                if int(num_col[0]) > maxcolors[num_col[1]]:
                    possibleround[-1] = False
                if maxneeded[cur_round][num_col[1]] < int(num_col[0]):
                    maxneeded[cur_round][num_col[1]] = int(num_col[0])
        totalpower += maxneeded[cur_round]["red"] * maxneeded[cur_round]["blue"] * maxneeded[cur_round]["green"]
    for idx, possible in enumerate(possibleround):
        totalpossible += idx + 1 if possible else 0
    print("part 1: ",totalpossible)
    print("part 2: ",totalpower)

