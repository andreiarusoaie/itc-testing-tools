import re
import sys
import os

# traverse the lines, and consider only those having the above format
# the rest is ignored for now
with open(sys.argv[1]) as f:
    lines = f.readlines()


collectingMode = False
error_message = "unknown"
filename = "unknown"
line_no = "unknown"
for line in lines:
    a = line.strip().split(":")
    if (len(a) >= 3):
        if (collectingMode):
            print(filename, ",", line_no, ",", "\"" + error_message + "\"")
            collectingMode = False # probably this line is not needed
        filename = os.path.basename(a[0])
        line_no = a[1]
        error_message = ""
        j = 2
        while (j < len(a)):
            error_message = error_message + ":" + a[j]
            j = j + 1
        collectingMode = True
    else:
        if (collectingMode):
            error_message = error_message + line.strip()
            
