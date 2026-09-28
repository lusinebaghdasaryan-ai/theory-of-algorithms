import time


def heapify(arr: list[int], n: int, i: int) -> None:
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    # If left child exists and is greater than root
    if left < n and arr[left] > arr[largest]:
        largest = left

    # If right child exists and is greater than largest so far
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If largest is not root, swap and continue heapifying
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap_sort(arr: list[int]) -> list[int]:
    n = len(arr)

    # Build a max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements one by one
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Swap
        heapify(arr, i, 0)

    return arr


if __name__ == "__main__":
    test_lists = [
        [54, 26, 93, 17, 77, 31, 44, 55, 20],
        [1, 2, 3, 4, 5, 6],
        [4, 2, -3, 12, 4, 1, -5, 6, 0, 12]
    ]

    for idx, lst in enumerate(test_lists, 1):
        print(f"--- Test {idx} ---")
        print("Original:", lst)

        start_time = time.perf_counter()
        sorted_lst = heap_sort(lst.copy())
        end_time = time.perf_counter()

        print("Sorted list:  ", sorted_lst)
        print(f"Execution time: {end_time - start_time:.8f} seconds\n")
