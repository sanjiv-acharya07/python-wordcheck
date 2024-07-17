def ascii_sum(string, table_size):
    hash_value = sum(ord(char) for char in string)
    return hash_value % table_size


def jenkins_hash(string, table_size):
    hash_value = 0
    for char in string:
        hash_value += ord(char)
        hash_value += (hash_value << 10)
        hash_value ^= (hash_value >> 6)
    hash_value += (hash_value << 3)
    hash_value ^= (hash_value >> 11)
    hash_value += (hash_value << 15)
    return hash_value % table_size


def division_hash(string, table_size, seed):
    prime_list = [31, 37, 41, 43, 47, 53, 59, 61, 67, 71]
    prime = prime_list[seed]
    hash_value = 0
    for i, char in enumerate(string):
        hash_value += ord(char) * prime ** (i)
        i += 1
    return hash_value % table_size


def fnv1a_hash(string, table_size, seed):
    prime_list = [16777619, 16777633, 16777639, 16777643, 16777669, 16777679, 16777681, 16777699, 16777711, 16777721]
    offset_basis = 0x811c9dc5
    prime = prime_list[seed]
    hash_value = offset_basis
    for char in string:
        hash_value ^= ord(char)
        hash_value *= prime
        hash_value &= 0xffffffff
    return hash_value % table_size


def solve(input):
    new_string = input.split(", ")
    hash_function = ''
    hash_table_size = ''
    seed = ''
    string_val = ''

    if len(new_string) == 4:
        hash_function = new_string[0]
        hash_table_size = int(new_string[1])
        seed = int(new_string[2])
        string_val = new_string[3]
        string_val = string_val.replace('\n', '')
    elif len(new_string) == 3:
        hash_function = new_string[0]
        hash_table_size = int(new_string[1])
        string_val = new_string[2]
        string_val = string_val.replace('\n', '')

    if hash_function == 'ascii_sum':
        return str(ascii_sum(string_val, hash_table_size))

    elif hash_function == 'jenkins':
        return str(jenkins_hash(string_val, hash_table_size))
    elif hash_function == 'division':
        return str(division_hash(string_val, hash_table_size, seed))
    elif hash_function == 'fnv1a':
        return str(fnv1a_hash(string_val, hash_table_size, seed))


def read_input(path):
    try:
        with open(path, "r") as file:
            return file.read()
    except Exception as e:
        print(e)


def main():
    ##input_output.read_write_input_output(sys.argv[1:], "part1")
    try:
        input_content = read_input("part1/inputs/input0")
        # TODO: Call the appropriate solution method here and assign the result to the output variable
        output = solve(input_content)
        with open("part1/output/output0", "w") as file:
            file.write(output)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
