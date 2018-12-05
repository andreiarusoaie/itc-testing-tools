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
        return "System"
    if toolname == "flintpp":
        return "Flint++"
    return toolname.capitalize()
    
def total(tex_file_name, rep_directory, latex_dir, tool_list):
    tex_file_path = os.path.join(latex_dir, tex_file_name)

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
    

# Detection rate by defects
def defects_dr(tex_file_name, rep_directory, latex_dir, tool_list):
    tex_file_path = os.path.join(latex_dir, tex_file_name)

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
            if (not name in def_map.keys()):
                def_map[name] = (0, 0)
            
            tp  = int(items[1].strip())
            var = int(items[3].strip())
            def_map[name] = (def_map[name][0] + tp, def_map[name][1] + var)
        t_map[tool] = def_map

    sys.stdout = open(tex_file_path, "w")
    print("\\begin{tabular}{|l|r|r|r|r|r|r|r|r|r|r|}")
    print("%\\hline")
    print("% Detection rate per defects \\\\ ")
    print("\\hline")
    print("Tool & D1 & D2 & D3 & D4 & D5 & D6 & D7 & D8 & D9", "\\\\")
    print("%% ", "Tool &", " & ".join(sorted(defects)), "\\\\")
    print("\\hline")
    for tool in sorted(t_map.keys()):
        print(nice(tool), end="")
        def_map = t_map[tool]
        for defect in sorted(defects):
            tp  = def_map[defect][0]
            var = def_map[defect][1]
            dr  = int(round((tp * 100) / var, 0))
            print(" & ", dr, end="")
        print("\\\\")
    print("\\hline")
    print("\\end{tabular}")
    sys.stdout = sys.__stdout__

# false positives rate
def defects_fpr(tex_file_name, rep_directory, latex_dir, tool_list):
    tex_file_path = os.path.join(latex_dir, tex_file_name)

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
            if (not name in def_map.keys()):
                def_map[name] = (0, 0)

            fp  = int(items[2].strip())
            var = int(items[3].strip())
            def_map[name] = (def_map[name][0] + fp, def_map[name][1] + var)
        t_map[tool] = def_map

    sys.stdout = open(tex_file_path, "w")
    print("\\begin{tabular}{|l|r|r|r|r|r|r|r|r|r|r|}")
    print("%\\hline")
    print("% False positive rate per defects \\\\ ")
    print("\\hline")
    print("Tool & D1 & D2 & D3 & D4 & D5 & D6 & D7 & D8 & D9", "\\\\")
    print("%% ", "Tool &", " & ".join(sorted(defects)), "\\\\")
    print("\\hline")
    for tool in sorted(t_map.keys()):
        print(nice(tool), end="")
        def_map = t_map[tool]
        for defect in sorted(defects):
            fp  = def_map[defect][0]
            var = def_map[defect][1]
            fpr  = int(round((fp * 100) / var, 0))
            print(" & ", fpr, end="")
        print("\\\\")
    print("\\hline")
    print("\\end{tabular}")
    sys.stdout = sys.__stdout__

# production     
def defects_pr(tex_file_name, rep_directory, latex_dir, tool_list):
    tex_file_path = os.path.join(latex_dir, tex_file_name)

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
            if (not name in def_map.keys()):
                def_map[name] = (0, 0, 0)

            tp  = int(items[1].strip())
            fp  = int(items[2].strip())
            var = int(items[3].strip())
            def_map[name] = (def_map[name][0] + tp, def_map[name][1] + fp, def_map[name][2] + var)
        t_map[tool] = def_map

    sys.stdout = open(tex_file_path, "w")
    print("\\begin{tabular}{|l|r|r|r|r|r|r|r|r|r|r|}")
    print("%\\hline")
    print("% Production per defects \\\\ ")
    print("\\hline")
    print("Tool & D1 & D2 & D3 & D4 & D5 & D6 & D7 & D8 & D9", "\\\\")
    print("%% ", "Tool &", " & ".join(sorted(defects)), "\\\\")
    print("\\hline")
    for tool in sorted(t_map.keys()):
        print(nice(tool), end="")
        def_map = t_map[tool]
        for defect in sorted(defects):
            tp  = def_map[defect][0]
            fp  = def_map[defect][1]
            var = def_map[defect][2]
            dr  = round((tp * 100) / var, 2)
            fpr  = round((fp * 100) / var, 2)
            pr = int(round(sqrt(dr * (100 - fpr)), 0)) 
            print(" & ", pr, end="")
        print("\\\\")
    print("\\hline")
    print("\\end{tabular}")
    sys.stdout = sys.__stdout__

# Robust detection rate
def defects_rdr(tex_file_name, rep_directory, latex_dir, tool_list):
    tex_file_path = os.path.join(latex_dir, tex_file_name)

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
            if (not name in def_map.keys()):
                def_map[name] = (0, 0)

            rdc  = int(items[7].strip())
            var = int(items[3].strip())
            def_map[name] = (def_map[name][0] + rdc, def_map[name][1] + var)
        t_map[tool] = def_map

    sys.stdout = open(tex_file_path, "w")
    print("\\begin{tabular}{|l|r|r|r|r|r|r|r|r|r|r|}")
    print("%\\hline")
    print("% Robust detection rate per defects \\\\ ")
    print("\\hline")
    print("Tool & D1 & D2 & D3 & D4 & D5 & D6 & D7 & D8 & D9", "\\\\")
    print("%% ", "Tool &", " & ".join(sorted(defects)), "\\\\")
    print("\\hline")
    for tool in sorted(t_map.keys()):
        print(nice(tool), end="")
        def_map = t_map[tool]
        for defect in sorted(defects):
            rdc  = def_map[defect][0]
            var = def_map[defect][1]
            rdr  = int(round((rdc * 100) / var, 0))
            print(" & ", rdr, end="")
        print("\\\\")
    print("\\hline")
    print("\\end{tabular}")
    sys.stdout = sys.__stdout__

def defects_unique(tex_file_name, rep_directory, latex_dir, tool_list):
    tex_file_path = os.path.join(latex_dir, tex_file_name)

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
            if (not name in def_map.keys()):
                def_map[name] = 0

            rdc  = int(items[9].strip())
            def_map[name] = def_map[name] + rdc
        t_map[tool] = def_map

    sys.stdout = open(tex_file_path, "w")
    print("\\begin{tabular}{|l|r|r|r|r|r|r|r|r|r|r|}")
    print("% \\hline")
    print("% Unique (robust) defects \\\\ ")
    print("\\hline")
    print("Tool & D1 & D2 & D3 & D4 & D5 & D6 & D7 & D8 & D9", "\\\\")
    print("%% ", "Tool &", " & ".join(sorted(defects)), "\\\\")
    print("\\hline")
    for tool in sorted(t_map.keys()):
        print(nice(tool), end="")
        def_map = t_map[tool]
        for defect in sorted(defects):
            unique  = def_map[defect]
            print(" & ", unique, end="")
        print("\\\\")
    print("\\hline")
    print("\\end{tabular}")
    sys.stdout = sys.__stdout__




# Production by subdefects
def subdefects_pr(tex_file_name, rep_directory, latex_dir, tool_list):
    tex_file_path = os.path.join(latex_dir, tex_file_name)

    t_map = {}
    subdefects = set()
    subdef_map = {} # subdef |-> [(tool, production)]
    for tool in tool_list:
        c_total_path = os.path.join(rep_directory, tool, 'c_subdefects.csv')
        head, *tail = lines(c_total_path)
        cpp_total_path = os.path.join(rep_directory, tool, 'cpp_subdefects.csv')
        h, *t = lines(cpp_total_path)

        for line in tail + t:
            items = line.split(",")
            name = items[2]
            subdefects.add(name)
            if (not name in subdef_map.keys()):
                subdef_map[name] = []
            
            tp  = int(items[3].strip())
            fp  = int(items[4].strip())
            var = int(items[5].strip())
            dr  = round((tp * 100) / var, 2)
            fpr = round((fp * 100) / var, 2)
            pr  = round(sqrt(dr * (100 - fpr)), 2)
            subdef_map[name] = subdef_map[name] + [(tool, pr)]


    for subdef in subdef_map.keys():
        # print(subdef,":")
        # print(subdef_map[subdef])
        srt = sorted(subdef_map[subdef], key = lambda x : x[1])
        srt.reverse()
        subdef_map[subdef] = srt[0]
        # print(subdef_map[subdef])
        # print("\n\n")

    sys.stdout = open(tex_file_path, "w")
    print("\\begin{tabular}{|l|c|r|}")
    print("%\\hline")
    print("% Production per subdefects \\\\ ")
    print("\\hline")
    print("\multicolumn{1}{|c|}{Defect subtype} & \multicolumn{1}{|c|}{Tool} & \multicolumn{1}{|c|}{PR}", "\\\\")
    print("\\hline")
    for subdefect in sorted(subdef_map.keys()):
        sub = subdefect if len(subdefect) <= 20 else subdefect[0:27]+'...'
        toool = nice(subdef_map[subdefect][0]) if subdef_map[subdefect][1] > 0 else "-"
        print(sub, " & ", toool, " & ", "{:4.2f}".format(subdef_map[subdefect][1]), "\\\\")
    print("\\hline")
    print("\\end{tabular}")
    sys.stdout = sys.__stdout__


    
# Robust detection rate by subdefects
def subdefects_rdr(tex_file_name, rep_directory, latex_dir, tool_list):
    tex_file_path = os.path.join(latex_dir, tex_file_name)

    t_map = {}
    subdefects = set()
    subdef_map = {} # subdef |-> [(tool, rdr)]
    for tool in tool_list:
        c_total_path = os.path.join(rep_directory, tool, 'c_subdefects.csv')
        head, *tail = lines(c_total_path)
        cpp_total_path = os.path.join(rep_directory, tool, 'cpp_subdefects.csv')
        h, *t = lines(cpp_total_path)

        for line in tail + t:
            items = line.split(",")
            name = items[2]
            subdefects.add(name)
            if (not name in subdef_map.keys()):
                subdef_map[name] = []
            
            rdc = int(items[9].strip())
            var = int(items[5].strip())
            rdr  = round((rdc * 100) / var, 2)
            subdef_map[name] = subdef_map[name] + [(tool, rdr)]

    for subdef in subdef_map.keys():
        # print(subdef,":")
        # print(subdef_map[subdef])
        srt = sorted(subdef_map[subdef], key = lambda x : x[1])
        srt.reverse()
        subdef_map[subdef] = srt[0]
        # print(subdef_map[subdef])
        # print("\n\n")

    sys.stdout = open(tex_file_path, "w")
    print("\\begin{tabular}{|l|c|r|}")
    print("%\\hline")
    print("% Robust detection rate per subdefects \\\\ ")
    print("\\hline")
    print("\multicolumn{1}{|c|}{Defect subtype} & \multicolumn{1}{|c|}{Tool} & \multicolumn{1}{|c|}{RDR}", "\\\\")
    print("\\hline")
    for subdefect in sorted(subdef_map.keys()):
        sub = subdefect if len(subdefect) <= 20 else subdefect[0:27]+'...'
        toool = nice(subdef_map[subdefect][0]) if subdef_map[subdefect][1] > 0 else "-"
        print(sub, " & ", toool, " & ", "{:4.2f}".format(subdef_map[subdefect][1]), "\\\\")
    print("\\hline")
    print("\\end{tabular}")
    sys.stdout = sys.__stdout__

    
# Unique by subdefects
def subdefects_unique(tex_file_name, rep_directory, latex_dir, tool_list):
    tex_file_path = os.path.join(latex_dir, tex_file_name)

    t_map = {}
    subdefects = set()
    subdef_map = {} # subdef |-> [(tool, unique)]
    for tool in tool_list:
        c_total_path = os.path.join(rep_directory, tool, 'c_subdefects.csv')
        head, *tail = lines(c_total_path)
        cpp_total_path = os.path.join(rep_directory, tool, 'cpp_subdefects.csv')
        h, *t = lines(cpp_total_path)

        for line in tail + t:
            items = line.split(",")
            name = items[2]
            subdefects.add(name)
            if (not name in subdef_map.keys()):
                subdef_map[name] = []
            
            rdc = int(items[11].strip())
            subdef_map[name] = subdef_map[name] + [(tool, rdc)]

    for subdef in subdef_map.keys():
        # print(subdef,":")
        # print(subdef_map[subdef])
        srt = sorted(subdef_map[subdef], key = lambda x : x[1])
        srt.reverse()
        subdef_map[subdef] = srt[0]
        # print(subdef_map[subdef])
        # print("\n\n")

    sys.stdout = open(tex_file_path, "w")
    print("\\begin{tabular}{|l|c|c|}")
    print("%\\hline")
    print("% Unique per subdefects \\\\ ")
    print("\\hline")
    print("\multicolumn{1}{|c|}{Defect subtype} & \multicolumn{1}{|c|}{Tool} & \multicolumn{1}{|c|}{Unique}", "\\\\")
    print("\\hline")
    for subdefect in sorted(subdef_map.keys()):
        sub = subdefect if len(subdefect) <= 20 else subdefect[0:27]+'...'
        toool = nice(subdef_map[subdefect][0]) if subdef_map[subdefect][1] > 0 else "-"

        print(sub, " & ", toool, " & ", subdef_map[subdefect][1], "\\\\")
    print("\\hline")
    print("\\end{tabular}")
    sys.stdout = sys.__stdout__


# Detected by all by subdefects
def subdefects_all(tex_file_name, rep_directory, latex_dir, tool_list):
    tex_file_path = os.path.join(latex_dir, tex_file_name)

    t_map = {}
    subdefects = set()
    subdef_map = {} # subdef |-> [tools]
    subdef_files = {}
    for tool in tool_list:
        c_total_path = os.path.join(rep_directory, tool, 'c_subdefects.csv')
        head, *tail = lines(c_total_path)
        cpp_total_path = os.path.join(rep_directory, tool, 'cpp_subdefects.csv')
        h, *t = lines(cpp_total_path)

        for line in tail + t:
            items = line.split(",")
            name = items[2]
            subdefects.add(name)
            if (not name in subdef_map.keys()):
                subdef_map[name] = []
                subdef_files[name] = []
            
            rdc = int(items[11].strip())
            tp = int(items[3].strip())
            filename = items[0].strip()
            subdef_map[name] = subdef_map[name] + [(tool, tp)]
            if not (filename in subdef_files[name]):
                subdef_files[name] = subdef_files[name] + [filename]
            else:
                subdef_files[name] = subdef_files[name]

    for subdef in subdef_map.keys():
        srt = list(filter(lambda x : x[1] != 0, subdef_map[subdef]))
        subdef_map[subdef] = srt;

    
    sys.stdout = open(tex_file_path, "w")                                                                             #
    print("\\begin{tabular}{|l|l|l|}")                                                                                #
    print("%\\hline")                                                                                                 #
    print("% Subdefects detected by \\\\ ")                                                                            #
    print("\\hline")                                                                                                  #
    print("{Defect subtype} & {Tools which detected this subtype} & {Filenames}", "\\\\") #
    print("\\hline")                                                                                                  #
    for subdefect in sorted(subdef_map.keys()):                                                                       #
        sub = subdefect if len(subdefect) <= 20 else subdefect[0:27]+'...'                                            #
        toool = ",".join(list(map (lambda x : x[0], subdef_map[subdefect])))
        fnames = ",".join(list(map (lambda x : str(x.replace("_", "\\_")), subdef_files[subdefect])))
                                                                                                                      #
        print(sub, " & ", toool, " & ", fnames, "\\\\")                                             #
    print("\\hline")                                                                                                  #
    print("\\end{tabular}")                                                                                           #
    sys.stdout = sys.__stdout__                                                                                       #
    
