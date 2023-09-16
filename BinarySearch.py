def BinarySearch(arr, n, k):
    left, right = 0, n - 1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == k:
            return mid
        elif arr[mid] < k:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

print(BinarySearch([1, 2, 3, 4, 5], 5, 4))
print(BinarySearch([11, 22, 33, 44, 55], 5, 445))