def get_gamma_rate(list_of_binary: list):
    tally = {}
    no_numbers = len(list_of_binary)
    gamma_rate = ""

    for seq in list_of_binary:
        for i, bit in enumerate(seq):
            if i not in tally:
                tally[i] = 0
            tally[i] += int(bit)

    for key, value in tally.items():
        if value > no_numbers / 2:
            gamma_rate += '1'
        else:
            gamma_rate += '0'

    return gamma_rate


def get_oxygen_rating(list_of_binary: list):
    length_of_binary = len(list_of_binary[0])

    for i in range(length_of_binary):
        list_of_binary = get_dominating_bit_at_index(list_of_binary, i, type='oxygen')

        if len(list_of_binary) == 1:
            return list_of_binary[-1]

    return list_of_binary[-1]


def get_co2_rating(list_of_binary: list):
    length_of_binary = len(list_of_binary[0])

    for i in range(length_of_binary):
        list_of_binary = get_dominating_bit_at_index(list_of_binary, i, type='co2')
        if len(list_of_binary) == 1:
            return list_of_binary[-1]


def get_dominating_bit_at_index(list_of_binary: list, position: int, type: str):
    max_dict = {'1': [], '0': []}

    for number in list_of_binary:
        bit_at_pos = number[position]
        max_dict[bit_at_pos].append(number)  # Store all numbers starting with 1 or 0

    if type == 'oxygen':
        if len(max_dict['1']) >= len(max_dict['0']):
            return max_dict['0']
        else:
            return max_dict['1']
    elif type == 'co2':
        if len(max_dict['1']) >= len(max_dict['0']):
            return max_dict['1']
        else:
            return max_dict['0']


def get_complement(binary_number: str):
    complement = ""
    for bit in binary_number:
        complement += str(1 - int(bit))

    return complement


if __name__ == '__main__':
    with open("/Users/august/PycharmProjects/advent_of_code_2021/inputs/input_day_3.txt") as f:
        list_of_binary = [x for x in f.read().splitlines()]

    gamma_rate = get_gamma_rate(list_of_binary)
    epsilon_rate = get_complement(gamma_rate)

    print(f"Power consumption: {int(gamma_rate, 2) * int(epsilon_rate, 2)}")

    # Part 2
    oxygen_rating = int(get_oxygen_rating(list_of_binary), 2)
    co2_rating = int(get_co2_rating(list_of_binary), 2)

    print(f"Life support rating: {oxygen_rating * co2_rating}")
