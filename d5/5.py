#!/usr/bin/env python3
from enum import IntEnum
Map = IntEnum('Map',['SeedSoil','SoilFert','FertWat','WaterLight','LightTemp','TempHum','HumLoc'],start=0)
with open("sample") as f:
    maps = [[] for i in range(7)]
    seedstoplant = []
    currentmap = -1
    for line in f.read().splitlines():
        match line:
            case "seed-to-soil map:": currentmap = Map.SeedSoil
            case "soil-to-fertilizer map:": currentmap = Map.SoilFert
            case "fertilizer-to-water map:": currentmap = Map.FertWat
            case "water-to-light map:": currentmap = Map.WaterLight
            case "light-to-temperature map:": currentmap = Map.LightTemp
            case "temperature-to-humidity map:": currentmap = Map.TempHum
            case "humidity-to-location map:": currentmap = Map.HumLoc
            case "": continue
            case other:
                if "seeds:" in line:
                    seedstoplant = line.split(" ")[1:]
                else:
                    rng = line.split(" ")
                    dstrng = range(int(rng[0]), int(rng[0])+int(rng[2])-1)
                    srcrng = range(int(rng[1]), int(rng[1])+int(rng[2])-1)
                    maps[currentmap].append((srcrng,dstrng)) # append ranges as tuple

    # correspond src to dst, anything not in range is 1:1
    for seed in seedstoplant:

        for ranges in maps[Map.SeedSoil]:
            print("seed",seed,"is in range",ranges[1]) if int(seed) in ranges[1] else print(seed,"maps to",seed)

        #for ranges in maps[Map.SoilFert]:
