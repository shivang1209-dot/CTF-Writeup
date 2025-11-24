# Decompiled with PyLingual (https://pylingual.io)
# Internal filename: pylinguese.py
# Bytecode version: 3.12.0rc2 (3531)
# Source timestamp: 2025-09-06 18:41:22 UTC (1757184082)

import pyfiglet
file = open('flag.txt', 'r')
flag = file.read()
font = 'slant'
words = 'MASONCC IS THE BEST CLUB EVER'
flag_track = 0
art = list(pyfiglet.figlet_format(words, font=font))
i = len(art) % 10
for ind in range(len(art)):
    if ind == i and flag_track < len(flag):
        art[ind] = flag[flag_track]
        i += 28
        flag_track += 1
art_str = ''.join(art)
first_val = 5
second_val = 6
first_half = art_str[:len(art_str) // 2]
second_half = art_str[len(art_str) // 2:]
first = [~ord(char) ^ first_val for char in first_half]
second = [~ord(char) ^ second_val for char in second_half]
output = second + first
print(output)