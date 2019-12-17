import unittest
import testDay_05

inputUsed = [3,225,1,225,6,6,1100,1,238,225,104,0,1001,191,50,224,101,-64,224,224,4,224,1002,223,8,223,101,5,224,224,1,224,223,223,2,150,218,224,1001,224,-1537,224,4,224,102,8,223,223,1001,224,2,224,1,223,224,223,1002,154,5,224,101,-35,224,224,4,224,1002,223,8,223,1001,224,5,224,1,224,223,223,1102,76,17,225,1102,21,44,224,1001,224,-924,224,4,224,102,8,223,223,1001,224,4,224,1,224,223,223,101,37,161,224,101,-70,224,224,4,224,1002,223,8,223,101,6,224,224,1,223,224,223,102,46,157,224,1001,224,-1978,224,4,224,102,8,223,223,1001,224,5,224,1,224,223,223,1102,5,29,225,1101,10,7,225,1101,43,38,225,1102,33,46,225,1,80,188,224,1001,224,-73,224,4,224,102,8,223,223,101,4,224,224,1,224,223,223,1101,52,56,225,1101,14,22,225,1101,66,49,224,1001,224,-115,224,4,224,1002,223,8,223,1001,224,7,224,1,224,223,223,1101,25,53,225,4,223,99,0,0,0,677,0,0,0,0,0,0,0,0,0,0,0,1105,0,99999,1105,227,247,1105,1,99999,1005,227,99999,1005,0,256,1105,1,99999,1106,227,99999,1106,0,265,1105,1,99999,1006,0,99999,1006,227,274,1105,1,99999,1105,1,280,1105,1,99999,1,225,225,225,1101,294,0,0,105,1,0,1105,1,99999,1106,0,300,1105,1,99999,1,225,225,225,1101,314,0,0,106,0,0,1105,1,99999,108,226,226,224,1002,223,2,223,1005,224,329,101,1,223,223,108,677,677,224,1002,223,2,223,1006,224,344,1001,223,1,223,8,677,677,224,102,2,223,223,1006,224,359,101,1,223,223,7,226,677,224,102,2,223,223,1005,224,374,101,1,223,223,107,226,226,224,102,2,223,223,1006,224,389,101,1,223,223,7,677,226,224,1002,223,2,223,1006,224,404,1001,223,1,223,1107,677,226,224,1002,223,2,223,1006,224,419,1001,223,1,223,1007,226,226,224,102,2,223,223,1005,224,434,101,1,223,223,1008,226,677,224,102,2,223,223,1005,224,449,1001,223,1,223,1007,677,677,224,1002,223,2,223,1006,224,464,1001,223,1,223,1008,226,226,224,102,2,223,223,1006,224,479,101,1,223,223,1007,226,677,224,1002,223,2,223,1005,224,494,1001,223,1,223,108,226,677,224,1002,223,2,223,1006,224,509,101,1,223,223,8,226,677,224,102,2,223,223,1005,224,524,1001,223,1,223,107,677,677,224,1002,223,2,223,1005,224,539,101,1,223,223,107,226,677,224,1002,223,2,223,1006,224,554,101,1,223,223,1107,226,677,224,1002,223,2,223,1006,224,569,1001,223,1,223,1108,677,226,224,102,2,223,223,1005,224,584,1001,223,1,223,1008,677,677,224,102,2,223,223,1005,224,599,1001,223,1,223,1107,677,677,224,102,2,223,223,1006,224,614,101,1,223,223,7,226,226,224,102,2,223,223,1005,224,629,1001,223,1,223,1108,677,677,224,102,2,223,223,1006,224,644,1001,223,1,223,8,677,226,224,1002,223,2,223,1005,224,659,101,1,223,223,1108,226,677,224,102,2,223,223,1005,224,674,101,1,223,223,4,223,99,226]


# takes the opcode (without the ones and tens places) and gets the correct
# parameters depending on intermediate vs. position mode
def getParameterFromOpcodeString(current, intcode):
    modeString = str(intcode[current])[:-2]
    numberOfInstructions = len(modeString)
    opcode = int(str(intcode[current])[-2:])

    if numberOfInstructions == 0:
        # both or all in position mode
        if opcode == 4:
            return [intcode[intcode[current + 1]], None]
        else:
            return [
                intcode[intcode[current + 1]], intcode[intcode[current + 2]]
            ]

    # first is either 0 or 1
    if modeString[-1] == '0':
        parameter1 = intcode[intcode[current + 1]]
    else:
        parameter1 = intcode[current + 1]

    # 2nd either doesn't exist or is 1
    if opcode == 4:
        return [parameter1, None]
    elif numberOfInstructions > 1:
        parameter2 = intcode[current + 2]
    else:
        parameter2 = intcode[intcode[current + 2]]

    return [parameter1, parameter2]


def runIntcode(intcodeInput, firstInput):
    intcode = [] + intcodeInput
    input = firstInput

    current = 0
    outputs = []

    while current < len(intcode) and intcode[current] != 99:
        opcode = int(str(intcode[current])[-2:])  # get ones and tens digits

        if opcode == 1:  # add two values
            [parameter1,
             parameter2] = getParameterFromOpcodeString(current, intcode)
            intcode[intcode[current + 3]] = parameter1 + parameter2
            current += 4
        elif opcode == 2:  # multiply two values
            [parameter1,
             parameter2] = getParameterFromOpcodeString(current, intcode)
            intcode[intcode[current + 3]] = parameter1 * parameter2
            current += 4
        elif opcode == 3:  # use the input
            # assume only position mode for now
            intcode[intcode[current + 1]] = input
            current += 2
        elif opcode == 4:  # add output to output array
            [parameter1,
             parameter2] = getParameterFromOpcodeString(current, intcode)
            outputs.append(parameter1)
            current += 2
        elif opcode == 5:
            [parameter1,
             parameter2] = getParameterFromOpcodeString(current, intcode)
            if parameter1 != 0:
                current = parameter2
            else:
                current += 3
        elif opcode == 6:
            [parameter1,
             parameter2] = getParameterFromOpcodeString(current, intcode)
            if parameter1 == 0:
                current = parameter2
            else:
                current += 3
        elif opcode == 7:
            [parameter1,
             parameter2] = getParameterFromOpcodeString(current, intcode)
            if parameter1 < parameter2:
                intcode[intcode[current + 3]] = 1
            else:
                intcode[intcode[current + 3]] = 0
            current += 4
        elif opcode == 8:
            [parameter1,
             parameter2] = getParameterFromOpcodeString(current, intcode)
            if parameter1 == parameter2:
                intcode[intcode[current + 3]] = 1
            else:
                intcode[intcode[current + 3]] = 0
            current += 4

    return [intcode, outputs]

if __name__ == '__main__':
    print('Running tests')
    tests = unittest.TestLoader().loadTestsFromModule(testDay_05)
    unittest.TextTestRunner(verbosity=2).run(tests)

    print('Running parts 1 and 2')
    print('Part 1')
    answerPart1 = runIntcode(inputUsed, 1)
    print(answerPart1[1])

    print('Part 2')
    answerPart2 = runIntcode(inputUsed, 5)
    print(answerPart2[1])
