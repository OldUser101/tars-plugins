import os, shutil, glob

TARS_FS_OPERATIONS = [
    "copy",
    "copy2", 
    "copytree",
    "move",
    "remove",
    "rmtree",
    "rmdir",
    "mkdir",
    "exists",
    "isdir",
    "isfile",
    "chmod",
    "symlink",
    "rename",
    "touch"
]

class TarsFs:
    def __init__(self):
        self.src = ""
        self.dst = ""
        self.tgt = ""
        self.op = ""
        self.cfg = {}
        self.__operations = {
            "copy": self.fs_copy,
            "copy2": self.fs_copy2,
            "copytree": self.fs_copytree,
            "move": self.fs_move,
            "remove": self.fs_remove,
            "rmtree": self.fs_rmtree,
            "rmdir": self.fs_rmdir,
            "mkdir": self.fs_mkdir,
            "exists": self.fs_exists,
            "isdir": self.fs_isdir,
            "isfile": self.fs_isfile,
            "chmod": self.fs_chmod,
            "symlink": self.fs_symlink,
            "rename": self.fs_rename,
            "touch": self.fs_touch
        }

    def load_from_config(self, cfg):
        if "src" in cfg:
            self.src = os.path.expanduser(cfg["src"])

        if "dest" in cfg:
            self.dst = os.path.expanduser(cfg["dest"])

        if "target" in cfg:
            self.tgt = os.path.expanduser(cfg["target"])

        self.op = str(cfg["transform"]).split(":")[1]
        self.cfg = cfg

        return 0

    def run(self):
        if self.op in self.__operations:
            return self.__operations[self.op]()
        return 1

    def fs_copy(self):
        matched = glob.glob(self.src)
        if not matched:
            return 1

        if len(matched) > 1 or os.path.isdir(self.src) or '*' in self.cfg["src"]:
            for f in matched:
                shutil.copy(f, os.path.join(self.dst, os.path.basename(f)))
        else:
            shutil.copy(matched[0], self.dst)     

        return 0
    
    def fs_copy2(self):
        matched = glob.glob(self.src)
        if not matched:
            return 1

        if len(matched) > 1 or os.path.isdir(self.src) or '*' in self.cfg["src"]:
            for f in matched:
                shutil.copy2(f, os.path.join(self.dst, os.path.basename(f)))
        else:
            shutil.copy2(matched[0], self.dst)     

        return 0
    
    def fs_copytree(self):
        shutil.copytree(self.src, self.dst)
        return 0
    
    def fs_move(self):
        matched = glob.glob(self.src)
        if not matched:
            return 1
    
        if len(matched) > 1 or os.path.isdir(self.src) or '*' in self.cfg["src"]:
            for f in matched:
                shutil.move(f, os.path.join(self.dst, os.path.basename(f)))
        else:
            shutil.move(matched[0], self.dst)

        return 0

    def fs_remove(self):
        os.remove(self.tgt)
        return 0
    
    def fs_rmtree(self):
        shutil.rmtree(self.tgt)
        return 0
    
    def fs_rmdir(self):
        os.rmdir(self.tgt)
        return 0
    
    def fs_mkdir(self):
        os.makedirs(self.tgt, exist_ok=True)
        return 0

    def fs_exists(self):
        if os.path.exists(self.tgt):
            return 0
        return 1
    
    def fs_isdir(self):
        if os.path.isdir(self.tgt):
            return 0
        return 1
    
    def fs_isfile(self):
        if os.path.isfile(self.tgt):
            return 0
        return 1
    
    def fs_chmod(self):
        if "mode" not in self.cfg:
            return 1
        
        os.chmod(self.tgt, int(self.cfg["mode"]))
        return 0
    
    def fs_symlink(self):
        os.symlink(self.target, self.dst)
        return 0
    
    def fs_rename(self):
        os.rename(self.src, self.dst)
        return 0
    
    def fs_touch(self):
        open(self.tgt, "a").close()
        return 0

def fs_run(cfg):
    tfs = TarsFs()
    res = tfs.load_from_config(cfg)

    if res != 0:
        return res
    
    return tfs.run()

def register(ctx):
    for op in TARS_FS_OPERATIONS:
        ctx.register_transform(op, fs_run)