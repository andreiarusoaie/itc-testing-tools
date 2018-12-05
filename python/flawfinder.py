import sys
import os.path
import system
import dirutils
import tempfile
import shutil
from pathlib import Path

temp_path = os.path.abspath(sys.argv[1])
directory = os.path.abspath(sys.argv[2])
csv       = os.path.abspath(sys.argv[3])
exe       = sys.argv[4]

# create temporary dir to run the analyzer
tmpdir_path = os.path.join(str(Path.home()),"tmp", "flawfinder-" + next(tempfile._get_candidate_names()))
shutil.copytree(directory, tmpdir_path)

print("======[FLAWFINDER]=======")
print("[CWD]:", tmpdir_path)
print("[CSV]:", csv)
print("[EXE]:", exe)

source_files = dirutils.list_files(tmpdir_path, '.c') + dirutils.list_files(tmpdir_path, '.cpp')
if os.path.exists(csv):
    os.remove(csv)
sys.stdout = open(csv, "w")
print("File, Line, Error")
sys.stdout = sys.__stdout__


source_files = dirutils.list_files(directory, '.c') + dirutils.list_files(directory, '.cpp')
for source_file in source_files:
    flawfinder = exe + " " + source_file
    (output, err, exit, time) = system.system_call(flawfinder, tmpdir_path)
    lines = output.splitlines()
    sys.stdout = open(csv, "a")
    collectingMode = False
    error_message = "unknown"
    filename = "unknown"
    line_no = "unknown"
    for line in lines:
        a = line.decode("utf-8").strip().split(":")
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
                error_message = error_message + line.decode("utf-8").strip()
    sys.stdout = sys.__stdout__            

print("[CLEANUP]: removing ", tmpdir_path)
shutil.rmtree(tmpdir_path)
print("======[DONE WITH FLAWFINDER]=======")
