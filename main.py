# Simple digital logic addition subtraction calculator

#    1  2  3  4
# 1  1  2  3  *
# 2  4  5  6  /
# 3  7  8  9  -
# 4     0     +


# modeled off of key pad where output is [R1 R2 R3 R4 C1 C2 C3 C4], i.e. 1 = [1 0 0 0 1 0 0 0] , 4 = [0 1 0 0 1 0 0 0]\\
# define the key pad outputs based on input
def key_out(butt):
    if butt == '1':
        return [1, 0, 0, 0, 1, 0, 0, 0]
    elif butt == '2':
        return [1, 0, 0, 0, 0, 1, 0, 0]
    elif butt == '3':
        return [1, 0, 0, 0, 0, 0, 1, 0]
    elif butt == '4':
        return [0, 1, 0, 0, 1, 0, 0, 0]
    elif butt == '5':
        return [0, 1, 0, 0, 0, 1, 0, 0]
    elif butt == '6':
        return [0, 1, 0, 0, 0, 0, 1, 0]
    elif butt == '7':
        return [0, 0, 1, 0, 1, 0, 0, 0]
    elif butt == '8':
        return [0, 0, 1, 0, 0, 1, 0, 0]
    elif butt == '9':
        return [0, 0, 1, 0, 0, 0, 1, 0]
    elif butt == '0':
        return [0, 0, 0, 1, 0, 1, 0, 0]
    elif butt == '+':
        return [0, 0, 0, 1, 0, 0, 0, 1]
    elif butt == '-':
        return [0, 0, 1, 0, 0, 0, 0, 1]


# define and or and not gates which will be used to do rest of logic
def and_g(a, b):
    if a == 1 and b == 1:
        return 1
    else:
        return 0


def or_g(a, b):
    if a == 1 or b == 1:
        return 1
    else:
        return 0


def not_g(a):
    if a == 1:
        return 0
    else:
        return 1


# display key pad as well as ask for inputs
print('this is a simple calculator that can add 2 single digit numbers \n the layout of the keypad is as follows:')
print('    1  2  3  4\n______________\n1|  1  2  3  *\n2|  4  5  6  /\n3|  7  8  9  -\n4|     0     +')
print('Please input only numbers and characters on the key pad')
input1 = input('first input:')
input2 = input('action:')
input3 = input('second input:')
print(input1 + ' ' + input2 + ' ' + input3)
[a1, b1, c1, d1, e1, f1, g1, h1] = key_out(input1)
[a2, b2, c2, d2, e2, f2, g2, h2] = key_out(input2)
[a3, b3, c3, d3, e3, f3, g3, h3] = key_out(input3)
print('num1: ' + str([a1, b1, c1, d1, e1, f1, g1, h1]))
print('action: ' + str([a2, b2, c2, d2, e2, f2, g2, h2]))
print('num2: ' + str([a3, b3, c3, d3, e3, f3, g3, h3]))
# convert input to pin outputs that would be received from a keypad














