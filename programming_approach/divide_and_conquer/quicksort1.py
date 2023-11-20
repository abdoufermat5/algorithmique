def partition(arr, low, high):
    pivot = arr[high]

    i = low - 1  # car arr[low] pourrait etre superieur a pivot

    # on range a gauche tous les elements inferieur a pivot
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    # on met a gauche du pivot l'element a la position i+1
    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    # retourne le prochain pivot
    return i + 1


from algo_fermat_utils.helpers import measure_performance


@measure_performance
def quicksort(arr, l, h):

    if l<h:
        # on partitionne et on recupere le pivot
        pi = partition(arr, l, h)

        # on traite tous les elements a gauche du pivot
        quicksort(arr, l, pi - 1)

        # on traite tous les elements a gauche du pivot
        quicksort(arr, pi + 1, h)


if __name__ == "__main__":
    test_array = [10, 80, 30, 90, 40, 50, 70]
    low = 0
    high = len(test_array) - 1
    quicksort(test_array, low, high)
    print("------------------------------------------------")
    print(test_array)