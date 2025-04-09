def is_palindrome(x: int) -> bool:
    str_x = str(x)
    if str_x == str_x[::-1]:
        return True
    return False

