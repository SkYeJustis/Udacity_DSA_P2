import sys
from collections import deque
import unittest
import re

class Node:
    def __init__(self):
        self.letter = None
        self.value = None
        self.left = None
        self.right = None

    def has_left_child(self):
        return self.right != None

    def has_right_child(self):
        return self.left != None

    def get_left_child(self):
        return self.left

    def get_right_child(self):
        return self.right

    def __str__(self):
        return f"< {self.letter} | {self.value} >"

class PriorityQueue:
    def __init__(self):
        self.q = []

    def __str__(self):
        return ' '.join([str(i) for i in self.q])

    def is_empty(self):
        return self.q == []

    def insert(self, node):
        self.q.append(node)

    def pop(self):
        min_index = 0
        for i in range(len(self.q)):
            if self.q[i].value < self.q[min_index].value:
                min_index = i

        if not self.is_empty():
            node = self.q[min_index]
            del self.q[min_index]
            return node

class Queue():
    def __init__(self):
        self.q = deque()

    def enq(self, value):
        self.q.appendleft(value)

    def deq(self):
        if len(self.q) > 0:
            return self.q.pop()
        else:
            return None

    def __len__(self):
        return len(self.q)


class Tree:
    def __init__(self):
        self.root = None
        self.code_map = {}


    def get_root(self):
        return self.root

    def encode_traverse(self):
        self.encode_traverse_helper(self.root, "")


    def encode_traverse_helper(self, node, code):
        if not node:
            return

        if node.letter:
            self.code_map[node.letter] = code
            return

        self.encode_traverse_helper(node.left, code + "0")
        self.encode_traverse_helper(node.right, code + "1")


    def __repr__(self):
        level = 0
        q = Queue()
        visit_order = list()
        node = self.get_root()
        q.enq((node, level))
        while (len(q) > 0):
            node, level = q.deq()
            if node == None:
                visit_order.append(("<empty>", level))
                continue
            visit_order.append((node, level))
            if node.has_left_child():
                q.enq((node.get_left_child(), level + 1))
            else:
                q.enq((None, level + 1))

            if node.has_right_child():
                q.enq((node.get_right_child(), level + 1))
            else:
                q.enq((None, level + 1))

        s = "Tree\n"
        previous_level = -1
        for i in range(len(visit_order)):
            node, level = visit_order[i]
            if level == previous_level:
                s += " || " + str(node)
            else:
                s += "\n" + str(node)
                previous_level = level
        return s


def build_frequency_map(sentence):
    frequency_map = {}
    for l in sentence:
        if l in frequency_map:
            frequency_map[l] += 1
        else:
            frequency_map[l] = 1
    return frequency_map


def build_huffman_tree(frequency_map):
    pq = PriorityQueue()

    # Add letter nodes in Priority Queue
    #print(f"=== Priority Queue ===")
    for data in frequency_map.items():
        node = Node()
        node.value = data[1]
        node.letter = data[0]
        pq.insert(node)
        #print(node)
    #print("====================")

    # Create internal linking nodes / build huffman tree
    while not pq.is_empty():
        node_1 = pq.pop()
        node_2 = pq.pop()

        if node_1 and node_2:
            new_node = Node()
            new_node.value = node_1.value + node_2.value
            new_node.left = node_1
            new_node.right = node_2
            pq.insert(new_node)

    tree = Tree()
    tree.root = node_1 or node_2

    return tree

####################################################################################################################

def huffman_encoding(data):
    assert isinstance(data, str)

    frequency_map = build_frequency_map(data)
    tree = build_huffman_tree(frequency_map)
    tree.encode_traverse()
    # Get encoded
    encoded_data = ""
    for l in data:
        encoded_data += tree.code_map[l]
    return encoded_data, tree


def huffman_decoding(data, tree):
    assert isinstance(data, str) and isinstance(tree, Tree) and bool(re.match('^[01]+$', data))
    decoded_data = ""
    node = tree.get_root()
    for i in data:
        if i == "0":
            node = node.left
        else:
            node = node.right
        if node.letter:
            decoded_data += node.letter
            node = tree.get_root()
    return decoded_data

###################################################################################################################

class Tests_Regular_1(unittest.TestCase):
    def setUp(self):
        self.a_great_sentence = "The bird is the word"

    def tests_regular_1(self):
        #print("The size of the data is: {}\n".format(sys.getsizeof(self.a_great_sentence)))
        #print("The content of the data is: {}\n".format(self.a_great_sentence))

        encoded_data, tree = huffman_encoding(self.a_great_sentence)

        #print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
        #print("The content of the encoded data is: {}\n".format(encoded_data))

        decoded_data = huffman_decoding(encoded_data, tree)

        #print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
        #print("The content of the encoded data is: {}\n".format(decoded_data))

        print(f"Test: Input string is {self.a_great_sentence}")
        # Solution: Decoded string is a_great_sentence
        self.assertTrue(self.a_great_sentence == decoded_data)

        print(f"Test: Size of encoded data vs decoded data")
        # Solution: Non-encoded data should be of greater size for encoded data, due to compression
        self.assertTrue(sys.getsizeof(int(encoded_data, base=2)) < sys.getsizeof(self.a_great_sentence))
        self.assertTrue(sys.getsizeof(int(encoded_data, base=2)) < sys.getsizeof(decoded_data))
        self.assertTrue(sys.getsizeof(decoded_data) == sys.getsizeof(self.a_great_sentence))


class Tests_Regular_2(unittest.TestCase):
    def setUp(self):
        self.a_great_sentence = "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way - in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only."

    def tests(self):

        encoded_data, tree = huffman_encoding(self.a_great_sentence)

        decoded_data = huffman_decoding(encoded_data, tree)

        print(f"Test: Input string is {self.a_great_sentence}")
        # Solution: Decoded string is the same as a_great_sentence
        self.assertTrue(self.a_great_sentence == decoded_data)

        print(f"Test: Size of encoded data vs decoded data")
        # Solution: Non-encoded data should be of greater size for encoded data, due to compression
        self.assertTrue(sys.getsizeof(int(encoded_data, base=2)) < sys.getsizeof(self.a_great_sentence))
        self.assertTrue(sys.getsizeof(int(encoded_data, base=2)) < sys.getsizeof(decoded_data))
        self.assertTrue(sys.getsizeof(decoded_data) == sys.getsizeof(self.a_great_sentence))

class Tests_Irregular_3(unittest.TestCase):
    def setUp(self):
        self.a_great_sentence = 90210

    def tests(self):
        print("Test: Invalid datatype for huffman_encoding")
        # Solution: AssertionError is expected since the input data is not a string
        self.assertRaises(AssertionError, huffman_encoding,  self.a_great_sentence)

class Tests_Irregular_4(unittest.TestCase):
    def setUp(self):
        self.encoded_data = 12343
        self.tree = None

    def tests(self):
        print("Test: Invalid datatype for huffman_decoding")
        # Solution: AssertionError is expected since data != str, tree != Tree object, or data is not completely comprised of 0s and 1s
        self.assertRaises(AssertionError, huffman_decoding, self.encoded_data, self.tree)

"""
References:
    Udacity: Data Structures and Nanodegree Program - 2. Data Structures
"""

if __name__ == "__main__":
    unittest.main()