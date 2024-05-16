def prod(num1, num2):
    """Returns the product of two numbers a and b."""
    return num1 * num2


def fact_gen():
    """Generator function that yields the next factorial number."""
    factorial = 1
    num = factorial
    while True:
        factorial = prod(factorial, num)
        yield factorial
        num += 1


# Create a generator instance
factorial_generator = fact_gen()

# Test the generator by printing the first few factorial numbers
print(next(factorial_generator))  # Output: 1
print(next(factorial_generator))  # Output: 2
print(next(factorial_generator))  # Output: 6
print(next(factorial_generator))  # Output: 24
print(next(factorial_generator))  # Output: 120


# Solution
def prod(a, b):
    return a * b


def fact_gen():
    i = 1
    n = i
    while True:
        output = prod(n, i)
        yield output
        i += 1
        n = output
