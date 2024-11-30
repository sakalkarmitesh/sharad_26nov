"""
Problem Statement

Given a number n, write a program to find the sum of the largest prime factors of each of nine consecutive numbers starting from n. g(n) = f(n) + f(n+1)+f(n+2)+f(n+3) + f(n+4) + f(n+5) + f(n+6) + f(n+7) + f(n+8) where, g(n) is the sum and f(n) is the largest prime factor of n

For example, g(10)=f(10)+f(11)+f(12)+f(13)+f(14)+f(15)+f(16)+f(17)+f(18) 5+11+3+13+7+5+2+17+3 =66
"""
def find_factors(num):

  factors = []
  for i in range(1, int(num**0.5) + 1):
    if num % i == 0:
      factors.append(i)
      if num // i != i:
        factors.append(num // i)
  return factors

def is_prime(num):
  if num <= 1:
    return False
  for i in range(2, int(num**0.5) + 1):
    if num % i == 0:
      return False
  return True

def find_largest_prime_factor(num):
  factors = find_factors(num)
  largest_prime = 0
  for factor in factors:
    if is_prime(factor) and factor > largest_prime:
      largest_prime = factor
  return largest_prime

def find_g(num):

  sum_of_factors = 0
  for i in range(num, num + 9):
    sum_of_factors += find_largest_prime_factor(i)
  return sum_of_factors

# Example usage:
n = 10
result = find_g(n)
print(result)