import os
import sys
from os import listdir
from os.path import isfile, join

def list_files(directory, extension, absolute_path=False):
    files = []

    for f in listdir(directory):
        fpath = join(directory, f)
        if isfile(fpath) and fpath.endswith(extension):
            files.append(fpath)
    return files

def append_in(file_path, text):
    sys.stdout = open(file_path, "a")
    print(text)
    sys.stdout = sys.__stdout__

def reset_file(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)
    sys.stdout = open(file_path, "w")
    sys.stdout = sys.__stdout__

def file_line_error_header(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)
    sys.stdout = open(file_path,"w")
    print("File, Line, Error")
    sys.stdout = sys.__stdout__
    
def tool_exec_log(file_path, cmd, out, err, exit):
    sys.stdout = open(file_path, "a")
    print("[CMD]: " + cmd) 
    print("[OUTPUT]:\n" + out.decode("utf-8"))
    print("[ERR]:\n" + err.decode("utf-8"))
    print("[EXIT]: " + str(exit) + "\n")
    sys.stdout = sys.__stdout__
    