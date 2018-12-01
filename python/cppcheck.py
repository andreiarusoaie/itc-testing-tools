import sys
import os.path
import system
import dirutils
import tempfile
import xml.etree.ElementTree as ET
import shutil

xml_report_path = os.path.abspath(sys.argv[1])
directory       = os.path.abspath(sys.argv[2])
csv             = os.path.abspath(sys.argv[3])
exe             = sys.argv[4]
opts            = sys.argv[5]

# create temporary dir to run the analyzer
tmpdir_path = os.path.join("/home","itc","tmp", "cppcheck-" + next(tempfile._get_candidate_names()))
shutil.copytree(directory, tmpdir_path)

print("\n======[CPPCHECK]=======")
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
    cppcheck = exe + opts + " " + source_file + " --output-file=" + xml_report_path
    (output, err, exit, time) = system.system_call(cppcheck, ".")
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
