import csv
from itertools import combinations

def find_collisions(input_file, collisions_file):
    # Dictionary to store hash values and their corresponding words
    hash_dict = {}

    # Read the input file and populate hash_dict
    with open(input_file, 'r', encoding='utf-8') as infile:
        reader = csv.DictReader(infile)
        
        for row in reader:
            word = row['Word']
            hash_value = row['Hash']
            
            # Add word to the list of words that have this hash value
            if hash_value in hash_dict:
                hash_dict[hash_value].append(word)
            else:
                hash_dict[hash_value] = [word]

    # Write collisions to output file
    with open(collisions_file, 'w', newline='', encoding='utf-8') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(['Word1', 'Word2', 'Hash'])  # Header row
        
        # Find all collisions
        collision_count = 0
        for hash_value, words in hash_dict.items():
            if len(words) > 1:
                # Generate all unique pairs of words with the same hash
                for word1, word2 in combinations(words, 2):
                    writer.writerow([word1, word2, hash_value])
                    collision_count += 1

    print(f"Total collisions found: {collision_count}")

# Example usage
find_collisions('hashes.csv', 'collisions.csv')
