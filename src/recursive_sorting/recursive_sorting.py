# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # TO-DO
    # keep looping until we look at everything in both arrays
    while max(len(arrA), len(arrB)) > 0:
        for i in range(len(merged_arr)):  # begin to assign things its place in merged_arr
            if len(arrA) == 0:
                merged_arr[i] = arrB.pop(0)
            elif len(arrB) == 0:
                merged_arr[i] = arrA.pop(0)
            elif arrA[0] < arrB[0]:
                merged_arr[i] = arrA.pop(0)
            else:  # arrA[0] > arrB[0]
                merged_arr[i] = arrB.pop(0)

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # TO-DO
    if len(arr) > 1:
        # halve the array
        arrA = merge_sort(arr[:len(arr)//2])
        arrB = merge_sort(arr[len(arr)//2:])

        arr = merge(arrA, arrB)
    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # no extra variables?
    if arr[mid] <= arr[mid + 1]:
        return arr

    while start <= mid and mid + 1 <= end:
        if arr[start] <= arr[mid + 1]:
            start += 1
        else:
            arr.insert(start, arr.pop(mid + 1))
            start += 1
            mid += 1
    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO
    if l < r:
        # Improvement: move (l + r)//2 into its own variable named middle
        merge_sort_in_place(arr, l, (l + r)//2)
        merge_sort_in_place(arr, ((l + r)//2) + 1, r)

        merge_in_place(arr, l, (l + r)//2, r)
    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
