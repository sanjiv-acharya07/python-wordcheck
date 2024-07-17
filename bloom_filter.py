class BloomFilter:

    def __init__(self, table_size, hash_functions):
        self.table_size = table_size
        self.bit_array = [0] * table_size
        self.hash_functions = hash_functions

    def add(self, element):
        changed_bits = 0
        for hash_function in self.hash_functions:
            hash_value = hash_function(element) % self.table_size
            if self.bit_array[hash_value] == 0:
                self.bit_array[hash_value] = 1
                changed_bits += 1
        return changed_bits

    def query(self, element):
        for hash_function in self.hash_functions:
            hash_value = hash_function(element) % self.table_size
            if self.bit_array[hash_value] == 0:
                return False
        return True

    # Hash functions
    def ascii_sum_hash(element):
        return sum(ord(char) for char in element)

    def jenkins_hash(element):
        hash_value = 0
        for char in element:
            hash_value += ord(char)
            hash_value += (hash_value << 10)
            hash_value ^= (hash_value >> 6)
        hash_value += (hash_value << 3)
        hash_value ^= (hash_value >> 11)
        hash_value += (hash_value << 15)
        return hash_value

    def division_modulo_hash(seed, element):
        prime_list = [31, 37, 41, 43, 47, 53, 59, 61, 67, 71]
        prime = prime_list[seed]
        hash_value = 0
        for i, char in enumerate(element):
            hash_value += ord(char) * (prime ** (i))
            i += 1
        return hash_value

    def fnv1a_hash(seed, element):
        fnv_prime_options = [16777619, 16777633, 16777639, 16777643, 16777669,
                             16777679, 16777681, 16777699, 16777711, 16777721]
        offset_basis = 0x811c9dc5
        fnv_prime = fnv_prime_options[seed]

        hash_value = offset_basis
        for char in element:
            hash_value ^= ord(char)
            hash_value *= fnv_prime
            hash_value &= 0xffffffff
        return hash_value



