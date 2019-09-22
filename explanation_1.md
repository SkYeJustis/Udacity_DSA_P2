# Explanation for Problem 1
-------------------------------------------------

## A hash map or python dictionary was used to allow for O(1) get operations. 
## A queue concept was used to keep track of how recently used certain key/value pairs were used when using a set operation.
## A doubly linked node with prev and next references was used as components of the queue and allow for O(1) operations, when adding elements (enqueuing), getting existing elements(dequeuing and re-enqueuing), and removing an element and adding an element when the capacity is reached (dequeuing and enqueuing).
## A doubly linked list concept is used to keep track of the front of the list (next item to dequeue) and the back of the list (most recently used item).
## The time complexity is of the get and set operations is O(1). 
## The space complexity is O(n) as the hash map and queue will increase linearly with each element.