text = "Hello, world!"
print(text.find("world"))    # Output: 7
print(text.find("o"))        # Output: 4 (first occurrence)
print(text.find("Python"))   # Output: -1 (not found)
print(text.find("o", 5))     # Output: 8 (search starts from index 5)
