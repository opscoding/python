EXPECTED_BAKE_TIME = 40


def bake_time_remaining(actual_min):
    if (EXPECTED_BAKE_TIME <= actual_min):
        remaining = (actual_min - EXPECTED_BAKE_TIME)
    else:
        remaining = (EXPECTED_BAKE_TIME - actual_min)
    return remaining


def preparation_time_in_minutes(layers):
    amount_time = layers * 2
    return amount_time

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    print(preparation_time_in_minutes(number_of_layers) + bake_time_remaining(elapsed_bake_time))

if __name__ == '__main__':
    elapsed_time_in_minutes(3, 20)
