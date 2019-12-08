import unittest

inputMax = 843167
inputMin = 382345


def validatePassword1(password):
    passwordString = str(password)
    hasDouble = False

    for index in range(1, len(passwordString)):
        if not hasDouble and passwordString[index -
                                            1] == passwordString[index]:
            hasDouble = True

        if int(passwordString[index]) < int(passwordString[index - 1]):
            return False

    if hasDouble:
        return True

    return False


def validatePassword2(password):
    passwordString = str(password)
    hasDouble = False
    for index in range(1, len(passwordString)):
        if not hasDouble and passwordString[index -
                                            1] == passwordString[index]:
            hasDouble = True

            # false alarms
            if index < len(passwordString) - 1 and passwordString[
                    index] == passwordString[index + 1]:
                # next number is same as current
                hasDouble = False
            elif passwordString[index] == passwordString[index - 2]:
                # two numbers ago is same as current
                hasDouble = False
        if int(passwordString[index]) < int(passwordString[index - 1]):
            return False

    if hasDouble:
        return True

    return False


def countValidPasswords1(start, end):
    validPasswords = 0
    for test in range(start + 1, end):
        if validatePassword1(test):
            validPasswords += 1

    return validPasswords


def countValidPasswords2(start, end):
    validPasswords = 0
    for test in range(start + 1, end):
        if validatePassword2(test):
            validPasswords += 1

    return validPasswords


print('Number of valid passwords 1', countValidPasswords1(inputMin, inputMax))
print('Number of valid passwords 2', countValidPasswords2(inputMin, inputMax))


class Test(unittest.TestCase):
    # sample test cases
    def test1(self):
        actual = validatePassword1(122345)
        expected = True
        self.assertEqual(actual, expected)

    def test2(self):
        actual = validatePassword1(111123)
        expected = True
        self.assertEqual(actual, expected)

    def test3(self):
        actual = validatePassword1(135679)
        expected = False
        self.assertEqual(actual, expected)

    def test4(self):
        actual = validatePassword1(223450)
        expected = False
        self.assertEqual(actual, expected)

    def test5(self):
        actual = validatePassword2(112233)
        expected = True
        self.assertEqual(actual, expected)

    def test6(self):
        actual = validatePassword2(123444)
        expected = False
        self.assertEqual(actual, expected)

    def test7(self):
        actual = validatePassword2(111122)
        expected = True
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)
