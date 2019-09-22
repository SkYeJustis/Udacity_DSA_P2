# Explanation for Problem 2
-------------------------------------------------

## Recursion is used to explore the main directory and any subdirectories present to find files containing the suffix.
## The time complexity is O( n*m ), given operations performed by find_files_helper would be for n items of the original size of the ./testdir and m items at the depth of subdirectories beyond .testdir.
## The space complexity is O( n*m ), where n is the original size of the ./testdir and m is the depth of subdirectories beyond .testdir.