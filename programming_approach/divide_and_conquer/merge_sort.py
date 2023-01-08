from algo_fermat_utils.helpers import measure_performance


def merge_sort(array):
    if len(array) <= 1:
        return array
    mid = len(array) // 2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])
    return merge(left, right)


def merge(left, right):
    result = []
    left_index = 0
    right_index = 0
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1
    result.extend(left[left_index:])
    result.extend(right[right_index:])
    return result


@measure_performance
def apply_merge_sort(array):
    return merge_sort(array)


if __name__ == '__main__':
    print(apply_merge_sort([7, 1, 5, 3, 6, 4]))  # [1, 3, 4, 5, 6, 7]
    print(apply_merge_sort([7, 6, 4, 3, 1]))  # [1, 3, 4, 6, 7]
