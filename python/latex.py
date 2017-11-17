import os
import sys

def lines(file_path):
    with open(file_path) as f:
        return f.read().splitlines()

    
def total(tex_file_name, rep_directory, tool_list):
    tex_file_path = os.path.join(rep_directory, tex_file_name)

    l = []
    for tool in tool_list:
        c_total_path = os.path.join(rep_directory, tool, 'c_total.csv')
        items = lines(c_total_path)[1].split(",");
        dr  = float(items[3].strip())
        fpr = float(items[4].strip())
        pr  = float(items[5].strip())
        rdr = float(items[7].strip())
        uni = int(items[8].strip())

        timing_path = os.path.join(rep_directory, tool, 'timing.csv')
        timing = lines(timing_path)[0].split(",")
        runtime = round(float(timing[1].strip()) + float(timing[2].strip()), 2)

        # put everything in a tuple
        l.append((tool, dr, fpr, pr, rdr, uni, runtime))

    srt = sorted(l, key = lambda x : x[3])
    srt.reverse()

    sys.stdout = open(tex_file_path, "w")
    print("\\begin{tabular}{|l|c|c|c|c|c|c|}")
    print("\\hline")
    print("Tool & DR & FPR & PR & RDR & Unique & Time (s) \\\\ ")
    print("\\hline")
    for t in srt:
        t_as_list = map(lambda x : str(x), list(t))
        print(' & '.join(t_as_list),"\\\\")
        
    print("\\hline")
    print("\\end{tabular}")
    sys.stdout = sys.__stdout__
    
