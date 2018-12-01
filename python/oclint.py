import sys
import os.path
import system
import dirutils
import tempfile
import shutil

temp_path = os.path.abspath(sys.argv[1])
directory = os.path.abspath(sys.argv[2])
csv       = os.path.abspath(sys.argv[3])
exe       = sys.argv[4]
if (len(sys.argv) > 5):
    opts      = sys.argv[5]
else:
    opts = ""

# create temporary dir to run the analyzer
tmpdir_path = os.path.join("/home","itc","tmp", "oclint-" + next(tempfile._get_candidate_names()))
shutil.copytree(directory, tmpdir_path)
    
print("======[OCLINT]=======")
print("[CWD]:", tmpdir_path)
print("[CSV]:", csv)
print("[EXE]:", exe)
print("[EXE OPTIONS]:", opts)

source_files = dirutils.list_files(tmpdir_path, '.c') + dirutils.list_files(tmpdir_path, '.cpp')

if os.path.exists(csv):
    os.remove(csv)
sys.stdout = open(csv, "w")
print("File, Line, Error")
sys.stdout = sys.__stdout__


for source_file in source_files:
    oclint = exe + " " + source_file
    (output, err, exit, time) = system.system_call(oclint, tmpdir_path)
    lines = output.splitlines()
    sys.stdout = open(csv, "a")
    for line in lines:
        a = line.decode("utf-8").strip().split(":")
        if (len(a) >= 3):
            message = a[3]
            i = 4
            while (i < len(a)):
                message = message + ":" + a[i]
                i = i + 1
            print(os.path.basename(a[0]), ",", a[1], ",", "\"" + message + "\"")
    sys.stdout = sys.__stdout__

print("[CLEANUP]: removing ", tmpdir_path)
shutil.rmtree(tmpdir_path)
print("======[DONE WITH OCLINT]=======")
