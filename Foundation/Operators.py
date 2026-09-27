# Concept: Operator precedence, bitwise manipulation, short-circuit evaluation.
# Challenge: Implement a function is_power_of_two(n) that returns True if an integer n () is a power of 2, and False otherwise. You must use only bitwise operators (no loops, no modulo, no exponentiation, and no math library functions).


n = 128
def _power_of_two(n):
    if(n > 0 and n & (n-1)) == 0:
        return True
    else:
        return False

value = _power_of_two(n)
print(value)