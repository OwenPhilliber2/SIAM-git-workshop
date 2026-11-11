def subtractNumbers(a, b):
    return a - b

def isEven(num):
    if (num % 2) == 0:
        return 'Yes!'
    if (num % 2) == 1:
        return 'No'

if __name__ == '__main__':
    print(f'Is 2 even? {isEven(2)}')
    print(f'Is 9 even? {isEven(9)}')

    print(f'Is 9 minus 2 even? {isEven(subtractNumbers(9, 2))}')