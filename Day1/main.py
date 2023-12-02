
total = 0
starts = set(['o', 't', 'f', 's', 'e', 'n'])
nums = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}
for line in open("input.txt"):
    curr = ''
    for i, l in enumerate(line):
        if l.isdigit():
            curr += l
            break

        elif l in starts:
            currWord = l
            found = False
            for j in range(i+1, len(line)):
                if line[j].isalpha():
                    currWord += line[j]
                    if currWord in nums:
                        curr += str(nums[currWord])
                        found = True
                        break
                else:
                    break
            if found:
                break

    for i, l in enumerate(reversed(line)):
        if l.isdigit():
            curr += l
            break
        else:
            currWord = l
            found = False
            for j in range(len(line)-i, len(line)):
                currWord += line[j]
                if currWord in nums:
                    curr += str(nums[currWord])
                    found = True
                    break
        if found:
            break
    total += int(curr)


print(total)

# Part 1
# total = 0
# for line in open("input.txt"):
#     curr = ''
#     for l in line:
#         if l.isdigit():
#             curr += l
#             break

#     for l in line[::-1]:
#         if l.isdigit():
#             curr += l
#             break
#     total += int(curr)

# print(total)
