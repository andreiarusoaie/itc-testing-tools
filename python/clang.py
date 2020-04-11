import sys
import os.path
import system
import dirutils
import tempfile
import platform
import shutil
from pathlib import Path

temp_path = os.path.abspath(sys.argv[1])
directory = os.path.abspath(sys.argv[2])
csv       = os.path.abspath(sys.argv[3])
exe       = sys.argv[4]
opts      = sys.argv[5]


# create temporary dir to run the analyzer
tmpdir_path = os.path.join(str(Path.home()),"tmp", "clang-" + next(tempfile._get_candidate_names()))
shutil.copytree(directory, tmpdir_path)

print("\n======[CLANG]=======")
print("[CWD]:", tmpdir_path)
print("[CSV]:", csv)
print("[EXE]:", exe)
print("[EXE OPTIONS]:", opts)

source_files = dirutils.list_files(tmpdir_path, '.c')
sys_opts = "" if (platform.system() != 'Linux') else " -I /usr/include -I /usr/include/x86_64-linux-gnu/ -I /usr/lib/clang/6.0/include"

dirutils.file_line_error_header(csv)
dirutils.reset_file(temp_path)

for source_file in source_files:
    if source_file.endswith("main.c"):
        continue
    if source_file.endswith("invalid_extern_1.c"):
        continue
    if source_file.endswith("invalid_extern.c"):
        source_file = source_file + " " + os.path.join(tmpdir_path, "invalid_extern_1.c")
    clang = exe + " " + opts + " " + sys_opts + " " + source_file
    (output, err, exit, time) = system.system_call(clang, ".")
    dirutils.tool_exec_log(temp_path, clang, output, err, exit)
    sys.stdout = open(csv, "a")
    print(err, file=sys.__stdout__)
    lines = err.splitlines()
    for line in lines:
        parsed = line.decode("utf-8").strip().split(":")
        if (len(parsed) >= 4 and parsed[0] == source_file and not parsed[3].endswith('note')):
            print(os.path.basename(parsed[0]), ",", parsed[1], ",", parsed[3] + ":" + parsed[4])
    sys.stdout = sys.__stdout__


print("[CLEANUP]: removing ", tmpdir_path)
shutil.rmtree(tmpdir_path)
print("======[DONE WITH CLANG]=======")
