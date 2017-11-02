import re
import os
import time

import system


# this is supposed to match over 'filename:line:column:warning message' format
extractor = re.compile(b'(.+?\.[ch])\:([0-9]+?):(.+?)$')

# traverse the lines, and consider only those having the above format
# the rest is ignored for now
with open(sys.argv[1]) as f:
    lines = f.readlines()

lno = 0
for line in lines:
    matched = extractor.match(line)
    if (not matched == None):
        filename = os.path.basename(matched.group(1).decode("utf-8"))
        line_no = matched.group(2).decode("utf-8")
        key = filename + ":" + line_no
        error_msg = matched.group(3).decode("utf-8")
        k = 1
        while (lines[lno + k].strip() and (extractor.match(lines[lno+k]) == None)):
            error_msg = error_msg + str(lines[lno+k].decode("utf-8"))
            k = k + 1
        print(filename, line_no, error_msg)
     
    lno = lno + 1


