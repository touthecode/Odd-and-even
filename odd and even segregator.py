# The program should open a file named "integer.txt" which contains 20 integers
# The program will then read the text file then create 2 text files namely "odd.txt" and "even.txt"
# "odd.txt" will then contain odd numbers while "even.txt" shall contain even numbers both coming from the numbers in "integer.txt"

# Read the file containing the 20 integers.
import sys
print(sys.path)

with open("C:\Users\Tou\Desktop\School\OOP\Python Stuff\Odd and Even\integer.txt") as int_file:
    numbers = int_file.readlines()

with open("C:\Users\Tou\Desktop\School\OOP\Python Stuff\Odd and Even\odd.txt") as output_odd, open("C:\Users\Tou\Desktop\School\OOP\Python Stuff\Odd and Even\even.txt") as output_even:
    for line in numbers:
        int_line = int(line)
