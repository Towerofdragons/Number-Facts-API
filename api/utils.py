# utils.py (or include these in your views module)
def is_prime(n):
    """Return True if n is a prime number, otherwise False."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect(n):
    """Return True if n is a perfect number, otherwise False."""
    if n < 1:
        return False
    return sum(i for i in range(1, n) if n % i == 0) == n

def digit_sum(n):
    """Return the sum of the digits of n."""
    return sum(int(d) for d in str(abs(n)))

def is_armstrong(n):
    """
    Return True if n is an Armstrong number.
    An Armstrong (or narcissistic) number is one that equals the sum of its digits each raised to the power of the number of digits.
    """
    if n < 0:
        return False
    digits = [int(d) for d in str(n)]
    power = len(digits)
    return sum(d ** power for d in digits) == n
