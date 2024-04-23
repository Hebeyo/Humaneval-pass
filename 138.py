
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    for i in range(1, n):
        for j in range(1, n):
            for k in range(1, n):
                for l in range(1, n):
                    if i + j + k + l == n:
                        if i % 2 == 0 and j % 2 == 0 and k % 2 == 0 and l % 2 == 0:
                            return True
    return False
def check(candidate):
    assert candidate(4) == False
    assert candidate(6) == False
    assert candidate(8) == True
    assert candidate(10) == True
    assert candidate(11) == False
    assert candidate(12) == True
    assert candidate(13) == False
    assert candidate(16) == True
'''
Standard answer: 
    return n%2 == 0 and n >= 8
'''
check(is_equal_to_sum_even)
