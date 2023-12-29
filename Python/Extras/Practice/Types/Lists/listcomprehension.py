#!/usr/bin/env python

# Multi dimensional matrix
numbers = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]
     ]

# Print the Matrix
print(numbers)

# Get the second column values from the matrix

col2 = [row[1] for row in numbers]


# Print the Column 2 values
print(col2)


# Square the numbers
squareIt = [2, 4, 6]

squares = [each ** 2 for each in squareIt]
print(squares)