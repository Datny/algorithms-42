unsorted = [10, 3, 1, 120, 99, 4, 12, 39, 7, 7]


def bubble_sort(arr):
    index, swaps = 0, 0
    length = len(arr)

    while True:

        #Swap elements
        if arr[index] > arr[index+1]:
            temp = arr[index+1]
            arr[index+1] = arr[index]
            arr[index] = temp
            swaps += 1
        index += 1

        #Exit if there was no swaps in whole array
        if index == length - 1 and not swaps:
            return arr

        #Reset index to do another loop
        if index == length - 1:
            index, swaps = 0, 0




print(bubble_sort(unsorted))