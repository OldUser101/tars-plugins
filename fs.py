import os, shutil, glob

def fs_copy(cfg):
    if "src" not in cfg or "dest" not in cfg:
        return 1

    src = os.path.expanduser(cfg["src"])
    dest = os.path.expanduser(cfg["dest"])

    matched = glob.glob(src)
    if not matched:
        return 0

    if len(matched) > 1 or os.path.isdir(src) or '*' in cfg["src"]:
        os.makedirs(dest, exist_ok=True)
        for f in matched:
            shutil.copy2(f, os.path.join(dest, os.path.basename(f)))
    else:
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        shutil.copy2(matched[0], dest)

    return 0

def register(ctx):
    ctx.register_transform("copy", fs_copy)