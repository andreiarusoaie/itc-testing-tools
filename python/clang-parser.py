import sys
import os.path

report = sys.argv[1]

with open(report) as f:
    for line in f.readlines():
        a = line.strip().split(":")
        if (len(a) >= 4):
            print(os.path.basename(a[0]), ",", a[1], ",", a[3] + ":" + a[4])
