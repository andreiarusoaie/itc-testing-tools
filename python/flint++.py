import json
import sys
import os.path
import system
import dirutils

directory = os.path.abspath(sys.argv[1])
csv       = os.path.abspath(sys.argv[2])
exe       = sys.argv[3]
opts      = sys.argv[4]

print("======Running flint++=======")
print("Working dir:", directory)
print("CSV file:", csv)
print("Excutable:", exe)
print("Options:", opts)

c_files = dirutils.list_files(directory, '.c') + dirutils.list_files(directory, '.cpp')
(output, err, exit, time) = system.system_call(exe + " " + opts + " " + " ".join(c_files), directory)

temp_path = os.path.join(os.getcwd(), "csv", "flintpp", "temp", "flintpp-output.json")
temp_file = open(temp_path, 'w')
temp_file.write(output.decode("utf-8"))
temp_file.close()

sys.stdout = open(csv, "w")
print("File, Line, Error")
if (os.path.exists(temp_path)):
    with open(temp_path) as json_report_file:
        data = json.load(json_report_file)
    for f in data['files']:
        filename = f['path']
        for error in f['reports']:
            print(filename, ",", error['line'], ",", error['title'])
sys.stdout = sys.__stdout__
print("======Done with flint++=======")
