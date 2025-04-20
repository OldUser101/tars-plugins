# tars plugins

This is the repository of standard plugins for tars. See [the tars repository](https://github.com/OldUser101/tars) for more information on tars.

## Installing

tars uses the `~/.tars/plugins` directory to store plugins by default.

### Method 1: Script

Download and run the install script:

`wget -O ~/tars-plugins-install.sh https://raw.githubusercontent.com/OldUser101/tars-plugins/refs/heads/main/install.sh && chmod +x ~/tars-plugins-install.sh && ~/tars-plugins-install.sh && rm ~/tars-plugins-install.sh`

### Method 2: Manual

To use the plugins in this repository, just clone with:

`git clone https://github.com/OldUser101/tars-plugins.git`

to any directory of your choice.

And then copy all the Python (.py) files to `~/.tars/plugins`:

`cp /path/where/you/cloned/*.py ~/.tars/plugins/`

You may need to run the following if the plugins directory does not exist yet:

`mkdir -p ~/.tars/plugins`

## Notes

If you are working on these plugins, or are making your own, you may find the `copy-all.tars` package configuration useful.

This will just copy all Python (*.py) files in the current directory to `/.tars/plugins`.

To use this, you will need a working tars, and the `fs:copy` transform from this repository.

## More Information

If you want more information on plugins and their development, check out [the main tars repository](https://github.com/OldUser101/tars) and read the "Plugins" section of the Readme.

## Plugins

### fs

`fs` contains transforms for local file operations

 - `fs:copy`: copy files from `src` to `dest`, supports wildcards
 - `fs:copy2`: copy files from `src` to `dest`, preserving metadata, supports wildcards
 - `fs:copytree`: copies a complete directory tree from `src` to `dest`
 - `fs:move`: moves files and directories from `src` to `dest`, supports wildcards
 - `fs:remove`: removes a file at `target`
 - `fs:rmtree`: removes the directory tree, including files, at `target`
 - `fs:rmdir`: removes an empty directory at `target`
 - `fs:mkdir`: creates an empty directory at `target`, including intermediate directories
 - `fs:exists`: breaks if `target` doesn't exist
 - `fs:isdir`: breaks if `target` is not a directory
 - `fs:isfile`: breaks if `target` is not a file
 - `fs:chmod`: changes permissions of `target`, to `mode`, a valid mode integer
 - `fs:symlink`: creates a symlink with `target` as the target and `dest` as the link name
 - `fs:rename`: renames a file or directory `src` to `dest`
 - `fs:touch`: sets the timestamp on `target`, can also create files

### sh

`sh` contains transforms for shell commands

 - `sh:exec`: execute `cmd` in the default shell with the working directory `cwd` or default.
