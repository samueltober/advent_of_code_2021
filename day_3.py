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

    print(int(gamma_rate, 2) * int(epsilon_rate, 2))
