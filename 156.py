
def int_to_mini_roman(number):
    """
    Given a positive integer, obtain its roman numeral equivalent as a string,
    and return it in lowercase.
    Restrictions: 1 <= num <= 1000

    Examples:
    >>> int_to_mini_roman(19) == 'xix'
    >>> int_to_mini_roman(152) == 'clii'
    >>> int_to_mini_roman(426) == 'cdxxvi'
    """
    # Write your code here
    roman = ''
    while number > 0:
        if number >= 1000:
            roman += 'm'
            number -= 1000
        elif number >= 900:
            roman += 'cm'
            number -= 900
        elif number >= 500:
            roman += 'd'
            number -= 500
        elif number >= 400:
            roman += 'cd'
            number -= 400
        elif number >= 100:
            roman += 'c'
            number -= 100
        elif number >= 90:
            roman += 'xc'
            number -= 90
        elif number >= 50:
            roman += 'l'
            number -= 50
        elif number >= 40:
            roman += 'xl'
            number -= 40
        elif number >= 10:
            roman += 'x'
            number -= 10
        elif number >= 9:
            roman += 'ix'
            number -= 9
        elif number >= 5:
            roman += 'v'
            number -= 5
        elif number >= 4:
            roman += 'iv'
            number -= 4
        elif number >= 1:
            roman += 'i'
            number -= 1
    return roman
def check(candidate):

    # Check some simple cases
    assert candidate(19) == 'xix'
    assert candidate(152) == 'clii'
    assert candidate(251) == 'ccli'
    assert candidate(426) == 'cdxxvi'
    assert candidate(500) == 'd'
    assert candidate(1) == 'i'
    assert candidate(4) == 'iv'
    assert candidate(43) == 'xliii'
    assert candidate(90) == 'xc'
    assert candidate(94) == 'xciv'
    assert candidate(532) == 'dxxxii'
    assert candidate(900) == 'cm'
    assert candidate(994) == 'cmxciv'
    assert candidate(1000) == 'm'

    # Check some edge cases that are easy to work out by hand.
    assert True

'''
Standard answer: 
    num = [1, 4, 5, 9, 10, 40, 50, 90,  
           100, 400, 500, 900, 1000] 
    sym = ["I", "IV", "V", "IX", "X", "XL",  
           "L", "XC", "C", "CD", "D", "CM", "M"] 
    i = 12
    res = ''
    while number: 
        div = number // num[i] 
        number %= num[i] 
        while div: 
            res += sym[i] 
            div -= 1
        i -= 1
    return res.lower()
'''
check(int_to_mini_roman)
