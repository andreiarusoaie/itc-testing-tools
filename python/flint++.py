import json
import sys
import os.path
import system
import dirutils
import shutil
import tempfile
from pathlib import Path

temp_path = os.path.abspath(sys.argv[1])
directory = os.path.abspath(sys.argv[2])
csv       = os.path.abspath(sys.argv[3])
exe       = sys.argv[4]
opts      = sys.argv[5]

# create temporary dir to run the analyzer
tmpdir_path = os.path.join(str(Path.home()),"tmp", "flintpp-" + next(tempfile._get_candidate_names()))
shutil.copytree(directory, tmpdir_path)

print("======[FLINT++]=======")
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
    flintpp = exe + " " + opts + " " + source_file
    (output, err, exit, time) = system.system_call(flintpp, tmpdir_path)
    data = json.loads(output.decode("utf-8"))
    sys.stdout = open(csv, "a")
    for f in data['files']:
        filename = f['path']
        for error in f['reports']:
            print(os.path.basename(filename), ",", error['line'], ",", error['title'])
    sys.stdout = sys.__stdout__
    
print("[CLEANUP]: removing ", tmpdir_path)
shutil.rmtree(tmpdir_path)  
print("======[DONE WITH FLINT++]=======")
