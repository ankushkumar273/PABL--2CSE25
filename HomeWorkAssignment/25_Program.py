def is_palindrome(num):
    original = num
    rev = 0

    while num > 0:
        rev = rev * 10 + num % 10
        num //= 10

    return rev == original

def all_palindrome(arr):
    for num in arr:
        if not is_palindrome(num):
            return False
    return True