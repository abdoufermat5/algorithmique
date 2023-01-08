import random


def random_permutation(array):
    for i in range(len(array)):
        j = random.randint(i, len(array) - 1)
        array[i], array[j] = array[j], array[i]
    return array
