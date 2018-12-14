import json
import sys
import os.path
import system
import shutil
import tempfile
import dirutils
from pathlib import Path

temp_path = os.path.abspath(sys.argv[1])
directory = os.path.abspath(sys.argv[2])
csv       = os.path.abspath(sys.argv[3])
exe       = sys.argv[4]

# create temporary dir to run the analyzer
tmpdir_path = os.path.join(str(Path.home()),"tmp", "infer-" + next(tempfile._get_candidate_names()))
shutil.copytree(directory, tmpdir_path)

print("======[INFER]=======")
print("[CWD]:", tmpdir_path)
print("[CSV]:", csv)
print("[EXE]:", exe)

source_files = dirutils.list_files(tmpdir_path, '.c') + dirutils.list_files(tmpdir_path, '.cpp')
dirutils.file_line_error_header(csv)
dirutils.reset_file(temp_path)

for source_file in source_files:
    if source_file.endswith("invalid_extern_1.c"):
        continue
    if source_file.endswith("invalid_extern.c"):
        source_file = source_file + " " + os.path.join(tmpdir_path, "invalid_extern_1.c")
    infer = exe + " run -- gcc -c " + source_file
    (output, err, exit, time) = system.system_call(infer, tmpdir_path)
    dirutils.tool_exec_log(temp_path, infer, output, err, exit)
    sys.stdout = open(csv, "a")
    report_file = os.path.join(tmpdir_path, "infer-out", "report.json")
    if (os.path.exists(report_file)):
        with open(report_file) as json_report_file:
            data = json.load(json_report_file)
        for d in data:
            print(d['file'].strip(), ",", str(d['line']), ",", "\"" + d['qualifier'] + "\"")
    sys.stdout = sys.__stdout__
    shutil.rmtree(os.path.dirname(report_file))
    
print("[CLEANUP]: removing ", tmpdir_path)
shutil.rmtree(tmpdir_path)
print("======[DONE WITH INFER]=======")
