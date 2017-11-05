import sys
import os.path
from itertools import takewhile

report = sys.argv[1]

with open(report) as f:
    for line in f.readlines():
        a = line.strip().split(":")
        if (len(a) >= 4) and (a[0] == 'uno'):
            if len(a[2]) > 10: # hack to work around bug in printint wrong array indexing
                print(os.path.basename(a[1]), ",", ''.join(takewhile(str.isdigit, a[2].strip())), ",", a[2])
            else:
                print(os.path.basename(a[1]), ",", a[2], ",", a[3])
