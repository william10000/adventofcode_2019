import unittest

input = [
    1, 0, 0, 3, 1, 1, 2, 3, 1, 3, 4, 3, 1, 5, 0, 3, 2, 10, 1, 19, 1, 6, 19, 23,
    1, 23, 13, 27, 2, 6, 27, 31, 1, 5, 31, 35, 2, 10, 35, 39, 1, 6, 39, 43, 1,
    13, 43, 47, 2, 47, 6, 51, 1, 51, 5, 55, 1, 55, 6, 59, 2, 59, 10, 63, 1, 63,
    6, 67, 2, 67, 10, 71, 1, 71, 9, 75, 2, 75, 10, 79, 1, 79, 5, 83, 2, 10, 83,
    87, 1, 87, 6, 91, 2, 9, 91, 95, 1, 95, 5, 99, 1, 5, 99, 103, 1, 103, 10,
    107, 1, 9, 107, 111, 1, 6, 111, 115, 1, 115, 5, 119, 1, 10, 119, 123, 2, 6,
    123, 127, 2, 127, 6, 131, 1, 131, 2, 135, 1, 10, 135, 0, 99, 2, 0, 14, 0
]

inputUsed = [
    1, 12, 2, 3, 1, 1, 2, 3, 1, 3, 4, 3, 1, 5, 0, 3, 2, 10, 1, 19, 1, 6, 19, 23,
    1, 23, 13, 27, 2, 6, 27, 31, 1, 5, 31, 35, 2, 10, 35, 39, 1, 6, 39, 43, 1,
    13, 43, 47, 2, 47, 6, 51, 1, 51, 5, 55, 1, 55, 6, 59, 2, 59, 10, 63, 1, 63,
    6, 67, 2, 67, 10, 71, 1, 71, 9, 75, 2, 75, 10, 79, 1, 79, 5, 83, 2, 10, 83,
    87, 1, 87, 6, 91, 2, 9, 91, 95, 1, 95, 5, 99, 1, 5, 99, 103, 1, 103, 10,
    107, 1, 9, 107, 111, 1, 6, 111, 115, 1, 115, 5, 119, 1, 10, 119, 123, 2, 6,
    123, 127, 2, 127, 6, 131, 1, 131, 2, 135, 1, 10, 135, 0, 99, 2, 0, 14, 0
]

def runIntcode(intcode):
    current = 0
    while intcode[current] != 99:
        firstValue = intcode[intcode[current + 1]]
        secondValue = intcode[intcode[current + 2]]
        if intcode[current] == 1:
            answer = firstValue + secondValue
        else:
            answer = firstValue * secondValue
        intcode[intcode[current + 3]] = answer
        current = current + 4
    return intcode

finalAnswer = runIntcode(inputUsed)
print(finalAnswer)
print(finalAnswer[0])

class Test(unittest.TestCase):
    def test1(self):
        actual = runIntcode([1, 0, 0, 0, 99])
        expected = [2, 0, 0, 0, 99]
        self.assertEqual(actual, expected)

    def test2(self):
        actual = runIntcode([2, 3, 0, 3, 99])
        expected = [2, 3, 0, 6, 99]
        self.assertEqual(actual, expected)

    def test3(self):
        actual = runIntcode([2, 4, 4, 5, 99, 0])
        expected = [2, 4, 4, 5, 99, 9801]
        self.assertEqual(actual, expected)

    def test4(self):
        actual = runIntcode([1, 1, 1, 4, 99, 5, 6, 0, 99])
        expected = [30, 1, 1, 4, 2, 5, 6, 0, 99]
        self.assertEqual(actual, expected)

    def test5(self):
        actual = runIntcode([1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50])
        expected = [3500, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50]
        self.assertEqual(actual, expected)

unittest.main(verbosity=3)
