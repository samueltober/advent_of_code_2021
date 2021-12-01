def count_number_of_increases(numbers: list) -> int:
    """Count how many times there is an increase between
       two consecutive numbers in the list
    """
    no_increases = 0
    for i in range(1, len(numbers)):
        if numbers[i] > numbers[i - 1]:
            no_increases += 1

    return no_increases


def get_sliding_window_sums(numbers: list, window_size: int) -> list:
    """Runs a sliding window of size window_size over list, sums all number in window,
       and returns list of these sums
    """
    sliding_window_sums = []
    for i in range(len(numbers) - window_size + 1):
        window_sum = sum(numbers[i:i+window_size])
        sliding_window_sums.append(window_sum)

    return sliding_window_sums


if __name__ == "__main__":
    test_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    test_2 = [1, 1, 1, 1, 1, 1]

    assert count_number_of_increases(test_1) == 9
    assert count_number_of_increases(test_2) == 0
    assert get_sliding_window_sums(test_1, 3) == [6, 9, 12, 15, 18, 21, 24, 27]
    assert get_sliding_window_sums(test_2, 3) == [3, 3, 3, 3, 3, 3]

    with open("inputs/input_day_1.txt") as f:
        numbers = [int(x) for x in f.read().splitlines()]

    print(count_number_of_increases(numbers))
    window_sums = get_sliding_window_sums(numbers, window_size=3)
    print(count_number_of_increases(window_sums))
