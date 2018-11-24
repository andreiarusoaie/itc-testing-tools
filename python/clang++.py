import sys
import os.path
import system
import dirutils
import tempfile
import platform

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

c_files = dirutils.list_files(directory, '.cpp')
sys_opts = "" if (platform.system() != 'Linux') else " -I /usr/include -I /usr/include/x86_64-linux-gnu/ -I /usr/lib/clang/6.0/include"
(output, err, exit, time) = system.system_call(exe + " " + opts + " " + sys_opts +  " " + " ".join(c_files), ".")

temp_file = open(temp_path, 'w')
temp_file.write(err.decode("utf-8"))
temp_file.close()

report = temp_path
sys.stdout = open(csv, "w")
print("File, Line, Error")
with open(report) as f:
    for line in f.readlines():
        a = line.strip().split(":")
        if (len(a) >= 4):
            print(os.path.basename(a[0]), ",", a[1], ",", a[3] + ":" + a[4])
sys.stdout = sys.__stdout__
print("====== Done with clang=======")
