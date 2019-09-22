# Explanation for Problem 4
-------------------------------------------------

## Recursion is used to find the user within a group. The group can also have subgroups.
## The time complexity is O(n*m). The search for the user in a list takes n time. 
## Additional searches after the recursion take m time.
## The space complexity is O(n) where n would be the call stack for each recursive call to another group.