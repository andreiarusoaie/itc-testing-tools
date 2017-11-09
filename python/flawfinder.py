import sys
import os.path
import system
import dirutils
import tempfile

directory = os.path.abspath(sys.argv[1])
csv       = os.path.abspath(sys.argv[2])
exe       = sys.argv[3]
# opts      = sys.argv[4]

print("======Running flawfinder=======")
print("Working dir:", directory)
print("CSV file:", csv)
print("Excutable:", exe)
# print("Executable options:", opts)

c_files = dirutils.list_files(directory, '.c') + dirutils.list_files(directory, '.cpp')
(output, err, exit, time) = system.system_call(exe + " " + " ".join(c_files), directory)

temp_path = os.path.join(os.getcwd(), "csv", "flawfinder", "temp", "flawfinder-output.txt")
temp_file = open(temp_path, 'w')
temp_file.write(output.decode("utf-8"))
temp_file.close()

sys.stdout = open(csv, "w")
print("File, Line, Error")

with open(temp_path) as f:
    lines = f.readlines()
collectingMode = False
error_message = "unknown"
filename = "unknown"
line_no = "unknown"
for line in lines:
    a = line.strip().split(":")
    if (len(a) >= 3):
        if (collectingMode):
            print(filename, ",", line_no, ",", "\"" + error_message + "\"")
            collectingMode = False # this is needed to disable final
        filename = os.path.basename(a[0])
        line_no = a[1]
        error_message = ""
        j = 2
        while (j < len(a)):
            error_message = error_message + ":" + a[j]
            j = j + 1
        collectingMode = True
    else:
        if (collectingMode):
            error_message = error_message + line.strip()
sys.stdout = sys.__stdout__            
print("======Done with flawfinder=======")
