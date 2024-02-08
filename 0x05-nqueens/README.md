# N Queens Solver

- **Problem Description:**
  The N queens puzzle is the challenge of placing N non-attacking queens on an N×N chessboard.

- **Usage:**


- **Error Handling:**
- If the user called the program with the wrong number of arguments:
  ```
  Usage: nqueens N
  ```
  followed by a new line, and exit with the status 1.
- If N is not an integer:
  ```
  N must be a number
  ```
  followed by a new line, and exit with the status 1.
- If N is smaller than 4:
  ```
  N must be at least 4
  ```
  followed by a new line, and exit with the status 1.

- **Output:**
- The program should print every possible solution to the problem, one solution per line.
- Solutions should be formatted as follows:
  ```
  Solution: [1, 3, 0, 2]
  ```
- You don’t have to print the solutions in a specific order.

- **Constraints:**
- You are only allowed to import the sys module.
