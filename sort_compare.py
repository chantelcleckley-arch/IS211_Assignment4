import random
import time


def insertion_sort(a_list):
    start_time = time.perf_counter()

    for index in range(1, len(a_list)):
        current_value = a_list[index]
        position = index

        while position > 0 and a_list[position - 1] > current_value:
            a_list[position] = a_list[position - 1]
            position = position - 1

        a_list[position] = current_value

    end_time = time.perf_counter()

    return end_time - start_time


def gap_insertion_sort(a_list, start, gap):
    for i in range(start + gap, len(a_list), gap):
        current_value = a_list[i]
        position = i

        while position >= gap and a_list[position - gap] > current_value:
            a_list[position] = a_list[position - gap]
            position = position - gap

        a_list[position] = current_value


def shell_sort(a_list):
    start_time = time.perf_counter()

    sublist_count = len(a_list) // 2

    while sublist_count > 0:
        for start_position in range(sublist_count):
            gap_insertion_sort(
                a_list,
                start_position,
                sublist_count
            )

        sublist_count = sublist_count // 2

    end_time = time.perf_counter()

    return end_time - start_time


def python_sort(a_list):
    start_time = time.perf_counter()

    a_list.sort()

    end_time = time.perf_counter()

    return end_time - start_time


def main():
    list_sizes = [500, 1000, 5000]

    for size in list_sizes:

        insertion_total = 0
        shell_total = 0
        python_total = 0

        for i in range(100):
            numbers = [
                random.randint(1, 1000000)
                for x in range(size)
            ]

            insertion_list = numbers.copy()
            shell_list = numbers.copy()
            python_list = numbers.copy()

            insertion_total += insertion_sort(insertion_list)
            shell_total += shell_sort(shell_list)
            python_total += python_sort(python_list)

        insertion_average = insertion_total / 100
        shell_average = shell_total / 100
        python_average = python_total / 100

        print("\nList size:", size)

        print(
            f"Insertion Sort took "
            f"{insertion_average:10.7f} seconds to run, on average"
        )

        print(
            f"Shell Sort took "
            f"{shell_average:10.7f} seconds to run, on average"
        )

        print(
            f"Python Sort took "
            f"{python_average:10.7f} seconds to run, on average"
        )


if __name__ == "__main__":
    main()