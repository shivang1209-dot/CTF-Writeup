s = "pesbMUQl73oWnqD9rAvFRKZaf0hO5@dBN4uSzCtGjE YxITwXiVm1Jcgy26LkH8P"

idx = [
29,1,54,26,10,42,10,24,24,
0,10,47,1,16,2,
26,1,7,7,42,
32,10,63,16,10,24,49,7,1,42,
37,10,51,51,23,12,30,42,
# shortened — easier way below
]

# Instead of pasting hundreds of indexes,
# do this automatically from your text:

import re, os

_resdir = os.path.dirname(os.path.abspath(__file__))
_path = os.path.join(_resdir, "decoded_payload.txt")
if not os.path.exists(_path):
    _path = "decoded_payload.txt"
data = open(_path, "r", encoding="latin1").read()

indexes = re.findall(r"~(\d+),1", data)

out = ""
for i in indexes:
    out += s[int(i)]

print(out)
