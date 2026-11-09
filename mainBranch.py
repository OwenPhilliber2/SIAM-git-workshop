# Main branch file

def HelloWorld():
    print("Hello World!")

def addNumbers(a, b):
    return a + b

def isOdd(num):
    if (num % 2):
        return 1
    if not (num % 2):
        return 0

if __name__ == '__main__':
    HelloWorld()

    print(f'Adding 9 and 3 = {addNumbers(9, 3)}')

    print(f'Is 3 odd? {isOdd(3)}')
    print(f'Is 4 odd? {isOdd(4)}')
