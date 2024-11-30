"""Problem Statement

A 10-substring of a number is a substring of its digits that sum up to 10.
For example, the 10-substrings of the number 3523014 are: 3523014, 3523014, 3523014, 3523014
Write a python function, find_ten_substring(num str) which accepts a string and returns the list of 10-substrings of that string.
Handle the possible errors in the code written inside the function.

Sample Input
3523014
Expected Output
['5230', '23014', '523', '352']"""
def find_ten_substrings(num_str):

    if not num_str.isdigit():
        raise ValueError("Input must be a string of digits")

    ten_substrings = []
    for i in range(len(num_str)):
        curr_sum = 0
        j = i
        while j < len(num_str) and curr_sum <= 10:
            curr_sum += int(num_str[j])
            if curr_sum == 10:
                ten_substrings.append(num_str[i:j+1])
            j += 1

    return ten_substrings

# Example usage:
num_str = "3523014"
result = find_ten_substrings(num_str)
print(result)