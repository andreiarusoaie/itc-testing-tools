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

print("======Running frama-c=======")
print("Working dir:", directory)
print("CSV file:", csv)
print("Excutable:", exe)
print("Executable options:", opts)

c_files = dirutils.list_files(directory, '.c') # + dirutils.list_files(directory, '.cpp')
c_files = [x for x in c_files if not ('invalid_extern' in x)]

(output, err, exit, time) = system.system_call(exe + " -val " + " ".join(c_files), directory)
temp_path = os.path.join(os.getcwd(), "csv", "framac", "temp", "framac-output.txt")
temp_file = open(temp_path, 'a')
temp_file.write(output.decode("utf-8"))
temp_file.close()

sys.stdout = open(csv, "w")
print("File, Line, Error")
with open(temp_path) as f:
    for line in f.readlines():
        a = line.strip().split(":")
        if (len(a) >= 3 and (a[0].endswith(".c") or a[0].endswith(".cpp"))):
            message = a[2]
            i = 3
            while (i < len(a)):
                message = message + ":" + a[i]
                i = i + 1
            print(os.path.basename(a[0]), ",", a[1], ",", message)
sys.stdout = sys.__stdout__            
print("======Done with frama-c=======")
