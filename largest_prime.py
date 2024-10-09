#!/usr/bin/env python3
"""
Largest Prime Fibonacci Number

Write a program that takes a number as an argument, finds the *Fibonacci* numbers less than that number, and prints the largest prime number in the list. 

	- Use command-line arguments to specify the upper limit 
	- Implement a function to check if a number is prime
	- Import and use the Fibonacci generating function from problem 1 as a module

Task: Find the largest prime Fibonacci number less that 50000
"""

# You're on your own for this one. Good luck!


import fibonnaci
import sys


def number_prime(n):
	for i in range(2,(n//2)+ 1):
		if n%i == 0:
			return False
	return True		


fib_list = fibonnaci.fibonacci_seq(sys.argv[1])
largest_prime_number = 2
for n in fib_list:
	if number_prime(n):
		largest_prime_number = n

print(largest_prime_number)

	

			   



