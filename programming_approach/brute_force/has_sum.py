from algo_fermat_utils.helpers import measure_performance


@measure_performance
def has_sum(array, target_sum):
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if array[i] + array[j] == target_sum:
                return True
    return False


if __name__ == '__main__':
    print(has_sum([10, 15, 3, 7], 17))  # True because 10 + 7 = 17
    print(has_sum([10, 15, 3, 9], 19))  # True because 10 + 9 = 19
    print(has_sum([10, 15, 3, 7], 20))  # False because there is no pair of numbers that sum to 20
