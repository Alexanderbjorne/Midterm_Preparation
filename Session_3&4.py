# Session 3 & 4 - Python Fundamentals & Git Version Control

# 1. Checking Python Object Types
x = 5
y = 3.14
print(f"x is of type {type(x)}, y is of type {type(y)}")

# 2. Basic Arithmetic Operations
a, b = 10, 3
print(f"Addition: {a + b}")
print(f"Subtraction: {a - b}")
print(f"Multiplication: {a * b}")
print(f"Division: {a / b}")
print(f"Integer Division: {a // b}")
print(f"Modulus: {a % b}")
print(f"Exponentiation: {a ** b}")

# 3. Boolean Operations
print(f"True AND False: {True and False}")
print(f"True OR False: {True or False}")
print(f"NOT True: {not True}")

# 4. Git Commands (as comments)
"""
# Git Basic Commands
git init          # Initialize a new Git repository
git clone <URL>   # Clone an existing repository
git add <file>    # Stage changes
git commit -m "Message"  # Save changes
git push origin main  # Upload changes
git pull origin main  # Download latest changes
"""

# 5. Example Function (Prime Number Check)
def is_prime(n):
    """Returns True if n is a prime number, else False."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

print(f"Is 7 prime? {is_prime(7)}")  # Output: True
print(f"Is 8 prime? {is_prime(8)}")  # Output: False


print(type(2))
print(type(2.0))
print(type(False))
print(type(None))



