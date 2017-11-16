import sys
import os
from collections import defaultdict
from math import sqrt

# input files
merged_csv_filename=sys.argv[1]
tool_filename_w_defects=sys.argv[2]
tool_filename_wo_defects=sys.argv[3]
tool_out_subdefects=sys.argv[4]
tool_out_defects=sys.argv[5]
tool_out_total=sys.argv[6]

# handle list of tools to detect unique bugs
tools = []
if len(sys.argv) > 7:
    tools = sys.argv[7].split(",")
    
# print(merged_csv_filename)
# print(tool_filename_w_defects)
# print(tool_filename_wo_defects)
# print(tool_out_subdefects)
# print(tool_out_defects)
# print(tool_out_total)
# exit(1)

def get_defects_reported_by_tool(tool_filename_w_defects, tool_filename_wo_defects):
    w_defects_found = defaultdict(lambda: [])
    wo_defects_found = defaultdict(lambda: [])

    firstLine = True
    with open(tool_filename_w_defects, "r") as merged_file:
        for line in merged_file:
            if (firstLine):
                firstLine = False
                continue
            a = line.split(",")
            filename = a[0].strip()
            line = int(a[1].strip())
            w_defects_found[filename].append(line)

    firstLine = True
    with open(tool_filename_wo_defects, "r") as merged_file:
        for line in merged_file:
            if (firstLine):
                firstLine = False
                continue
            a = line.split(",")
            filename = a[0].strip()
            line = int(a[1].strip())
            wo_defects_found[filename].append(line)

    return (w_defects_found, wo_defects_found)


def get_filename_w_defects(tool):
    csv_file = os.path.basename(os.path.realpath(tool_filename_w_defects))
    csv = os.path.join(os.path.dirname(os.path.realpath(tool_filename_w_defects)), "..", "..", tool, "temp", csv_file)
    return csv

def get_filename_wo_defects(tool):
    csv_file = os.path.basename(os.path.realpath(tool_filename_wo_defects))
    csv = os.path.join(os.path.dirname(os.path.realpath(tool_filename_wo_defects)), "..", "..", tool, "temp", csv_file)
    return csv

    
# get defects for current tool
(w_defects_found, wo_defects_found) = get_defects_reported_by_tool(tool_filename_w_defects, tool_filename_wo_defects)

# get defects for other tools
defects_by_tool = {}
for tool in tools:
    w_defects = get_filename_w_defects(tool)
    wo_defects = get_filename_wo_defects(tool)
    defects_by_tool[tool] = get_defects_reported_by_tool(w_defects, wo_defects)

# print(defects_by_tool)


### statistics

# read merged file into datastructures
defect_dict = {}
subdefect_dict = {}
line_dict = {}
line_wo_dict = {}
variations = []
variations_by_filename = defaultdict(lambda: [])
filenames_by_defect = defaultdict(lambda: set())
firstLine = True
with open(merged_csv_filename, "r") as merged_file:
    for line in merged_file:
        if (firstLine):
            firstLine = False
            continue
        a = line.split(",")
        filename = a[0].strip()
        line_w_def = int(a[1].strip())
        line_wo_def = int(a[2].strip())
        def_type = a[3].strip()
        def_subtype = a[4].strip()
        filenames_by_defect[def_type].add(filename)
        if (not (filename in defect_dict.keys())):
            defect_dict[filename] = def_type
            subdefect_dict[filename] = def_subtype
            line_dict[filename] = []
            line_wo_dict[filename] = []
        line_dict[filename].append(line_w_def)
        line_wo_dict[filename].append(line_wo_def)

        x = line_w_def in w_defects_found[filename]
        y = line_wo_def in wo_defects_found[filename]            

        detected_by_w = set()
        detected_by_wo = set()
        for tool in tools:
            (tool_w_defects_found,tool_wo_defects_found) = defects_by_tool[tool]
            if line_w_def in tool_w_defects_found[filename]:
                detected_by_w.add(tool)
            if line_wo_def in tool_wo_defects_found[filename]:
                detected_by_wo.add(tool)
        
        tup = (filename, line_w_def, line_wo_def, x, y, detected_by_w, detected_by_wo)
        variations.append(tup)
        variations_by_filename[filename].append(tup)

# for filename in defect_dict.keys():
#     print(filename)
#     print(defect_dict[filename])
#     print(subdefect_dict[filename])
#     print(line_dict[filename])
#     print(line_wo_dict[filename])
#     print()
    
# print("=============")

sys.stdout = open("temp.txt", "a")
for variation in variations:
    print(variation)
sys.stdout = sys.__stdout__


# Sub-defects stats
sys.stdout = open(tool_out_subdefects, 'w')
print("Filename, Defect, Subdefect, TP, FP, Variations, Detection rate, False pos rate, Productivity, Robust detection rate", ",", "Unique")
for filename in defect_dict.keys():
    count_tp = 0
    count_fp = 0
    robust_counter = 0
    count_total = len(variations_by_filename[filename])
    unique = 0
    for variation in variations_by_filename[filename]:
        if (variation[3]):
            count_tp = count_tp + 1
        if (variation[4]):
            count_fp = count_fp + 1
        if (variation[3] and not variation[4]):
            robust_counter = robust_counter + 1
        diff = variation[5] - variation[6]
        if (variation[3] and (not variation[4]) and len(diff) == 0):
            unique = unique + 1
    dr = (count_tp * 100) / count_total
    fpr = (count_fp * 100) / count_total
    prod = sqrt(dr * (100 - fpr))
    robustness = (robust_counter * 100) / count_total
    print(filename,",", defect_dict[filename],",", subdefect_dict[filename],",", count_tp,",", count_fp,",", count_total, ",", round(dr,2), ",", round(fpr,2), ",", round(prod,2), ",", round(robustness,2), ",", unique)
    

# Defects stats
sys.stdout = open(tool_out_defects, 'w')
print("Defect, TP, FP, Variations, Detection rate, False pos rate, Productivity, Robust detection rate, Unique")
for defect in filenames_by_defect.keys():
    count_tp = 0
    count_fp = 0
    count_total = 0 
    robust_counter = 0
    unique = 0
    for filename in filenames_by_defect[defect]:
        count_total = count_total + len(variations_by_filename[filename])
        for variation in variations_by_filename[filename]:
            if (variation[3]):
                count_tp = count_tp + 1
            if (variation[4]):
                count_fp = count_fp + 1
            if (variation[3] and not variation[4]):
                robust_counter = robust_counter + 1
            diff = variation[5] - variation[6]
            if (variation[3] and (not variation[4]) and len(diff) == 0):
                unique = unique + 1
    dr = (count_tp * 100) / count_total
    fpr = (count_fp * 100) / count_total
    prod = sqrt(dr * (100 - fpr))
    robustness = (robust_counter * 100) / count_total
    print(defect,",", count_tp,",", count_fp,",", count_total, ",", round(dr,2), ",", round(fpr,2), ",", round(prod,2), ",", round(robustness,2), ",", unique)

    
# Total stats
sys.stdout = open(tool_out_total, 'w')
count_tp = 0
count_fp = 0
count_total = 0 
robust_counter = 0
unique = 0
print("TP, FP, Variations, Detection rate, False pos rate, Productivity, Robust detection rate, Unique")
for filename in defect_dict.keys():
    count_total = count_total + len(variations_by_filename[filename])
    for variation in variations_by_filename[filename]:
            if (variation[3]):
                count_tp = count_tp + 1
            if (variation[4]):
                count_fp = count_fp + 1
            if (variation[3] and not variation[4]):
                robust_counter = robust_counter + 1
            diff = variation[5] - variation[6]
            if (variation[3] and (not variation[4]) and len(diff) == 0):
                unique = unique + 1
dr = (count_tp * 100) / count_total
fpr = (count_fp * 100) / count_total
prod = sqrt(dr * (100 - fpr))
robustness = (robust_counter * 100) / count_total
print(count_tp,",", count_fp,",", count_total, ",", round(dr,2), ",", round(fpr,2), ",", round(prod,2), ",", round(robustness,2), ",", unique)
