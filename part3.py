import bloom_filter
import re
BloomFilter = bloom_filter.BloomFilter
import nltk.corpus
words = nltk.corpus.words
wordnet = nltk.corpus.wordnet
brown = nltk.corpus.brown


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


words_corpus = list(words.words())
wordnet_corpus = list(wordnet.words())
brown_corpus = list(brown.words())
corpus = words_corpus + wordnet_corpus + brown_corpus
hash_functions = [ascii_sum_hash, jenkins_hash]
hash_functions += [lambda element, i=i: division_modulo_hash(i, element) for i in range(10)]
hash_functions += [lambda element, i=i: fnv1a_hash(i, element) for i in range(10)]
bloom_filter = BloomFilter(18000000, hash_functions)
for word in corpus:
    cleaned_paragraph = ''.join(char if char in "'-" or char.isalpha() else ' ' for char in word)
    bloom_filter.add(cleaned_paragraph.lower())






def solve(input):
    cleaned_paragraph = ''.join(char if char in "'-" or char.isalpha() else ' ' for char in input)
    par_words = cleaned_paragraph.split()

    output = []

    for word in par_words:
        if not bloom_filter.query(word.lower()):
            output.append(word)

    return str(output) + '\n' + '\n'



def read_input(path):
    try:
        with open(path, "r") as file:
            return file.read()
    except Exception as e:
        print(e)


def main():
    ##input_output.read_write_input_output(sys.argv[1:], "part1")
    try:
        input_content = read_input("part3/inputs/input0")
        # TODO: Call the appropriate solution method here and assign the result to the output variable
        output = solve(input_content)
        with open("part3/outputs/output0", "w") as file:
            file.write(output)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()






