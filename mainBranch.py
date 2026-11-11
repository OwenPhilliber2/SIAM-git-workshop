# Main branch file

def HelloWorld():
    print("Hello World!")

def addNumbers(a, b):
    return a + b

def isOdd(num):
    if num % 2 == 1:
        return 1
    if num % 2 == 0:
        return 0

def abs(num):
    if num < 0:
        return -1 * num
    if num >= 0:
        return num

if __name__ == '__main__':
    HelloWorld()

    print(f'Adding 9 and 3 = {addNumbers(9, 3)}')

    print(f'Is 3 odd? {isOdd(3)}')
    print(f'Is 4 odd? {isOdd(4)}')

    print(f'Absolute value of -5: {abs(-5)}')
    print(f'Absolute value of 3: {abs(3)}')
