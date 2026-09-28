import time


def insertion_sort(arr: list[int]) -> list[int]:
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
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
        sorted_lst = insertion_sort(lst.copy())
        end_time = time.perf_counter()

        print("Sorted list:  ", sorted_lst)
        print(f"Execution time: {end_time - start_time:.8f} seconds\n")
