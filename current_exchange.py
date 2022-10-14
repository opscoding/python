def exchange_money(budget, exchange_rate):
    """
    This function will return the value of
    the exchanged currency
    """
    calc = budget / exchange_rate
    return calc


def get_change(budget, exchanging_value):
    """
    This function will return the amount of
    money that is left from the budget
    """
    money_left = budget - exchanging_value
    return money_left

def get_value_of_bills(denomination, number_of_bills):
    """

    """
    booth = denomination * number_of_bills
    return booth

def get_number_of_bills(budget, denomination):
    """

    """
    budget_bills = int(budget/denomination)
    return budget_bills

def get_letfover_of_bills(budget, denomination):
    """
    """
    leftover = budget %denomination
    return leftover

def exchange_value(budget, exchange_rate, spread, denomination):
    """
    """
    new_exchange_rate = ((spread/100) * exchange_rate + exchange_rate)
    new_calc = budget/new_exchange_rate
    new_cal2 = new_calc % denomination
    right_amount = new_calc - new_cal2
    return int(right_amount)


if __name__ == '__main__':
    # print(exchange_money(127.5, 1.2))
    # print(get_change(127.5, 120))
    # print(get_value_of_bills(5, 128))
    # print(get_number_of_bills(127.5, 5))
    # print(get_letfover_of_bills(127.5,20))
    print(exchange_value(127.25, 1.20, 10, 20))
    print(exchange_value(127.25, 1.20, 10, 5))



