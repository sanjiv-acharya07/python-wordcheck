# python-wordcheck
## Part 1
Part one utilizes four different hash functions to form a table and store a word. These functions are ASCII Sum, Jenkins Hash, Division Hash, and FNV1A Hash. For the ASCII and Jenkins functions, the input will contain just the hash function, the string, and the table size. For Division Hash and FNV1A Hash, the input will contain everything stated previously but also a seed. The order will be this separated by a comma in the file: hash function, table size, seed (if needed), string. The output will be the hash value mod table size, or in other words the spot in the hash table where the word is stored.

## Part 2
Part two utilizes the bloom filter created in the bloom_filter.py class. This part recieves an input of table size and a list of strings and uses the bloom filter to store them. The hash functions of the bloom filter are the 22 variations of the hash functions in part one. The bloom filter runs each hash function for each word and keeps track of the number of bits changed in the bloom filter (this is also the number of hash functions had a free spot to store the string). Once the program is finished running, the output will contain a list of the number of hash functions that store each word. The input of this part will be the same as the file in part2/inputs, but feel free to change the words and table size.

## Part 3
