from sys import stdin

elves_cals = []
current_cals = 0

while True:
    line = input()

    if line != "":
        if line == "EOF":
            elves_cals.append(current_cals)
            break
        else:
            current_cals += int(line)
    else:
        elves_cals.append(current_cals)
        current_cals = 0

print(max(elves_cals))
