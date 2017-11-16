import sys
import os.path
import system
import dirutils
import tempfile
import xml.etree.ElementTree as ET

temp_path = os.path.abspath(sys.argv[1])
directory = os.path.abspath(sys.argv[2])
csv       = os.path.abspath(sys.argv[3])
exe       = sys.argv[4]
opts      = sys.argv[5]

print("======Running cppcheck=======")
print("Working dir:", directory)
print("CSV file:", csv)
print("Excutable:", exe)
print("Executable options:", opts)

(output, err, exit, time) = system.system_call(exe + " --quiet " + opts + " " + directory + " --output-file=" + temp_path, ".")

report=temp_path
sys.stdout = open(csv, "w")
print("File, Line, Error")
tree = ET.parse(report)
root = tree.getroot()
errors = root[1]
for error in errors:
    msg = "\"" + error.attrib['verbose'] + "\""
    for location in error:
        print(os.path.basename(location.attrib['file']) + ",", location.attrib['line'] + ",", msg)
sys.stdout = sys.__stdout__
print("====== Done with cppcheck=======")
