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

print("======Running frama-c=======")
print("Working dir:", directory)
print("CSV file:", csv)
print("Excutable:", exe)
print("Executable options:", opts)

pthread = os.path.join(directory, "pthread.h")
unistd = os.path.join(directory, "unistd.h")
copyfile(os.path.join(directory, "pthread.hx"), pthread)
copyfile(os.path.join(directory, "unistd.hx"), unistd)

c_files = dirutils.list_files(directory, '.c') # + dirutils.list_files(directory, '.cpp')
c_files = [x for x in c_files if not ('invalid_extern' in x)]
c_files = [x for x in c_files if not ('wrong_arguments_func_pointer' in x)]
c_files = [x for x in c_files if not ('func_pointer' in x)]
print(c_files)
(output, err, exit, time) = system.system_call(exe + " -val " + " ".join(c_files), directory)
temp_file = open(temp_path, 'w')
temp_file.write(output.decode("utf-8"))
temp_file.close()

os.remove(pthread)
os.remove(unistd)

sys.stdout = open(csv, "w")
print("File, Line, Error")
with open(temp_path) as f:
    lines = f.readlines();
    for i in range(0, len(lines)):
        line = lines[i];
        a = line.strip().split(":")
        if (len(a) >= 3 and (a[0].endswith(".c") or a[0].endswith(".cpp"))):
            message = a[2]
            i = 3
            while (i < len(a)):
                message = message + ":" + a[i]
                i = i + 1
            fronts = a[0].split(" ");
            cfile = fronts[1];
            print(os.path.basename(cfile), ",", a[1], ",", message + lines[i+1].strip())
sys.stdout = sys.__stdout__            
print("======Done with frama-c=======")
