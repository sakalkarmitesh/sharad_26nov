"""
Write a recursive function, is_palindrome() to find out whether a string is a palindrome or not. The function should return true, if it is a palindrome. Else it should return false. Note- Perform case insensitive operations wherever necessary.
"""

def is_palindrome(word):
    if len(word) <= 1:
        return True

    # Convert the first and last characters to lowercase for case-insensitive comparison
    first_char = word[0].lower()
    last_char = word[-1].lower()
    if first_char != last_char:
        return False

    return is_palindrome(word[1:-1])

# Example usage:
word = "racecar"
result = is_palindrome(word)

if result:
    print("The given word is a Palindrome")
else:
    print("The given word is not a Palindrome")