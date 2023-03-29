def eat_ghost(power_pellet_active, touching_ghost):
    """
    This function will returns True only if Pac-Man has a power pellet active and is touching a ghost.
    """
    # if power_pellet_active and touching_ghost == True:
    #     return True
    return bool(power_pellet_active and touching_ghost )

def score(touching_power_pellet, touching_dot):
    """
    This function will returns True if Pac-Man is touching a power pellet or a dot.
    """
    # if touching_power_pellet or touching_dot == True:
    #     return True
    return bool(touching_power_pellet or touching_dot)

def lose(power_pellet_active, touching_ghost):
    """
    This function will returns True if Pac-Man is touching a ghost and does not have a power pellet active.
    """
    # if power_pellet_active == False and touching_ghost == True:
    #     return True
    return bool(touching_ghost and not power_pellet_active)

def win(has_eaten_all_dots, power_pellet_active, touching_ghost):
    """
    This function will returns True if Pac-Man has eaten all of the dots and has not lost based on the function "lose".
    """
    # if has_eaten_all_dots == True and lose(power_pellet_active, touching_ghost) == False:
    #     return True
    return bool(has_eaten_all_dots and lose(power_pellet_active, touching_ghost) is False)

if __name__ == '__main__':
    # print(eat_ghost(False, True))
    # print(score(False, True))
    print(lose(True, False))
    # print(win(True, False, True))
