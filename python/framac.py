import sys
import os
import os.path
import system
import dirutils
import tempfile
import shutil
from shutil import copyfile
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
tmpdir_path = os.path.join(str(Path.home()), "tmp", "frama-c-" + next(tempfile._get_candidate_names()))
shutil.copytree(directory, tmpdir_path)

print("======[FRAMA-C]=======")
print("[CWD]:", tmpdir_path)
print("[CSV]:", csv)
print("[EXE]:", exe)
print("[EXE OPTIONS]:", opts)

pthread = os.path.join(directory, "pthread.h")
unistd = os.path.join(directory, "unistd.h")
# copyfile(os.path.join(directory, "pthread.hx"), pthread)
# copyfile(os.path.join(directory, "unistd.hx"), unistd)

source_files = dirutils.list_files(directory, '.c') + dirutils.list_files(directory, '.cpp')

if os.path.exists(csv):
    os.remove(csv)
sys.stdout = open(csv, "w")
print("File, Line, Error")
sys.stdout = sys.__stdout__

for source_file in source_files:
    framac = exe + " -val -quiet " + source_file + " main.c"
    (output, err, exit, time) = system.system_call(framac, directory)
    sys.stdout = open(csv, "a")
    lines = output.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i].decode("utf-8")
        if (line[0] == '['):
            j = line.find("]");
            if (j != -1):
                parsed = line[j+1:].split(':')
                if (len(parsed) >= 3):
                    fname = parsed[0].strip()
                    line_no = parsed[1].strip()
                    message = parsed[2].strip()
                    if (i + 1 < len(lines)):
                        message = message + ":" + lines[i+1].decode("utf-8")
                    if (fname != "main.c" and line_no.isdigit()):
                        print(fname + "," + line_no + "," + message)
        i = i + 1
    sys.stdout = sys.__stdout__

print("[CLEANUP]: removing ", tmpdir_path)
shutil.rmtree(tmpdir_path)
print("======[DONE WITH FRAMA-C]=======")
