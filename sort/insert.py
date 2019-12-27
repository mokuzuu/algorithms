import sys
sys.setrecursionlimit(10 ** 7)


def insert_sort_without_binary_search(arr):
    for i in range(1, len(arr)):
        j = i - 1
        ele = arr[i]
        while arr[j] > ele and j >= 0:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j+1] = ele
    return arr


# Insert search with binary search
def binary_search(arr, low, hig, ele):
    if low == hig:
        if arr[low] > ele:
            return low
        else:
            return low + 1
    elif low > hig:
        return low

    mid = (low + hig) // 2
    if arr[mid] < ele:
        return binary_search(arr, mid+1, hig, ele)
    elif arr[mid] > ele:
        return binary_search(arr, low, mid-1, ele)
    else:
        return mid


def insert_sort_bin(arr):
    for i in range(1, len(arr)):
        ele = arr[i]

        ind = binary_search(arr, 0, i - 1, ele)
        arr[:] = arr[:ind]+[ele]+arr[ind:i]+arr[i+1:]
    return arr


print(insert_sort_bin([1, 2, 2, 13, 31, 5321, 23, 3431, 32, 6, 32, 3, 15]))
