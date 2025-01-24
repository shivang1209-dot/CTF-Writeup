# Initialize a list with placeholders for 32 positions
hash_list = [''] * 32

# Assign characters to their positions (adjusting for 0-indexing)
positions = {
    'a': [1, 2, 6, 20, 31, 32],
    'b': [29],
    'c': [3, 7, 8, 12, 14],
    'd': [21, 23],
    'f': [15, 17],
    '0': [16, 25],
    '1': [18],
    '2': [24],
    '3': [26],
    '4': [9, 27],
    '5': [4, 10, 19],
    '6': [5],
    '7': [11, 28, 30],
    '8': [22],
    '9': [13],
}

# Populate the hash list
for char, pos_list in positions.items():
    for pos in pos_list:
        hash_list[pos - 1] = char  # Convert to 0-indexed

# Join the list into the final hash string
final_hash = ''.join(hash_list)
print(f"Final Hash: {final_hash}")
