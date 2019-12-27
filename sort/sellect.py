def sellect_sort(arr: [int]):
    for ind, ele in enumerate(arr):
        min_ind = min(range(ind, len(arr)), key=arr.__getitem__)
        arr[ind], arr[min_ind] = arr[min_ind], ele
    return arr


print(sellect_sort([43, 4, 62, 34, 4, 8, 1, 9,
                    4, 32, 5, 124, 6, 8, 2, 47, 24, 54]))
