import sys
import os.path
import json

if (os.path.exists(sys.argv[1])):
    with open(sys.argv[1]) as json_report_file:
        data = json.load(json_report_file)
    for d in data:
       print(d['file'].strip(), ",", str(d['line']), ",", "\"" + d['qualifier'] + "\"")
       
