def bubble_sort(arr: list[int]) -> list[int]:
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


if __name__ == "__main__":
    lst = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print("Sorted list:", bubble_sort(lst))

    lst = [1, 2, 3, 4, 5, 6]
    print("Sorted list:", bubble_sort(lst))

    lst = [4, 2, -3, 12, 4, 1, -5, 6, 0, 12]
    print("Sorted list:", bubble_sort(lst))
