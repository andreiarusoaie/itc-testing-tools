import sys
import os.path

report = sys.argv[1]

with open(report) as f:
    for line in f.readlines():
        a = line.strip().split(":")
        if (len(a) >= 4):
            message = a[3]
            i = 4
            while (i < len(a)):
                message = message + ":" + a[i]
                i = i + 1
            print(os.path.basename(a[0]), ",", a[1], ",", message)
