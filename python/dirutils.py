from os import listdir
from os.path import isfile, join

def list_files(directory, extension, absolute_path=False):
    files = []

    for f in listdir(directory):
        fpath = join(directory, f)
        if isfile(fpath) and fpath.endswith(extension):
            files.append(fpath)
    return files
