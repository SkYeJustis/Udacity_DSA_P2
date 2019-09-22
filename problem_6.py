import unittest

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

def union(llist_1, llist_2):
    """
    :param llist_1:
    :param llist_2:
    :return: llist_result
    """
    if llist_1.size() == 0:
        return llist_2
    elif llist_2.size() == 0:
        return llist_1

    llist_result = LinkedList()
    membership = set()

    node = llist_1.head
    while node:
        if node.value not in membership:
            membership.add(node.value)
            llist_result.append(node.value)
        node = node.next

    node = llist_2.head
    while node:
        if node.value not in membership:
            membership.add(node.value)
            llist_result.append(node.value)
        node = node.next

    return llist_result

def intersection(llist_1, llist_2):
    """
    :param llist_1:
    :param llist_2:
    :return: llist_result
    """
    if llist_1.size() == 0 or  llist_2.size() == 0:
        return None
    llist_result = LinkedList()
    membership = set()

    node = llist_1.head
    while node:
        membership.add(node.value)
        node = node.next

    node = llist_2.head
    while node:
        if node.value in membership:
            llist_result.append(node.value)
        node = node.next

    return llist_result

#####################################################################################################################

class Test_Case_1(unittest.TestCase):
    def setUp(self):
        self.linked_list_1 = LinkedList()
        self.linked_list_2 = LinkedList()

        element_1 = [1, 2, 3, 4, 5]
        element_2 = [3, 4, 5, 6, 7]

        for i in element_1:
            self.linked_list_1.append(i)

        for i in element_2:
            self.linked_list_2.append(i)

    def test(self):
        print("Union for linked lists containing [1, 2, 3, 4, 5] and [3, 4, 5, 6, 7]")
        # Solution: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 ->
        test_union = union(self.linked_list_1, self.linked_list_2)
        answer = []
        node = test_union.head
        while node:
            answer.append(node.value)
            node = node.next
        self.assertTrue( answer == [1,2,3,4,5,6,7])

        print("Instersection for linked lists containing [1, 2, 3, 4, 5] and [3, 4, 5, 6, 7]")
        # Solution: 3 -> 4 -> 5 ->
        test_intersection = intersection(self.linked_list_1, self.linked_list_2)
        answer = []
        node = test_intersection.head
        while node:
            answer.append(node.value)
            node = node.next
        self.assertTrue(answer == [3,4,5])


class Test_Case_2(unittest.TestCase):
    def setUp(self):
        # Duplicate values
        self.linked_list_1 = LinkedList()
        self.linked_list_2 = LinkedList()

        element_1 = [3, 2, 4, 35, 6, 65, 6, 6, 4, 3, 21]
        element_2 = [6, 32, 4, 9, 6, 1, 11, 21, 1]

        for i in element_1:
            self.linked_list_1.append(i)
        for i in element_2:
            self.linked_list_2.append(i)

    def test(self):
        print("Union for linked lists containing [3, 2, 4, 35, 6, 65, 6, 4, 3, 21] and [6, 32, 4, 9, 6, 1, 11, 21, 1]")
        # Solution: 3 -> 2 -> 4 -> 35 -> 6 -> 65 -> 21 -> 32 -> 9 -> 1 -> 11
        test_union = union(self.linked_list_1, self.linked_list_2)
        answer = []
        node = test_union.head
        while node:
            answer.append(node.value)
            node = node.next
        self.assertTrue(answer==[3,2,4,35,6,65,21,32,9,1,11])

        print("Intersection for linked list containing [3, 2, 4, 35, 6, 65, 6, 4, 3, 21] and [6, 32, 4, 9, 6, 1, 11, 21, 1]")
        # Solution: 6 -> 4
        test_intersection = intersection(self.linked_list_1, self.linked_list_2)
        answer = []
        node = test_intersection.head
        while node:
            answer.append(node.value)
            node = node.next
        self.assertTrue(answer==[6,4,6,21])

class Test_Case_3(unittest.TestCase):
    def setUp(self):
        self.linked_list_1 = LinkedList()
        self.linked_list_2 = LinkedList()

        element_1 = ['x', 'y', 'z']
        element_2 = ['x', 'j', 'k']

        for i in element_1:
            self.linked_list_1.append(i)
        for i in element_2:
            self.linked_list_2.append(i)

    def test(self):
        print("Union for linked lists containing ['x', 'y', 'z'] and ['x', 'j', 'k'] ")
        # Solution: x -> y -> z -> j -> k
        test_union = union(self.linked_list_1, self.linked_list_2)
        answer = []
        node = test_union.head
        while node:
            answer.append(node.value)
            node = node.next
        self.assertTrue(answer==['x', 'y', 'z', 'j', 'k'])

        print("Intersection for linked lists containing ['x', 'y', 'z'] and ['x', 'j', 'k'] ")
        # Solution: x
        test_intersection = intersection(self.linked_list_1, self.linked_list_2)
        answer = []
        node = test_intersection.head
        while node:
            answer.append(node.value)
            node = node.next
        self.assertTrue(answer==['x'])

class Test_Case_4(unittest.TestCase):
    # Mixed values
    def setUp(self):
        self.linked_list_1 = LinkedList()
        self.linked_list_2 = LinkedList()

        element_1 = ['x',  None, 'z', 1, 3]
        element_2 = ['x', 'j', 'k', None, 1, 2]

        for i in element_1:
            self.linked_list_1.append(i)
        for i in element_2:
            self.linked_list_2.append(i)

    def test(self):
        print("Union for linked lists containing ['x',  None, 'z', 1, 3] and ['x', 'j', 'k', None, 1, 2] ")
        # Solution: x -> None -> z -> 1 -> 3 -> j -> k -> 2
        test_union = union(self.linked_list_1, self.linked_list_2)
        answer = []
        node = test_union.head
        while node:
            answer.append(node.value)
            node = node.next
        self.assertTrue(answer == ['x', None, 'z', 1, 3, 'j', 'k', 2])

        print("Intersection for linked lists containing ['x',  None, 'z', 1, 3] and ['x', 'j', 'k', None, 1, 2] ")
        # Solution: x -> None -> 1
        test_intersection = intersection(self.linked_list_1, self.linked_list_2)
        answer = []
        node = test_intersection.head
        while node:
            answer.append(node.value)
            node = node.next
        self.assertTrue(answer == ['x', None, 1])


if __name__ == '__main__':
    unittest.main()