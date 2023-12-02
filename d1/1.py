#!/usr/bin/env python3
import re
numwords = {"one":1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight": 8,"nine":9}
renums = re.compile('(?=(1|2|3|4|5|6|7|8|9|one|two|three|four|five|six|seven|eight|nine))')
with open("input") as f:
    part1 = part2 = 0
    for line in f.read().splitlines():
        nums = []
        [nums.append(c) if c.isdigit() else None for c in line]
        part1 += int(''.join([nums[0],nums[-1]])) if len(nums) else None

        matches = re.findall(renums,line)
        first = numwords[matches[0]] if matches[0] in numwords else int(matches[0])
        second = numwords[matches[-1]] if matches[-1] in numwords else int(matches[-1])
        part2 += int(str(first) + str(second))
    print(part1, part2)

