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

weird_number = int.from_bytes(data[0xbe:0xbf], byteorder='little')
count_of_assets = int.from_bytes(data[0xb4:0xb8], byteorder='little') - weird_number
assetsInfoSection = [int.from_bytes(data[0xb0:0xb4], byteorder='little'),
                     count_of_assets * 8]

assetsInfoSection = data[assetsInfoSection[0]:assetsInfoSection[0] + assetsInfoSection[1]]

for i in range(count_of_assets):
    assetSize = int.from_bytes(assetsInfoSection[i*8: i*8 + 4], byteorder='little')
    assetAbsolutePos = int.from_bytes(assetsInfoSection[i*8 + 4: i*8 + 8], byteorder='little')
    occurrences.append([assetSize, assetAbsolutePos])
    print([assetSize, assetAbsolutePos])

print("I have found", occurrences.__len__(), "occurrences")

# extract them all
for i in range(occurrences.__len__()):
    output = "file_" + i.__str__() + ".unk"
    extract(data, occurrences[i][1], occurrences[i][0] + occurrences[i][1], output)
