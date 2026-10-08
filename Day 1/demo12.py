# Demonstrate 5 common Python string methods
s = "hello world"
print(s.upper())       # Convert to uppercase
print(s.lower())       # Convert to lowercase
print(s.title())       # Convert to title case
print(s.replace("world", "Python"))  # Replace substring
print(s.split())       # Split string into a list of words
print(s.startswith("hello"))  # Check if string starts with "hello"
print(s.endswith("world"))    # Check if string ends with "world"
print(s.find("world"))        # Find the index of substring "world"
print(s.count("l"))           # Count occurrences of the character "l"
print(s.isalpha())            # Check if all characters are alphabetic
print(s.isdigit())            # Check if all characters are digits
print(s.isspace())            # Check if all characters are whitespace