import sys
import os
import os.path
import system
import dirutils
import tempfile
from shutil import copyfile

temp_path = os.path.abspath(sys.argv[1])
directory = os.path.abspath(sys.argv[2])
csv       = os.path.abspath(sys.argv[3])
exe       = sys.argv[4]
if (len(sys.argv) > 5):
    opts      = sys.argv[5]
else:
    opts = ""

print("======Running sparse=======")
print("Working dir:", directory)
print("CSV file:", csv)
print("Excutable:", exe)
print("Executable options:", opts)

hfile1 = os.path.join(directory, "HeaderFile.h")
if directory.endswith("Cpp") :
    hfile1 = os.path.join(directory, "HeaderFile.hpp")
hfile2 = os.path.join(directory, "HeaderFile.hx")
hfile3 = os.path.join(directory, "HeaderFile.tmp")
copyfile(hfile1, hfile3);
copyfile(hfile2, hfile1);

temp_file = open(temp_path, 'w')
temp_file.write("")
temp_file.close()

c_files = dirutils.list_files(directory, '.c') + dirutils.list_files(directory, '.cpp')
c_files = [x for x in c_files if not ('main' in x)]
temp_file = open(temp_path, 'a')
for sourcefile in c_files:
    (output, err, exit, time) = system.system_call(exe + " " + sourcefile + " " + opts, directory)
    temp_file.write(err.decode("utf-8"))
temp_file.close()

copyfile(hfile3, hfile1);
os.remove(hfile3)

sys.stdout = open(csv, "w")
print("File, Line, Error")
with open(temp_path) as f:
    for line in f.readlines():
        a = line.strip().split(":")
        if (len(a) >= 4):
            message = a[3]
            i = 4
            while (i < len(a)):
                message = message + ":" + a[i]
                i = i + 1
            print(os.path.basename(a[0]), ",", a[1], ",", message)

sys.stdout = sys.__stdout__            
print("======Done with sparse=======")
