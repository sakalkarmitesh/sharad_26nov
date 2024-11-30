"""
Problem Statement

Write a python function find_smallest_number() which accepts a number n and returns the smallest number having n divisors. Handle the possible errors in the code written inside the function.
Sample Input
16
Expected Output
120
"""
def find_smallest_number(n):
  if n <= 0:
    raise ValueError("n must be a positive integer")

  num = 1
  divisor_count = 0
  while divisor_count < n:
    num += 1
    divisor_count = 0
    for i in range(1, num + 1):
      if num % i == 0:
        divisor_count += 1

  return num

# Example usage with error handling:
try:
  n = int(input("Enter the number of divisors: "))
  result = find_smallest_number(n)
  print(f"The smallest number having {n} divisors: {result}")
except ValueError as e:
  print(f"Error: {e}")