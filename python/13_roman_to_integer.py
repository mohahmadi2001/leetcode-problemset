def roman_to_int(s: str) -> int:
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
             'C': 100, 'D': 500, 'M': 1000}
    total = 0
    for i in range(len(s) - 1):
        if roman[s[i]] < roman[s[i + 1]]:
            total -= roman[s[i]]
        else:
            total += roman[s[i]]
    return total + roman[s[-1]]

def roman_to_int_2(s: str) -> int:
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
             'C': 100, 'D': 500, 'M': 1000}
    total = 0
    pre_value = 0
    for char in reversed(s):
        value = roman[char]
        if value < pre_value:
            total -= value
        else:
            total += value
        pre_value = value
    return total
