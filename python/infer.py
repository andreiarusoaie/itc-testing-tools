import json
import sys
import os.path
import system
import shutil
import tempfile
import dirutils

directory = os.path.abspath(sys.argv[1])
csv       = os.path.abspath(sys.argv[2])
exe       = sys.argv[3]

# create temporary dir to run the analyzer
tmpdir_path = os.path.join("/home","itc","tmp", "infer-" + next(tempfile._get_candidate_names()))
shutil.copytree(directory, tmpdir_path)

print("======[INFER]=======")
print("[CWD]:", tmpdir_path)
print("[CSV]:", csv)
print("[EXE]:", exe)

source_files = dirutils.list_files(tmpdir_path, '.c') + dirutils.list_files(tmpdir_path, '.cpp')
if os.path.exists(csv):
    os.remove(csv)
sys.stdout = open(csv, "w")
print("File, Line, Error")
sys.stdout = sys.__stdout__
       
for source_file in source_files:
    infer = exe + " run -- gcc -c " + source_file
    (output, err, exit, time) = system.system_call(infer, tmpdir_path)
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
