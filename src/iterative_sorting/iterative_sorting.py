# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(cur_index, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j

        # TO-DO: swap
        holder = arr[smallest_index]
        arr[smallest_index] = arr[cur_index]
        arr[cur_index] = holder

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # loop through the array for undetermined amount of times
    # while things are unsorted, compare
    # if thing to the right is bigger than thing, swap

    something_has_swapped = True
    while something_has_swapped:
        something_has_swapped = False
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                temp = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = temp
                something_has_swapped = True
    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr
