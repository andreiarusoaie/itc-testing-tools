import sys
import os.path
from itertools import takewhile
import re
import python.system

# directory = os.path.abspath(sys.argv[1])
# csv       = os.path.abspath(sys.argv[2])
# exe       = sys.argv[3]
# opts      = sys.argv[4]

def clanalyze(directory, csv, exe, opts):
    print("======Running cl /analyze=======")
    print("Working dir:", directory)
    print("CSV file:", csv)
    print("Excutable:", exe)
    print("Executable options:", opts)

    #c_files = dirutils.list_files(directory, '.c')
    temp_path = os.path.join(os.getcwd(), "csv", "clanalyze", "temp", "output.txt")

    try:
        (output, err, exit, time) = python.system.system_call(exe + " " + directory + "/*.c* > " + temp_path)
    except:
        print("TROUBLE CALLING ANALYZER: ", sys.exc_info())
    
    regexp = re.compile("(\S+)\((\d+)\)\s?:\s+\S+\s+\S+:\s+(.+)")

    with open(temp_path) as f:
        for line in f.readlines():
            m = regexp.match(line)
            if not (m is None):
                print("Filename: ", m.groups()[0], "Line number: ", m.groups()[1], "Message: ", m.groups()[2])

    print("DONE CLANALYZE")
