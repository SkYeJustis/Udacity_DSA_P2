import unittest

class Node(object):
    """ Double linked node"""
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRU_Cache(object):
    """LRU Cache container utilizing"""
    def __init__(self, capacity):
        # Initialize class variables
        assert isinstance(capacity, int)

        self.capacity = capacity
        self.cache = {}
        self.num_elements = 0

        # Head and Tail endpoints to track nodes
        self.head = Node(None, None)
        self.tail = Node(None, None)

        self.head.next = self.tail
        self.tail.prev = self.head


    def size(self):
        return len(self.cache)

    def _full_capacity(self):
        return self.size() > self.capacity

    def _remove_node(self, node):
        """
        Remove a node from the linked list

        :param node:
        :return:
        """
        previous = node.prev
        next_node = node.next

        previous.next = next_node
        next_node.prev = previous

    # enqueue
    def _enqueue(self, node):
        """
        Add the node at tail

        :param node:
        :return:
        """
        node.prev = self.tail.prev
        node.next = self.tail

        self.tail.prev.next = node
        self.tail.prev = node

    # dequeue
    def _dequeue(self):
        """
        Pop the current head

        :return:
        """
        node = self.head.next
        self._remove_node(node)
        return node

    # re_enqueue
    def _re_enqueue(self, node):
        """
        Move certain node in between to the tail

        :param node:
        :return:
        """
        self._remove_node(node)
        self._enqueue(node)


    def get(self, key):
        """Retrieve item from provided key. Return -1 if nonexistent."""
        if key in self.cache:
            value = self.cache[key].value
            # Re-enqueue to indicate recently used
            self._re_enqueue(self.cache[key])
            return value
        else:
            return -1


    def set(self, key, value):
        """Set the value if the key is not present in the cache.
        If the cache is at capacity remove the oldest item.
        """
        if key not in self.cache:
            node = Node(key, value)
            self.cache[key] = node

            self._enqueue(node)
            self.num_elements += 1

            if self._full_capacity():
                dequeued = self._dequeue()
                del self.cache[dequeued.key]
                self.num_elements -= 1

        else:
            # Overwrite value if the key already exists
            # and re-enqueued to indicate recently used
            self.cache[key] = Node(key, value)
            self._re_enqueue(self.cache[key])

############################################################################################################

class TestCases(unittest.TestCase):
    def setUp(self):
        self.our_cache = LRU_Cache(5)

    def tests_regular(self):
        self.our_cache.set(1, 1)
        self.our_cache.set(2, 2)
        self.our_cache.set(3, 3)
        self.our_cache.set(4, 4)
        self.our_cache.set(5, 5)
        #print(f"Num elements{self.our_cache.num_elements}")
        #print(f"Cache size: {self.our_cache.size()}")

        print("Test: get function to get key: 1, value: 1")
        # Solution: 1
        self.assertTrue(self.our_cache.get(1) == 1)

        print("Test: get function for no present value: key 9")
        # Solution: 9
        self.assertTrue(self.our_cache.get(9) == -1)

        print("Test: get function on a value that should be removed - least recently used entry")
        # Solution: returns -1 because the cache reached it's capacity and 2 was the least recently used entry
        self.our_cache.set(6, 6)
        self.assertTrue(self.our_cache.get(2) == -1)

        print("Test: get function on a value that should be removed - least recently used entry")
        # Solution: returns -1 because the cache reached it's capacity and 3 was the least recently used entry
        self.our_cache.set(7, 7)
        self.assertTrue(self.our_cache.get(3) == -1)


    def tests_irregular(self):
        self.our_cache.set(1, 'one')
        self.our_cache.set(2, 'two')
        self.our_cache.set(3, 'three')
        self.our_cache.set(4, 'four')
        self.our_cache.set(5, 'five')
        #print(f"Num elements{self.our_cache.num_elements}")
        #print(f"Cache size: {self.our_cache.size()}")

        print("Test: get function to get key: 1, value: one")
        # Solution: 1
        self.assertTrue(self.our_cache.get(1) == 'one')

        print("Test: get function for no present value: key 9")
        # Solution: 9
        self.assertTrue(self.our_cache.get(9) == -1)

        print("Test: get function on a value that should be removed - least recently used entry")
        # Solution: returns -1 because the cache reached it's capacity and two was the least recently used entry
        self.our_cache.set(6, 'six')
        self.assertTrue(self.our_cache.get(2) == -1)

        print("Test: get function on a value that should be removed - least recently used entry")
        # Solution: returns -1 because the cache reached it's capacity and three was the least recently used entry
        self.our_cache.set(7, 'seven')
        self.assertTrue(self.our_cache.get(3) == -1)


    def test_edge(self):
        print("Test: Bad capacity value")
        # Solution: Print - Please instantiate with a valid integer.
        self.assertRaises(AssertionError, LRU_Cache, 'x')


if __name__ == '__main__':
    unittest.main()