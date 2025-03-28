text = "Hello, world!"
print(text.index("world"))    # Output: 7
print(text.index("o"))        # Output: 4 (first occurrence)
print(text.index("o", 5))     # Output: 8 (search starts from index 5)

# print(text.index("Python"))  # Raises ValueError: substring not found
