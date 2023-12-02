with open("input.txt") as f:
    total = 0

    for line in f:
        cubes = line.split(':')[1]
        games = cubes.split(';')
        max_blue = 0
        max_red = 0
        max_green = 0
        for game in games:
            game = game.strip()
            round = game.split()

            for i, r in enumerate(round):
                if r.isdigit():
                    color = round[i+1]
                    if color[-1] == ",":
                        color = color[:-1]
                    if color == 'red':
                        max_red = max(max_red, int(r))
                    elif color == 'green':
                        max_green = max(max_green, int(r))
                    elif color == 'blue':
                        max_blue = max(max_blue, int(r))

        total += max_red * max_green * max_blue

print(total)


# Part 1
# with open("input.txt") as f:

#     total = 0

#     most = {
#         'red': 12,
#         'green': 13,
#         'blue': 14
#     }

#     for line in f:
#         id, cubes = line.split(':')
#         id = int(id.split(' ')[1])
#         games = cubes.split(';')
#         valid = True
#         for game in games:
#             game = game.strip()
#             round = game.split()
#             for i, r in enumerate(round):
#                 if r.isdigit():
#                     color = round[i+1]
#                     if color[-1] == ",":
#                         color = color[:-1]
#                     if most[color] < int(r):
#                         valid = False
#                         break

#             if not valid:
#                 break

#         if valid:
#             total += id

# print(total)
