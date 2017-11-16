import sys
import os.path
import system
import dirutils
import tempfile

directory = os.path.abspath(sys.argv[1])
csv       = os.path.abspath(sys.argv[2])
exe       = sys.argv[3]
if (len(sys.argv) > 4):
    opts      = sys.argv[4]
else:
    opts = ""

print("======Running cpplint=======")
print("Working dir:", directory)
print("CSV file:", csv)
print("Excutable:", exe)
print("Executable options:", opts)

c_files = dirutils.list_files(directory, '.c') + dirutils.list_files(directory, '.cpp')
(output, err, exit, time) = system.system_call(exe + " " + " ".join(c_files) + " " + opts, directory)

temp_path = os.path.join(os.getcwd(), "csv", "uno", "temp", "uno-output.txt")
temp_file = open(temp_path, 'w')
temp_file.write(output.decode("utf-8"))
temp_file.close()

sys.stdout = open(csv, "w")
print("File, Line, Error")
with open(temp_path) as f:
    for line in f.readlines():
        a = line.strip().split(":")
        if (len(a) >= 4) and (a[0] == 'uno'):
            if len(a[2]) > 10: # hack to work around bug in printint wrong array indexing
                print(os.path.basename(a[1]), ",", ''.join(takewhile(str.isdigit, a[2].strip())), ",", a[2])
            else:
                print(os.path.basename(a[1]), ",", a[2], ",", a[3])

sys.stdout = sys.__stdout__            
print("======Done with uno=======")
