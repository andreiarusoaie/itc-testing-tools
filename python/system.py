import shlex
from subprocess import Popen, PIPE
import time


# simply run a system command and return the needed info
def system_call(cmd, dir="."):
    vtime = time.time();
    process = Popen(shlex.split(cmd), stdout=PIPE, stderr=PIPE, cwd=dir)
    (output, err) = process.communicate()
    exit_code = process.wait()
    vtime = round(time.time() - vtime, 5);
    return (output, err, exit_code, vtime)
