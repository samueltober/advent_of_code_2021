def calculate_position(list_of_instructions: list):
    tally = {}

    for instruction in list_of_instructions:
        direction = instruction.split()[0]
        steps = int(instruction.split()[1])

        if direction not in tally:
            tally[direction] = steps
        else:
            tally[direction] += steps

    return tally


class Submarine:
    def __init__(self, x, y, aim):
        self.x = x
        self.y = y
        self.aim = aim

    def _move_forward(self, horizontal_shift: int):
        self.x += horizontal_shift
        self.y += horizontal_shift * self.aim

    def _update_aim(self, vertical_shift: int):
        self.aim += vertical_shift

    def execute_instructions(self, instruction_list: list):
        for instruction in instruction_list:
            direction = instruction.split()[0]
            steps = int(instruction.split()[1])

            if direction.lower() == 'forward':
                self._move_forward(horizontal_shift=steps)
            elif direction.lower() == 'up':
                self._update_aim(vertical_shift=-steps)
            elif direction.lower() == 'down':
                self._update_aim(vertical_shift=steps)
            else:
                print("Invalid instruction")


if __name__ == '__main__':
    # Read input
    with open("/Users/august/PycharmProjects/advent_of_code_2021/inputs/input_day_2.txt") as f:
        instruction_list = [x for x in f.read().splitlines()]

    # Part 1
    tally = calculate_position(instruction_list)
    horisontal_pos = tally['forward']
    vertical_pos = tally['down'] - tally['up']

    print(f"({horisontal_pos}, {vertical_pos}): {vertical_pos * horisontal_pos}")

    # Part 2
    sub = Submarine(x=0, y=0, aim=0)
    sub.execute_instructions(instruction_list)
    print(f"({sub.x}, {sub.y}): {sub.x * sub.y}")
