##0x01. Lockboxes
You have n number of locked boxes in front of you. Each box is numbered sequentially from 0 to n - 1 and each box may contain keys to the other boxes.

Write a method that determines if all the boxes can be opened

# canUnlockAll Function

Prototype: 
- def canUnlockAll(boxes)

Input:
- boxes is a list of lists

Rule:
- A key with the same number as a box opens that box

Assumption:
- You can assume all keys will be positive integers
- There can be keys that do not have boxes

Initial State:
- The first box boxes[0] is unlocked

Output:
- Return True if all boxes can be opened, else return False
