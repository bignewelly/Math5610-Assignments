from random import random


def get_random_array():
    n = 1000
    v = [0.0] * n

    for i in range(n):
        v[i] = random()

    return v


if __name__ == '__main__':
    array = get_random_array()
    print(array)
