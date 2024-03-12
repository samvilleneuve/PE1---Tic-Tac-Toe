# PE1---Tic-Tac-Toe
**Python Essentials - Part 1 (Basics)**

**Module 4: Functions, tuples, dictionaries, data processing and exceptions**
**Project "4.7.2.1 PROJECT: Tic-Tac-Toe"**

See [Python Essentials - Part 1 (Basics) on OpenEDG](https://edube.org/study/pe1)

**LAB Objectives**
- perfecting the student's skills in using Python for solving complex problems;
- integrating programming techniques in one program consisting of many various parts.

## Standard grid 3x3

```

>> Enter the size of the game (type ENTER for the default = 3 or type 'exit' to exit game): 

Game starting

Computer plays [5]

+-------+-------+-------+
|       |       |       |
|   1   |   2   |   3   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   4   |   X   |   6   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   7   |   8   |   9   |
|       |       |       |
+-------+-------+-------+

>> Enter a square's number (or 'exit' to exit game): 1
You play [1]
+-------+-------+-------+
|       |       |       |
|   O   |   2   |   3   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   4   |   X   |   6   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   7   |   8   |   9   |
|       |       |       |
+-------+-------+-------+

Computer is thinking...
Random square's number:  1 - Check the tupple (1, 1) in the list of free squares: [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2), (3, 3)]
Random square's number:  8 - Check the tupple (3, 2) in the list of free squares: [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2), (3, 3)] ==> FREE
Computer plays [8]
+-------+-------+-------+
|       |       |       |
|   O   |   2   |   3   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   4   |   X   |   6   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   7   |   X   |   9   |
|       |       |       |
+-------+-------+-------+

>> Enter a square's number (or 'exit' to exit game): 3
You play [3]
+-------+-------+-------+
|       |       |       |
|   O   |   2   |   O   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   4   |   X   |   6   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   7   |   X   |   9   |
|       |       |       |
+-------+-------+-------+

Computer is thinking...
Random square's number:  1 - Check the tupple (1, 1) in the list of free squares: [(1, 2), (2, 1), (2, 3), (3, 1), (3, 3)]
Random square's number:  2 - Check the tupple (1, 2) in the list of free squares: [(1, 2), (2, 1), (2, 3), (3, 1), (3, 3)] ==> FREE
Computer plays [2]
+-------+-------+-------+
|       |       |       |
|   O   |   X   |   O   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   4   |   X   |   6   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   7   |   X   |   9   |
|       |       |       |
+-------+-------+-------+

You lose!

>> Play again? Type 'exit' to exit game or any input to continue playing:
```

## Enter a valid square's number!
```
+-------+-------+-------+
|       |       |       |
|   O   |   2   |   O   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   O   |   X   |   X   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   X   |   X   |   9   |
|       |       |       |
+-------+-------+-------+

>> Enter a square's number (or 'exit' to exit game): 1
You entered the number [1]. Enter a free square's number!
Below are the choices of left positions [row, col]:
 [(1, 2), (3, 3)]
Or left square's number:
 [2, 9]
```

## A big grid 6x6

```
>> Enter the size of the game (type ENTER for the default = 3 or type 'exit' to exit game): 6

Game starting

Computer plays [5]

+--------+--------+--------+--------+--------+--------+
|        |        |        |        |        |        |
|   1    |   2    |   3    |   4    |   X    |   6    |
|        |        |        |        |        |        |
+--------+--------+--------+--------+--------+--------+
|        |        |        |        |        |        |
|   7    |   8    |   9    |   10   |   11   |   12   |
|        |        |        |        |        |        |
+--------+--------+--------+--------+--------+--------+
|        |        |        |        |        |        |
|   13   |   14   |   15   |   16   |   17   |   18   |
|        |        |        |        |        |        |
+--------+--------+--------+--------+--------+--------+
|        |        |        |        |        |        |
|   19   |   20   |   21   |   22   |   23   |   24   |
|        |        |        |        |        |        |
+--------+--------+--------+--------+--------+--------+
|        |        |        |        |        |        |
|   25   |   26   |   27   |   28   |   29   |   30   |
|        |        |        |        |        |        |
+--------+--------+--------+--------+--------+--------+
|        |        |        |        |        |        |
|   31   |   32   |   33   |   34   |   35   |   36   |
|        |        |        |        |        |        |
+--------+--------+--------+--------+--------+--------+

>> Enter a square's number (or 'exit' to exit game):
```