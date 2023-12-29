#!/usr/bin/env python

# List of Students
students = ['Mike Tavera', 'Pam Stacy', 'Mike Ferrier', 'William Cartle']

# Student count
print("Number of Studnets : " + str(len(students)))

# Print all Students
print(students[:])

# Add new Student
students.append('Laurel Gini')

# Print all Students
print(students[:])

# Remove the Third Student
students.pop(2)

# Print all Students
print(students[:])

# Extend the List
students.extend(['Teddy Brown', 'Mike T', 'James John', 'Barry Cole'])

# Print all Students
print(students[:])

# Reverse the Students List
students.reverse()

# Print the Reverse Students List
print(students[:])

# Sort the Students List
students.sort()

# Print the Reverse Students List
print(students[:])



