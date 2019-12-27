import time


def bubble_sort(arr: [int]):
    change = True
    while change:
        change = False
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i+1] = arr[i + 1], arr[i]
                change = True

    return arr


start = time.process_time()
print(bubble_sort([3, 5, 2, 12, 2, 4, 6, 7, 8, 2, 4, 2]))
end = time.process_time()
print(end - start)
