import sys
import os
from extract_X import extract

max_size = 40000000

file_size = os.path.getsize(sys.argv[1])
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
png_header = bytes([0x89, 0x50, 0x4E, 0x47, 0x0D, 0x0A, 0x1A, 0x0A])
png_footer = bytes([0x49, 0x45, 0x4E, 0x44])
while not end_reached:
    last_found_index = data.find(png_header, last_found_index + 1)
    if last_found_index != -1:
        start = last_found_index
        end = data.find(png_footer, last_found_index)
        occurrences.append([start, end + 4])
    else:
        end_reached = True
print("I have found", occurrences.__len__(), "occurrences")


# extract them all
for i in range(occurrences.__len__()):
    output = "file_" + i.__str__() + ".png"
    extract(data, occurrences[i][0], occurrences[i][1], output)
