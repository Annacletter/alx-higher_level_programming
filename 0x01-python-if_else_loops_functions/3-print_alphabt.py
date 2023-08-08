#!/usr/bin/python3
excluded_chars = ['e', 'q']
result = 
''.join([chr(lower) for lower in range(97, 123) if chr(lower) not in excluded_chars])
print(result, end="")
