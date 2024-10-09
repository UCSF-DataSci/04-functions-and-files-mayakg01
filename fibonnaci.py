#!/usr/bin/env python3
"""
Fibonacci Sequence

Create a program that generates Fibonacci numbers less than a limit and writes them to a file. The _Fibonacci_ sequence is a sequence in which each number is the sum of the two preceding ones: 

`0, 1, 1 (0+1), 2 (1+1), 3 (2+1), 5 (3+2), ...`

	- Use a function to generate Fibonacci numbers as a list
	- Use `with` statements for file operations
	- Handle potential file I/O errors with `try`/`except`
	- Use command-line arguments (via `argparse`) to specify the upper limit and output file name

Task: Generate the Fibonacci numbers less than 100 and write them to `fibonacci_100.txt`
"""

def fibonacci_seq(limit = 100):
	fibonacci_nums = [0,1]
	max_number = 1

	while max_number < int(limit):
		n= fibonacci_nums[-1] + fibonacci_nums[-2]
		max_number = n
		if max_number >= int(limit):
			return fibonacci_nums
		fibonacci_nums.append(n)
		
	return fibonacci_nums



if __name__ == "__main__":
	with open('fibonacci_100.txt', 'w') as file:
		fib_list = fibonacci_seq(100)
		file.write('0, 1, ')
		for i in range(2, len(fib_list)):
			file.write(str(fib_list[i]) + ' (' + str(fib_list[i-2]) + '+' + str(fib_list[i-1]) + '), ')
	
	# Do stuff here
    
    
    
    