import sys
import os
import os.path
import system
import dirutils
import tempfile
from shutil import copyfile
import shutil
from pathlib import Path

temp_path = os.path.abspath(sys.argv[1])
directory = os.path.abspath(sys.argv[2])
csv       = os.path.abspath(sys.argv[3])
exe       = sys.argv[4]
if (len(sys.argv) > 5):
    opts      = sys.argv[5]
else:
    opts = ""
    
# create temporary dir to run the analyzer
tmpdir_path = os.path.join(str(Path.home()),"tmp", "sparse-" + next(tempfile._get_candidate_names()))
shutil.copytree(directory, tmpdir_path)
    
print("\n======[SPARSE]=======")
print("[CWD]:", tmpdir_path)
print("[CSV]:", csv)
print("[EXE]:", exe)
print("[EXE OPTIONS]:", opts)

# setup header file: comment math.h include.
hfile1 = os.path.join(tmpdir_path, "HeaderFile.h")
if directory.endswith("Cpp") :
    hfile1 = os.path.join(tmpdir_path, "HeaderFile.hpp")
hfile2 = os.path.join(tmpdir_path, "HeaderFile.hx")
copyfile(hfile2, hfile1);

if os.path.exists(csv):
    os.remove(csv)
sys.stdout = open(csv, "w")
print("File, Line, Error")
sys.stdout = sys.__stdout__

source_files = dirutils.list_files(tmpdir_path, '.c') + dirutils.list_files(tmpdir_path, '.cpp')
for source_file in source_files:
    sparse = exe + " " + source_file + " " + opts;
    (output, err, exit, time) = system.system_call(sparse, tmpdir_path)
    lines = err.splitlines();
    sys.stdout = open(csv, "a")
    for line in lines:
        a = line.decode("utf-8").strip().split(":")
        if (len(a) >= 4):
            message = a[3]
            i = 4
            while (i < len(a)):
                message = message + ":" + a[i]
                i = i + 1
            print(os.path.basename(a[0]), ",", a[1], ",", message)
    sys.stdout = sys.__stdout__
    
print("[CLEANUP]: removing ", tmpdir_path)
shutil.rmtree(tmpdir_path)
print("======[DONE WITH SPARSE]=======")
