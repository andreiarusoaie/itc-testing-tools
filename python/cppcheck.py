import sys
import os.path
import system
import dirutils
import tempfile
import xml.etree.ElementTree as ET
import shutil
from pathlib import Path

xml_report_path = os.path.abspath(sys.argv[1])
temp_path       = os.path.abspath(sys.argv[2])
directory       = os.path.abspath(sys.argv[3])
csv             = os.path.abspath(sys.argv[4])
exe             = sys.argv[5]
opts            = sys.argv[6]

# create temporary dir to run the analyzer
tmpdir_path = os.path.join(str(Path.home()),"tmp", "cppcheck-" + next(tempfile._get_candidate_names()))
shutil.copytree(directory, tmpdir_path)

print("\n======[CPPCHECK]=======")
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
    cppcheck = exe + opts + " " + source_file + " --output-file=" + xml_report_path
    (output, err, exit, time) = system.system_call(cppcheck, ".")
    dirutils.tool_exec_log(temp_path, cppcheck, output, err, exit)
    tree = ET.parse(xml_report_path)
    root = tree.getroot()
    errors = root[1]
    sys.stdout = open(csv, "a")
    for error in errors:
        msg = "\"" + error.attrib['verbose'] + "\""
        for location in error:
            print(os.path.basename(location.attrib['file']) + ",", location.attrib['line'] + ",", msg)
    sys.stdout = sys.__stdout__

print("[CLEANUP]: removing ", tmpdir_path)
shutil.rmtree(tmpdir_path)    
print("======[DONE WITH CPPCHECK]=======")
