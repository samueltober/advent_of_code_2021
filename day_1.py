def count_number_of_increases(numbers: list) -> int:
    """Count how many times there is an increase between
       two consecutive numbers in the list"""
    no_increases = 0
    for i in range(1, len(numbers)):
        if numbers[i] > numbers[i - 1]:
            no_increases += 1

    return no_increases


if __name__ == "__main__":
    test_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    test_2 = [1, 1, 1, 1, 1, 1]

    assert count_number_of_increases(test_1) == 9
    assert count_number_of_increases(test_2) == 0

    with open("inputs/input_day_1.txt") as f:
        numbers = [int(x) for x in f.read().splitlines()]
        print(count_number_of_increases(numbers))