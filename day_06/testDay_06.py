import unittest
import day_06 as day_06

fileHandleInput = open('input_day_06.txt')
fileHandleTest1 = open('test_day_06.txt')

# store map as list of [orbitee, orbiter]
directions = [
    row.split(')') for row in [line.rstrip('\n') for line in fileHandleInput]
]
testDirections = [
    row.split(')') for row in [line.rstrip('\n') for line in fileHandleTest1]
]


class TestDay06(unittest.TestCase):
    # orbitMap = day_06.getOrbitedMap(testDirections)

    def test_getOrbitedMap(self):
        actual = day_06.getOrbitedMap(testDirections)
        expected = {
            'B': 'COM',
            'C': 'B',
            'D': 'C',
            'E': 'D',
            'F': 'E',
            'G': 'B',
            'H': 'G',
            'I': 'D',
            'J': 'E',
            'K': 'J',
            'L': 'K',
        }
        self.assertEqual(actual, expected)

    def test_getAllOrbits_01(self):
        orbitMap = day_06.getOrbitedMap(testDirections)
        actual = day_06.getAllOrbits(orbitMap, 'COM')
        expected = 0
        self.assertEqual(actual, expected)

    def test_getAllOrbits_02(self):
        orbitMap = day_06.getOrbitedMap(testDirections)
        actual = day_06.getAllOrbits(orbitMap, 'B')
        expected = 1
        self.assertEqual(actual, expected)

    def test_getAllOrbits_03(self):
        orbitMap = day_06.getOrbitedMap(testDirections)
        actual = day_06.getAllOrbits(orbitMap, 'K')
        expected = 6
        self.assertEqual(actual, expected)

    def test_getTotalOfAllOrbits_01(self):
        actual = day_06.getTotalOfAllOrbits(testDirections)
        expected = 42
        self.assertEqual(actual, expected)

    def test_getTotalOfAllOrbits_02(self):
        actual = day_06.getTotalOfAllOrbits(directions)
        expected = 119831
        self.assertEqual(actual, expected)

    def test_getPathToTarget_01(self):
        orbitMap = day_06.getOrbitedMap(testDirections)
        actual = day_06.getPathToTarget(orbitMap, 'K', 'COM')
        expected = ['K', 'J', 'E', 'D', 'C', 'B', 'COM']
        self.assertEqual(actual, expected)

    def test_getPathToTarget_02(self):
        orbitMap = day_06.getOrbitedMap(testDirections)
        actual = day_06.getPathToTarget(orbitMap, 'C', 'COM')
        expected = ['C', 'B', 'COM']
        self.assertEqual(actual, expected)

    def test_getPathToTarget_03(self):
        orbitMap = day_06.getOrbitedMap(testDirections)
        actual = day_06.getPathToTarget(orbitMap, 'COM', 'COM')
        expected = ['COM']
        self.assertEqual(actual, expected)

    def test_countTransfersBetweenTwoPoints02(self):
        orbitMap = day_06.getOrbitedMap(testDirections)
        actual = day_06.countTransfersBetweenTwoPoints(orbitMap, 'COM', 'COM')
        expected = 0
        self.assertEqual(actual, expected)

    def test_countTransfersBetweenTwoPoints03(self):
        orbitMap = day_06.getOrbitedMap(testDirections)
        actual = day_06.countTransfersBetweenTwoPoints(orbitMap, 'H', 'I')
        expected = 3
        self.assertEqual(actual, expected)

    def test_countTransfersBetweenTwoPoints04(self):
        orbitMap = day_06.getOrbitedMap(testDirections)
        actual = day_06.countTransfersBetweenTwoPoints(orbitMap, 'B', 'G')
        expected = 1
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main(verbosity=2)