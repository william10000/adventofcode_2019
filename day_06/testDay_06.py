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

    def testgetOrbitedMap(self):
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

    def testgetAllOrbits_01(self):
        orbitMap = day_06.getOrbitedMap(testDirections)
        actual = day_06.getAllOrbits(orbitMap, 'COM')
        expected = 0
        self.assertEqual(actual, expected)

    def testgetAllOrbits_02(self):
        orbitMap = day_06.getOrbitedMap(testDirections)
        actual = day_06.getAllOrbits(orbitMap, 'B')
        expected = 1
        self.assertEqual(actual, expected)

    def testgetAllOrbits_03(self):
        orbitMap = day_06.getOrbitedMap(testDirections)
        actual = day_06.getAllOrbits(orbitMap, 'K')
        expected = 6
        self.assertEqual(actual, expected)

    def testgetTotalOfAllOrbits_01(self):
        actual = day_06.getTotalOfAllOrbits(testDirections)
        expected = 42
        self.assertEqual(actual, expected)

    def testgetTotalOfAllOrbits_02(self):
        actual = day_06.getTotalOfAllOrbits(directions)
        expected = 119831
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main(verbosity=2)