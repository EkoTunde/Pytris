import random


def randint(a, b, *exceptions):
    rand = 0
    while rand == 0 or (exceptions and rand in exceptions):
        rand = random.randint(a, b)
    return rand
