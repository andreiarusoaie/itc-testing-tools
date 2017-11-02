import sys

report = sys.argv[1]

with open(report) as f:
    for line in f.readlines():
        a = line.split(":")
        if (len(a) >= 4):
            print(a[0], ",", a[1], ",", a[3])
