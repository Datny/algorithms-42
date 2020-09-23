unsorted = [3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48]


def selection(arr):
    for i in range(len(arr)):
        min_idx = i

        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


print(selection(unsorted))
