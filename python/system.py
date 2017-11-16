import shlex
from subprocess import Popen, PIPE
import time


# simply run a system command and return the needed info
def system_call(cmd, dir="."):
    print("[CMD]:", cmd)
    vtime = time.time();
    process = Popen(shlex.split(cmd), stdout=PIPE, stderr=PIPE, cwd=dir)
    (output, err) = process.communicate()
    exit_code = process.wait()
    if (exit_code == 0):
        print("[DONE]", "\n")
    else:
        print("[FAILED]:", err.decode("utf-8"))
        print("[EXIT CODE]:", exit_code)
#    print("[OUTPUT]:", output)
    vtime = round(time.time() - vtime, 3);
    return (output, err, exit_code, vtime)
