def bubble_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                # swap
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


# Example usage
numbers = [5, 3, 8, 4, 2]
sorted_numbers = bubble_sort(numbers)
print("Sorted list:", sorted_numbers)
