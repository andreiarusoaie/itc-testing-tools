import sys
import os.path
import system
import dirutils
import tempfile

temp_path = os.path.abspath(sys.argv[1])
directory = os.path.abspath(sys.argv[2])
csv       = os.path.abspath(sys.argv[3])
exe       = sys.argv[4]
opts      = sys.argv[5]

print("======Running clang=======")
print("Working dir:", directory)
print("CSV file:", csv)
print("Excutable:", exe)
print("Executable options:", opts)

c_files = dirutils.list_files(directory, '.c')
(output, err, exit, time) = system.system_call(exe + " " + opts + " " + " ".join(c_files), ".")

temp_file = open(temp_path, 'w')
temp_file.write(err.decode("utf-8"))
temp_file.close()

sys.stdout = open(csv, "w")
print("File, Line, Error")
with open(temp_path) as f:
    for line in f.readlines():
        a = line.strip().split(":")
        if (len(a) >= 4):
            print(os.path.basename(a[0]), ",", a[1], ",", a[3] + ":" + a[4])
sys.stdout = sys.__stdout__
print("====== Done with clang=======")
