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
dirutils.file_line_error_header(csv)
dirutils.reset_file(temp_path)

for source_file in source_files:
    if source_file.endswith("main.c"):
        continue
    if source_file.endswith("invalid_extern_1.c"):
        continue
    if source_file.endswith("invalid_extern.c"):
        source_file = source_file + " " + os.path.join(tmpdir_path, "invalid_extern_1.c")
    flawfinder = exe + " " + source_file
    (output, err, exit, time) = system.system_call(flawfinder, tmpdir_path)
    dirutils.tool_exec_log(temp_path, flawfinder, output, err, exit)

    all_lines = output.splitlines()
    lines = []
    line_codes = []
    collect_flag = False
    for line in all_lines:
        dec = line.decode("utf-8").strip()
        if (collect_flag):
            lines.append(dec)
            if (len(dec.split(":")) >= 3):
                line_codes.append(True)
            else:
                line_codes.append(False)
        if dec == "FINAL RESULTS:":
            collect_flag = True
        if dec == "ANALYSIS SUMMARY:":
            break
    
    sys.stdout = open(csv, "a")
    for i in range(0,len(lines)):
        if (line_codes[i]):
            a = lines[i].split(":")
            filename = os.path.basename(a[0])
            line_no = a[1]
            error_message = ""
            j = 2
            while (j < len(a)):
                error_message = error_message + ":" + a[j]
                j = j + 1
            j = i + 1
            while (j < len(lines)):
                if (not line_codes[j]):
                    error_message += error_message + " " + lines[j].strip()
                    j = j + 1
                else:
                    break;
            print(filename, ",", line_no, ",", "\"" + error_message + "\"")
    sys.stdout = sys.__stdout__            

print("[CLEANUP]: removing ", tmpdir_path)
shutil.rmtree(tmpdir_path)
print("======[DONE WITH FLAWFINDER]=======")
