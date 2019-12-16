fileHandleInput = open('input_day_06.txt')
fileHandleTest1 = open('test_day_06.txt')

# store map as list of [orbitee, orbiter]
directions = [
    row.split(')') for row in [line.rstrip('\n') for line in fileHandleTest1]
]

print(directions)


def getAllOrbits(directions):
    numberOfOrbits = 0

    return numberOfOrbits
