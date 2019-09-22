

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

"""
References:
    Udacity: Data Structures and Nanodegree Program - 2. Data Structures
"""

if __name__ == '__main__':
    def group_test_case__nested_user():
        parent = Group("parent")
        child = Group("child")
        sub_child = Group("subchild")
        sub_child_user = "sub_child_user"
        sub_child.add_user(sub_child_user)
        child.add_group(sub_child)
        parent.add_group(child)

        print("Test: Check if sub_child_user is in sub_child group")
        # Solution True
        assert is_user_in_group(sub_child_user, sub_child) == True

        print("Test: Check if sub_child_user is in child group")
        # Solution True
        assert is_user_in_group(sub_child_user, child) == True

        print("Test: Check if sub_child_user is in parent group")
        # Solution True
        assert is_user_in_group(sub_child_user, parent) == True


    def group_test_case__partial_nested_user():
        parent = Group("parent")
        child = Group("child")
        sub_child = Group("subchild")
        child_user = "child_user"
        child.add_user(child_user)
        child.add_group(sub_child)
        parent.add_group(child)

        print("Test: Check if child_user is in sub_child group")
        # Solution False
        assert is_user_in_group(child_user, sub_child) == False

        print("Test: Check if child_user is in child group")
        # Solution True
        assert is_user_in_group(child_user, child) == True

        print("Test: Check if child_user is in parent group")
        # Solution True
        assert is_user_in_group(child_user, parent) == True


    def group_test_case__not_nested_user():
        parent = Group("parent")
        child = Group("child")
        sub_child = Group("subchild")
        parent_user = "parent_user"
        parent.add_user(parent_user)
        child.add_group(sub_child)
        parent.add_group(child)

        print("Test: Check if parent user is in sub_child group")
        # Solution False
        assert is_user_in_group(parent_user, sub_child) == False

        print("Test: Check if parent user is in child group")
        # Solution: False
        assert is_user_in_group(parent_user, child) == False

        print("Test: Check if parent user is in parent group")
        # Solution: True
        assert is_user_in_group(parent_user, parent) == True


    def group_test_case__mixed_values():
        parent = Group("parent")
        child = Group(1)
        sub_child = Group(2)
        parent_user = None
        parent.add_user(parent_user)
        child.add_group(sub_child)
        parent.add_group(child)

        print("Test: Check if parent user is in sub_child group")
        # Solution: False
        assert is_user_in_group(parent_user, sub_child) == False

        print("Test: Check if parent user is in child group")
        # Solution: False
        assert is_user_in_group(parent_user, child) == False

        print("Test: Check if parent user is in parent group")
        # Solution: True
        assert is_user_in_group(parent_user, parent) == True


    group_test_case__nested_user()
    group_test_case__partial_nested_user()
    group_test_case__not_nested_user()
    group_test_case__mixed_values()