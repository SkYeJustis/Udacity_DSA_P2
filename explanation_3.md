# Explanation for Problem 3
-------------------------------------------------

## The huffman encoding algorithm requires N time when building the frequency map, an additional logN is required to create the priority queue to create the binary huffman tree.
## The huffman decoding algorithm requires N time to traverse the length of the data and logN time to traverse the tree.
## The overall time complexity for both operations is O (n * log n).
## The overall space complexity for both operations is O( n )