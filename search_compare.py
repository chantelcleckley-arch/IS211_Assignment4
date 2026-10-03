import random
import time


def sequential_search(a_list, item):
    start_time = time.perf_counter()

    pos = 0
    found = False

    while pos < len(a_list) and not found:
        if a_list[pos] == item:
            found = True
        else:
            pos += 1

    end_time = time.perf_counter()

    return found, end_time - start_time


def ordered_sequential_search(a_list, item):
    start_time = time.perf_counter()

    pos = 0
    found = False
    stop = False

    while pos < len(a_list) and not found and not stop:
        if a_list[pos] == item:
            found = True

        else:
            if a_list[pos] > item:
                stop = True
            else:
                pos += 1

    end_time = time.perf_counter()

    return found, end_time - start_time


def binary_search_iterative(a_list, item):
    start_time = time.perf_counter()

    first = 0
    last = len(a_list) - 1
    found = False

    while first <= last and not found:
        midpoint = (first + last) // 2

        if a_list[midpoint] == item:
            found = True

        else:
            if item < a_list[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1

    end_time = time.perf_counter()

    return found, end_time - start_time


def binary_search_recursive(a_list, item):
    start_time = time.perf_counter()

    def recursive_search(a_list, item):
        if len(a_list) == 0:
            return False

        midpoint = len(a_list) // 2

        if a_list[midpoint] == item:
            return True

        else:
            if item < a_list[midpoint]:
                return recursive_search(a_list[:midpoint], item)
            else:
                return recursive_search(a_list[midpoint + 1:], item)

    found = recursive_search(a_list, item)

    end_time = time.perf_counter()

    return found, end_time - start_time


def main():
    list_sizes = [500, 1000, 5000]
    search_item = 99999999

    for size in list_sizes:

        sequential_total = 0
        ordered_total = 0
        binary_iterative_total = 0
        binary_recursive_total = 0

        for i in range(100):

            # Generate a list of positive integers.
            # The highest possible number is much smaller than 99999999.
            numbers = [
                random.randint(1, 1000000)
                for x in range(size)
            ]

            # Sequential search does not require a sorted list.
            result, time_taken = sequential_search(
                numbers,
                search_item
            )

            sequential_total += time_taken

            # Sort before running the algorithms that require sorted data.
            numbers.sort()

            result, time_taken = ordered_sequential_search(
                numbers,
                search_item
            )

            ordered_total += time_taken

            result, time_taken = binary_search_iterative(
                numbers,
                search_item
            )

            binary_iterative_total += time_taken

            result, time_taken = binary_search_recursive(
                numbers,
                search_item
            )

            binary_recursive_total += time_taken

        sequential_average = sequential_total / 100
        ordered_average = ordered_total / 100
        binary_iterative_average = binary_iterative_total / 100
        binary_recursive_average = binary_recursive_total / 100

        print("\nList size:", size)

        print(
            f"Sequential Search took "
            f"{sequential_average:10.7f} seconds to run, on average"
        )

        print(
            f"Ordered Sequential Search took "
            f"{ordered_average:10.7f} seconds to run, on average"
        )

        print(
            f"Iterative Binary Search took "
            f"{binary_iterative_average:10.7f} seconds to run, on average"
        )

        print(
            f"Recursive Binary Search took "
            f"{binary_recursive_average:10.7f} seconds to run, on average"
        )


if __name__ == "__main__":
    main()


