# return index of n in arr, returns -1 if n does not exist in arr
# arr is assumed to already be sorted

def binary_search(arr, n):
    if len(arr) == 0:
        return Exception("Binary Search - Empty Array")

    left = 0
    right = len(arr) - 1
    mid = (right + left) // 2

    while abs(right - left) > 0:
        if arr[mid] < n:
            left = mid + 1
            mid = (left + right) // 2
        elif n < arr[mid]:
            right = mid - 1
            mid = (left + right) // 2
        else:
            return mid


    if arr[mid] == n:
        return mid

    return -1

arr1 = [1, 2, 3, 4, 5, 6]
arr2 = [1, 2, 3, 4, 5]
arr3 = [1, 2, 3]
print(arr3, 11, binary_search(arr3, 11))
print(arr3, 2, binary_search(arr3, 2))
print(arr3, 3, binary_search(arr3, 3))
print(arr2, 4, binary_search(arr2, 4))
print(arr2, 5, binary_search(arr2, 5))
print(arr1, 6, binary_search(arr1, 6))