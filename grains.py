number = int(input("What is the square number? "))
if number > 64 or number < 1:
    raise ValueError("square must be between 1 and 64")

def square(number):
    """
    """
    n = 1
    grain = 1
    while n < number and number > 1:
        grain = grain * 2
        n += 1
    print(f'The total grains in the square', number, 'is', grain)


def total():
    """
    """
    n = 1
    grain = 1
    while n <= 64:
        grain = grain * 2
        n += 1
    print(f'The total grains on the chessboard is', grain )

if __name__ == '__main__':
    square(number)
    total()