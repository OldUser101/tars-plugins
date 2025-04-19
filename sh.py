import subprocess
import os

def sh_exec(cfg):
    cmd = ""
    cwd = os.getcwd()

    if "cmd" in cfg:
        cmd = cfg["cmd"]
    if "cwd" in cfg:
        cwd = cfg["cwd"]

    if cmd == "":
        return 1

    return subprocess.run(cmd, shell=True, cwd=cwd).returncode

def register(ctx):
    ctx.register_transform("exec", sh_exec)