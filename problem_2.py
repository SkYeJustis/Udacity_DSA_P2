import os


def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    if isinstance(suffix, str) and isinstance(path, str):
        return find_files_helper(suffix, path, os.listdir(path), [])
    else:
        return []

def find_files_helper(suffix, path_prefix, path_list, result):

    # Base case - if the path_list is empty OR the path list has completed iteration
    if len(path_list) == 0:
        return result

    for path in path_list:
        current_path = f"{path_prefix}/{path}"
        if os.path.isfile(current_path):
            if current_path.endswith(suffix) and suffix != '':
                result.append(current_path)
        else:
            result = find_files_helper(suffix, current_path, os.listdir(current_path), result)

    return result

"""
References:
    Udacity: Data Structures and Nanodegree Program - 2. Data Structures
"""

if __name__ == '__main__':

    def test_case_1():
        print(" Using files from 'testdir' to find all .c files ")
        # Solution: ['./testdir/subdir1/a.c', './testdir/t1.c', './testdir/subdir5/a.c', './testdir/subdir3/subsubdir1/subsubsubdir1/c.c', './testdir/subdir3/subsubdir1/b.c']
        assert sorted(find_files('.c', './testdir')) == sorted(['./testdir/subdir1/a.c', './testdir/t1.c',
                                                           './testdir/subdir5/a.c',
                                                           './testdir/subdir3/subsubdir1/subsubsubdir1/c.c',
                                                           './testdir/subdir3/subsubdir1/b.c'])

    def test_case_2():
        print(" Using files from 'testdir' to find all .gitkeep files ")
        # Solution: ['./testdir/subdir4/.gitkeep', './testdir/subdir2/.gitkeep']
        assert sorted(find_files('.gitkeep', './testdir')) == sorted(['./testdir/subdir4/.gitkeep', './testdir/subdir2/.gitkeep'])

    def test_case_3():
        print(" Using files from 'testdir' to find all .h files ")
        # Solution: ['./testdir/subdir1/a.h', './testdir/t1.h', './testdir/subdir5/a.h', './testdir/subdir3/subsubdir1/subsubsubdir1/c.h', './testdir/subdir3/subsubdir1/b.h']
        assert sorted(find_files('.h', './testdir')) == sorted(['./testdir/subdir1/a.h',
                                                                           './testdir/t1.h',
                                                                           './testdir/subdir5/a.h',
                                                                           './testdir/subdir3/subsubdir1/subsubsubdir1/c.h',
                                                                           './testdir/subdir3/subsubdir1/b.h'])

    def test_case_4():
        print(" Adding bad input: None as suffix ")
        # Solution: []
        assert find_files(None, './testdir') == []

    def test_case_5():
        print(" Adding bad input: None as path ")
        # Solution: []
        assert find_files('.c', None) == []

    def test_case_6():
        print(" Adding bad input: Empty string as path ")
        # Solution: []
        assert find_files('', './testdir') == []

    def test_case_7():
        print(" Adding bad input: bad type - number - as suffix ")
        # Solution: []
        assert find_files(10182028, './testdir') == []

    def test_case_8():
        print(" Adding bad input: bad type - number - as path ")
        # Solution: []
        assert find_files('.c', 123456778) == []


    test_case_1()
    test_case_2()
    test_case_3()
    test_case_4()
    test_case_5()
    test_case_6()
    test_case_7()
    test_case_8()