import sys
import os
from extract_X import extract

max_size = 4000000

file_size = os.path.getsize(sys.argv[1])
# print(file_size)
if file_size > max_size:
    print("File size is greater than", max_size)
    exit()

file = open(sys.argv[1], "rb")
data = file.read()
file.close()

# find all occurrence
occurrences = []
last_found_index = -1
end_reached = False
while not end_reached:
    last_found_index = data.find(b'RIFF', last_found_index + 1)
    if not last_found_index == -1:
        occurrences.append(last_found_index)
    else:
        end_reached = True
print("I have found", occurrences.__len__(), "occurrences")

# get their sizes
sizes = []
for i in occurrences:
    sizes.append(int.from_bytes(data[i + 4:i + 8], byteorder='little'))

# extract them all
for i in range(occurrences.__len__()):
    output = "file_" + i.__str__() + ".wav"
    extract(data, occurrences[i], occurrences[i] + sizes[i], output)

print(sizes)
