import os.path
import sys
import xml.etree.ElementTree as ET

report=sys.argv[1]

tree = ET.parse(report)
root = tree.getroot()
errors = root[1]
for error in errors:
    msg = "\"" + error.attrib['verbose'] + "\""
    for location in error:
        print(os.path.basename(location.attrib['file']) + ",", location.attrib['line'] + ",", msg)
    
