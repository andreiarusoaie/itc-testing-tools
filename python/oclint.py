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
if (len(sys.argv) > 5):
    opts      = sys.argv[5]
else:
    opts = ""

# create temporary dir to run the analyzer
tmpdir_path = os.path.join(str(Path.home()),"tmp", "oclint-" + next(tempfile._get_candidate_names()))
shutil.copytree(directory, tmpdir_path)
    
print("======[OCLINT]=======")
print("[CWD]:", tmpdir_path)
print("[CSV]:", csv)
print("[EXE]:", exe)
print("[EXE OPTIONS]:", opts)

source_files = dirutils.list_files(tmpdir_path, '.c') + dirutils.list_files(tmpdir_path, '.cpp')

dirutils.file_line_error_header(csv)
dirutils.reset_file(temp_path)

for source_file in source_files:
    if source_file.endswith("main.c"):
        continue
    if source_file.endswith("invalid_extern_1.c"):
        continue
    if source_file.endswith("invalid_extern.c"):
        source_file = source_file + " " + os.path.join(tmpdir_path, "invalid_extern_1.c")
    oclint = exe + " " + source_file
    (output, err, exit, time) = system.system_call(oclint, tmpdir_path)
    dirutils.tool_exec_log(temp_path, oclint, output, err, exit)
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
