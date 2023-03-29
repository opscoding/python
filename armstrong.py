number = int(input("input the number: "))

def is_armstrong_number(number):
    """
    This function will return if a number is armstrong,
    e.g
    9 is an Armstrong number, because 9 = 9^1 = 9
    10 is not an Armstrong number, because 10 != 1^2 + 0^2 = 1
    """
    order = len(str(number))
    sum = 0
    temp = number
    while temp > 0:
        digit = temp % 10
        sum += digit ** order
        temp //= 10

    return (number == sum)


if __name__ == '__main__':
    print(is_armstrong_number(number))