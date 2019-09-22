import unittest

class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name

def helper(user, group):
    if user in group.get_users():
        return True
    elif len(group.get_groups()) != 0:
        for group in group.get_groups():
            return helper(user, group)
    else:
        return False

def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    return helper(user, group)

##################################################################################################################

class GroupTestCase1_NestedUser(unittest.TestCase):
    def setUp(self):
        self.parent = Group("parent")
        self.child = Group("child")
        self.sub_child = Group("subchild")
        self.sub_child_user = "sub_child_user"
        self.sub_child.add_user(self.sub_child_user)
        self.child.add_group(self.sub_child)
        self.parent.add_group(self.child)

    def test_subchild(self):
        print("Test: Check if sub_child_user is in sub_child group")
        # Solution True
        self.assertTrue(is_user_in_group(self.sub_child_user, self.sub_child))

    def test_child(self):
        print("Test: Check if sub_child_user is in child group")
        # Solution True
        self.assertTrue(is_user_in_group(self.sub_child_user, self.child))

    def test_parent(self):
        print("Test: Check if sub_child_user is in parent group")
        # Solution True
        self.assertTrue(is_user_in_group(self.sub_child_user, self.parent))

class GroupTestCase2_PartialNestedUser(unittest.TestCase):
    def setUp(self):
        self.parent = Group("parent")
        self.child = Group("child")
        self.sub_child = Group("subchild")
        self.child_user = "child_user"
        self.child.add_user(self.child_user)
        self.child.add_group(self.sub_child)
        self.parent.add_group(self.child)

    def test_subchild(self):
        print("Test: Check if child_user is in sub_child group")
        # Solution False
        self.assertFalse(is_user_in_group(self.child_user, self.sub_child))

    def test_child(self):
        print("Test: Check if child_user is in child group")
        # Solution True
        self.assertTrue(is_user_in_group(self.child_user, self.child))

    def test_parent(self):
        print("Test: Check if child_user is in parent group")
        # Solution True
        self.assertTrue(is_user_in_group(self.child_user, self.parent))

class GroupTestCase3_NotNestedUser(unittest.TestCase):
    def setUp(self):
        self.parent = Group("parent")
        self.child = Group("child")
        self.sub_child = Group("subchild")
        self.parent_user = "parent_user"
        self.parent.add_user(self.parent_user)
        self.child.add_group(self.sub_child)
        self.parent.add_group(self.child)

    def test_subchild(self):
        print("Test: Check if parent user is in sub_child group")
        # Solution False
        self.assertFalse(is_user_in_group(self.parent_user, self.sub_child))

    def test_child(self):
        print("Test: Check if parent user is in child group")
        # Solution: False
        self.assertFalse(is_user_in_group(self.parent_user, self.child))

    def test_parent(self):
        print("Test: Check if parent user is in parent group")
        # Solution: True
        self.assertTrue(is_user_in_group(self.parent_user, self.parent))

class GroupTestCase4_MixedValues(unittest.TestCase):
    def setUp(self):
        self.parent = Group("parent")
        self.child = Group(1)
        self.sub_child = Group(2)
        self.parent_user = None
        self.parent.add_user(self.parent_user)
        self.child.add_group(self.sub_child)
        self.parent.add_group(self.child)

    def test_subchild(self):
        print("Test: Check if parent user is in sub_child group")
        # Solution False
        self.assertFalse(is_user_in_group(self.parent_user, self.sub_child))

    def test_child(self):
        print("Test: Check if parent user is in child group")
        # Solution: False
        self.assertFalse(is_user_in_group(self.parent_user, self.child))

    def test_parent(self):
        print("Test: Check if parent user is in parent group")
        # Solution: True
        self.assertTrue(is_user_in_group(self.parent_user, self.parent))

if __name__ == '__main__':
    unittest.main()


