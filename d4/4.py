#!/usr/bin/env python3
with open("sample") as f:
    part1 = part2 = 0
    for line in f.read().splitlines():
        nums = line.strip().split(":")[1].split("|")
        wins = set(nums[0].strip().split())
        mine = set(nums[1].strip().split())
        common = len(wins & mine)
        part1 += 2 ** (common - 1) if common else 0
    print(part1)

with open("sample") as f:
    part2 = 0
    for line in f.read().splitlines():
        nums = line.strip().split(":")[1].split("|")
        wins = set(nums[0].strip().split())
        mine = set(nums[1].strip().split())
        common = len(wins & mine)

