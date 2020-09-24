unsorted = [13, 44, 4, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48]


def insertion(arr):

    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1

        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

print(insertion(unsorted))







