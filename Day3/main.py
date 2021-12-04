from util.fileutil import read_file_to_string_list


def part1() -> None:
    vals = read_file_to_string_list("data.txt")
    size = len(vals)
    col_count = len(vals[0])
    bits = [0] * col_count
    for row in vals:
        for i, bit in enumerate(row):
            bits[i] += int(bit)

    # Binary strings
    gamma_bin = ""
    epsilon_bin = ""
    for bit in bits:
        if bit >= size/2:
            gamma_bin += "1"
            epsilon_bin += "0"
        else:
            gamma_bin += "0"
            epsilon_bin += "1"

    # Convert binary strings to integers
    gamma = int(gamma_bin, 2)
    epsilon = int(epsilon_bin, 2)

    print(f"Gamma: {gamma}, epsilon: {epsilon}, product: {gamma*epsilon}")


def part2() -> None:
    vals = read_file_to_string_list("data.txt")
    col_count = len(vals[0])

    # Oxygen processing
    current_vals = vals.copy()
    for curr_bit in range(col_count):
        current_bit_sum = 0
        if len(current_vals) == 1:
            break
        size = len(current_vals)
        for row in current_vals:
            current_bit_sum += int(row[curr_bit])
        freq_bit = 0
        if current_bit_sum >= size/2:
            freq_bit = 1
        new_vals = []
        for val in current_vals:
            if int(val[curr_bit]) == freq_bit:
                new_vals.append(val)
        current_vals = new_vals
    oxygen_rate = int(current_vals[0], 2)

    # CO2 processing
    current_vals = vals.copy()
    for curr_bit in range(col_count):
        current_bit_sum = 0
        if len(current_vals) == 1:
            break
        size = len(current_vals)
        for row in current_vals:
            current_bit_sum += int(row[curr_bit])
        freq_bit = 1
        if current_bit_sum >= size / 2:
            freq_bit = 0
        new_vals = []
        for val in current_vals:
            if int(val[curr_bit]) == freq_bit:
                new_vals.append(val)
        current_vals = new_vals
    co2_rate = int(current_vals[0], 2)
    print(f"Oxygen processing: {oxygen_rate}, CO2 processing: {co2_rate}, product: {oxygen_rate*co2_rate}")


if __name__ == "__main__":
    part1()
    part2()