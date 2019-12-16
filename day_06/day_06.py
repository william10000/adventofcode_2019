import unittest
import testDay_06

fileHandleInput = open('input_day_06.txt')
fileHandleTest1 = open('test_day_06.txt')

# store map as list of [orbitee, orbiter]
directions = [
    row.split(')') for row in [line.rstrip('\n') for line in fileHandleInput]
]
testDirections = [
    row.split(')') for row in [line.rstrip('\n') for line in fileHandleTest1]
]


# returns a dictionary of { orbiter: orbited }
def getOrbitedMap(directions):
    orbitedMap = {}
    for direction in directions:
        orbitedMap[direction[1]] = direction[0]
    return orbitedMap


# traverses the tree to get direct and indirect orbited elements
def getAllOrbits(orbitedMap, orbiter):
    numberOfOrbits = 0

    if orbiter in orbitedMap:
        numberOfOrbits = 1 + getAllOrbits(orbitedMap, orbitedMap[orbiter])
    else:
        return 0

    return numberOfOrbits


def getTotalOfAllOrbits(directions):
    totalOrbits = 0
    orbitedMap = getOrbitedMap(directions)

    for orbiter in orbitedMap:
        totalOrbits += getAllOrbits(orbitedMap, orbiter)

    return totalOrbits


if __name__ == '__main__':
    print('Running tests')
    tests = unittest.TestLoader().loadTestsFromModule(testDay_06)
    unittest.TextTestRunner(verbosity=2).run(tests)

    print('Running parts 1')
    print('Part 1 ')
    answerPart1 = getTotalOfAllOrbits(directions)
    print(answerPart1)
