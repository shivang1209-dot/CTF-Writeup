#!/usr/bin/env python3

# Read the output
with open('output.txt', 'r') as f:
    content = f.read().strip()
    # Extract the list from "output = [...]"
    output = eval(content.split('=', 1)[1].strip())

# Split back into second and first halves
mid = len(output) // 2
second = output[:mid]
first = output[mid:]

# Reverse the transformations
first_val = 5
second_val = 6
first_half = ''.join([chr(~(val ^ first_val)) for val in first])
second_half = ''.join([chr(~(val ^ second_val)) for val in second])

# Reconstruct the art string
art_str = first_half + second_half

# Extract flag from positions: len(art) % 10, then every 28 chars
i = len(art_str) % 10
flag = ''
while i < len(art_str):
    flag += art_str[i]
    i += 28

print(flag)

