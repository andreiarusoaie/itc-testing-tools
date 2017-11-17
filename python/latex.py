import os
import sys
from math import sqrt


def lines(file_path):
    with open(file_path) as f:
        return f.read().splitlines()

def nice(toolname):
    if toolname == 'clangcore':
        return "Clang (core)"
    if toolname == 'clangalpha':
        return "Clang (alpha)"
    if toolname == 'clangcorealpha':
        return "Clang"
    if toolname == 'framac':
        return "Frama-C"
    if toolname == "clanalyze":
        return "MSVC"
    return toolname.capitalize()
    
def total(tex_file_name, rep_directory, tool_list):
    tex_file_path = os.path.join(rep_directory, tex_file_name)

    l = []
    for tool in tool_list:
        c_total_path = os.path.join(rep_directory, tool, 'c_total.csv')
        items = lines(c_total_path)[1].split(",");
        tp  = int(items[0].strip())
        fp  = int(items[1].strip())
        var = int(items[2].strip())
        rdc = int(items[6].strip())
        uni = int(items[8].strip())

        cpp_total_path = os.path.join(rep_directory, tool, 'cpp_total.csv')
        items = lines(cpp_total_path)[1].split(",");
        tp  = tp  + int(items[0].strip())
        fp  = fp  + int(items[1].strip())
        var = var + int(items[2].strip())
        rdc = rdc + int(items[6].strip())
        uni = uni + int(items[8].strip())
        
        dr  = round((tp * 100.0) / var, 2)
        fpr = round((fp * 100.0) / var, 2)
        pr  = round(sqrt(dr * (100 - fpr)), 2)
        rdr = round((rdc * 100.0) / var, 2)

        timing_path = os.path.join(rep_directory, tool, 'timing.csv')
        timing = lines(timing_path)[0].split(",")
        runtime = round(float(timing[1].strip()) + float(timing[2].strip()), 2)

        # put everything in a tuple
        l.append((tool, dr, fpr, pr, rdr, uni, runtime))

    srt = sorted(l, key = lambda x : x[3])
    srt.reverse()

    sys.stdout = open(tex_file_path, "w")
    print("\\begin{tabular}{|l|r|r|r|r|r|r|}")
    print("\\hline")
    print("\multicolumn{1}{|c|}{Tool} & \multicolumn{1}{|c|}{DR} & \multicolumn{1}{|c|}{FPR} & \multicolumn{1}{|c|}{PR} & \multicolumn{1}{|c|}{RDR} & \multicolumn{1}{|c|}{U} & \multicolumn{1}{|c|}{Time} \\\\ ")
    print("\\hline")
    for t in srt:
        t_as_list = list(map(lambda x : "{:4.2f}".format(x) if isinstance(x, float) else str(x), list(t)))
        t_as_list[0] = nice(t_as_list[0])
        print(' & '.join(t_as_list),"\\\\")
        
    print("\\hline")
    print("\\end{tabular}")
    sys.stdout = sys.__stdout__
    

# dr ----> item = 1 
def defects_dr(tex_file_name, rep_directory, tool_list):
    tex_file_path = os.path.join(rep_directory, tex_file_name)

    t_map = {}
    defects = set()
    for tool in tool_list:
        c_total_path = os.path.join(rep_directory, tool, 'c_defects.csv')
        head, *tail = lines(c_total_path)
        cpp_total_path = os.path.join(rep_directory, tool, 'cpp_defects.csv')
        h, *t = lines(cpp_total_path)

        def_map = {}
        for line in tail + t:
            items = line.split(",")
            name = items[0]
            defects.add(name)
            def_map[name] = (0, 0)

            tp  = int(items[1].strip())
            var = int(items[3].strip())
            dr  = round((tp * 100) / var, 2)
            def_map[name] = (def_map[name][0] + tp, def_map[name][1] + var)
            print(tool, name, dr, def_map[name])
        t_map[tool] = def_map


    print(t_map)
    print(defects)
        
    # sys.stdout = open(tex_file_path, "w")
    # print("\\begin{tabular}{|l|r|r|r|r|r|r|}")
    # print("\\hline")
    # for defect in sorted(defects):
    #     print(defect, "&")
    # print("\\hline")
    
    # print("\\hline")
    # print("\\end{tabular}")
    # sys.stdout = sys.__stdout__

