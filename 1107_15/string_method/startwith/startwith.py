text = "Hello, world!"
print(text.startswith("Hello"))   # Output: True
print(text.startswith("world"))   # Output: False
print(text.startswith("Hello", 0, 5))  # Output: True (checks only the first 5 characters)
print(text.startswith("world", 7))  # Output: True (starting from index 7)
