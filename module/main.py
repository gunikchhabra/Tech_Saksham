import myModule
from math.operations import multiply, divide
from utils.math_operations import add, subtract, multiply, divide
from utils.greetings import greet

print(myModule.greet("Alice"))
print(myModule.add(5, 3))

# Using mymodule
print(myModule.greet("Alice"))
print(myModule.add(5, 3))

# Using math_pkg.operations
print(multiply(4, 5))
print(divide(10, 2))

# Greeting the user
print(greet("Alice"))

# Performing mathematical operations
print("10 + 5 =", add(10, 5))
print("10 - 5 =", subtract(10, 5))
print("3 * 4 =", multiply(3, 4))
print("20 / 4 =", divide(20, 4))