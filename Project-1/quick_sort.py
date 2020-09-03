def partition(arr, low, high, func):
    """
    This function takes last element as pivot, places
    the pivot element at its correct position in sorted
    array, and places all smaller (smaller than pivot)
    to left of pivot and all greater elements to right
    of pivot
    :param func:
    :param arr: The input partition
    :param low: The lower element of the partition
    :param high: The high element of the partition
    :return: i + 1
    """

    i = low - 1  # index of smaller element
    pivot = arr[high]  # pivot is always last element

    for j in range(low, high):

        # If current element is smaller than the pivot
        if func(arr[j]) < func(pivot):
            # increment index of smaller element
            i = i + 1
            # Swap the smaller element
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort(arr, func, low=0, high=None):
    """
    The main function that implements QuickSort
    :param func: custom function to sort
    :param arr: Array to be sorted
    :param low: Starting index
    :param high: Ending index
    :return: nothing
    """
    if high is None:
        high = len(arr) - 1

    if low < high:
        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(arr, low, high, func)

        # Separately sort elements before
        # partition and after partition
        quick_sort(arr, func, low, pi - 1)
        quick_sort(arr, func, pi + 1, high)
