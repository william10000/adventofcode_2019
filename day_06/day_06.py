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


def getPathToTarget(orbitedMap, source, target):
    path = [source]

    if not source in orbitedMap:
        return [source]
    elif orbitedMap[source] == target:
        return [source, target]
    else:
        path = path + getPathToTarget(orbitedMap, orbitedMap[source], target)

    return path


def countTransfersBetweenTwoPoints(orbitedMap, point1, point2):
    transfers = 0
    # assume 'COM' is beginning of tree
    path1 = getPathToTarget(orbitedMap, point1, 'COM')
    path2 = getPathToTarget(orbitedMap, point2, 'COM')

    if path1 == path2:
        return transfers

    transfers = len(path1) + len(path2)
    commonPath = set(path1).intersection(path2)
    transfers -= 2 * len(commonPath)

    # need to subtract 2 to account for 'YOU', 'SAN' unless 1 path complete overlaps the other
    if len(commonPath) != min(len(path1), len(path2)):
        transfers -= 2

    return transfers


if __name__ == '__main__':
    print('Running tests')
    tests = unittest.TestLoader().loadTestsFromModule(testDay_06)
    unittest.TextTestRunner(verbosity=2).run(tests)

    print('Running parts 1')
    print('Part 1')
    answerPart1 = getTotalOfAllOrbits(directions)
    print(answerPart1)

    print('Part 2')
    answerPart2 = countTransfersBetweenTwoPoints(getOrbitedMap(directions),
                                                 'YOU', 'SAN')
    print(answerPart2)
