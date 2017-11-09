import json
import sys
import os.path
import system

directory = os.path.abspath(sys.argv[1])
csv       = os.path.abspath(sys.argv[2])
exe       = sys.argv[3]
opts      = sys.argv[4]

print("======Running Infer=======")
print("Working dir:", directory)
print("CSV file:", csv)
print("Excutable:", exe)
print("Executable options:", opts)

(output, err, exit, time) = system.system_call("make clean", directory)
(output, err, exit, time) = system.system_call(exe + " run -- make", directory)

sys.stdout = open(csv, "w")
print("File, Line, Error")
report_file = os.path.join(directory, "infer-out", "report.json")
if (os.path.exists(report_file)):
    with open(report_file) as json_report_file:
        data = json.load(json_report_file)
    for d in data:
        print(d['file'].strip(), ",", str(d['line']), ",", "\"" + d['qualifier'] + "\"")
sys.stdout = sys.__stdout__
print("======Done with Infer=======")
