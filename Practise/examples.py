# mathematical functions
import math

# Example 1: Square root
print(math.sqrt(25))  # Output: 5.0

# Example 2: Sine of a number (in radians)
print(math.sin(math.pi / 60))  # Output: 1.0

# Example 3: Natural logarithm
print(math.log(0.5))  # Output: ~2.302585
#example 4
print(math.pow(2,3))
# alternatively
print(2**3)
#example 5
print(math.factorial(6))
#built in functions
# eample1
print(len("Joseph kamau"))
# example2
print(type('rat'))
# example3
print(math.prod([1,2,3,4,5,6,7,8,9,10]))
# example4
print(max([2,5,7,9,1,4]))
# User defined functions
# example1
def is_even(num):
    return num%2 == 0
print(is_even(3))
# example2
def Greetings(name):
    return 'Greetings'+name
print(Greetings('Kamau'))
# example3
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

print(is_prime(7))  # Output: True
print(is_prime(10))  # Output: False
