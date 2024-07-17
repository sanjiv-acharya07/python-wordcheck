import nltk
import Levenshtein
import heapq

class BKTreeNode:
    def __init__(self, word):
        self.word = word
        self.children = {}

class BKTree:
    def __init__(self):
        self.root = None

    def add(self, word):
        if self.root is None:
            self.root = BKTreeNode(word)
            return
        current = self.root
        while current:
            k = Levenshtein.distance(current.word, word)
            if k == 0:
                return
            if k in current.children:
                current = current.children[k]
            else:
                new_node = BKTreeNode(word)
                current.children[k] = new_node
                return

    def k_closest_words(self, root, query, k):
        if root is None:
            return []
        closest_words = []
        stack = [root]
        while stack:
            node = stack.pop()
            node_distance = Levenshtein.distance(query, node.word)
            if len(closest_words) < k:
                heapq.heappush(closest_words, (-node_distance, node.word))
            else:
                heapq.heappushpop(closest_words, (-node_distance, node.word))
            for dist, child in node.children.items():
                if abs(dist - node_distance) <= -closest_words[0][0]:
                    stack.append(child)
        return [word for _, word in sorted(closest_words, reverse=True)]








words = nltk.corpus.words
wordnet = nltk.corpus.wordnet
brown = nltk.corpus.brown



words_corpus = list(words.words())
wordnet_corpus = list(wordnet.words())
brown_corpus = list(brown.words())
corpus = words_corpus + wordnet_corpus + brown_corpus
bk_tree = BKTree()
for word in corpus:
    bk_tree.add(word)




def solve(input):
    lines = input.split('\n')
    root = bk_tree.root
    query = lines[0]
    k = int(lines[1])
    closest = bk_tree.k_closest_words(root, query, k)

    return str(closest)


def read_input(path):
    try:
        with open(path, "r") as file:
            return file.read()
    except Exception as e:
        print(e)


def main():
    ##input_output.read_write_input_output(sys.argv[1:], "part1")
    try:
        input_content = read_input("part4/inputs/input0")
        # TODO: Call the appropriate solution method here and assign the result to the output variable
        output = solve(input_content)
        output = str(output) + '\n' + '\n'
        with open("part4/outputs/output0", "w") as file:
            file.write(output)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()


