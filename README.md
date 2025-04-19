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

You may need to run teh following if the plugins directory does not exist yet:

`mkdir -p ~/.tars/plugins`

## Notes

If you are working on these plugins, or are making your own, you may find the `copy-all.tars` package configuration useful.

This will just copy all Python (*.py) files in the current directory to `/.tars/plugins`.

To use this, you will need a working tars, and the `fs:copy` transform from this repository.

## More Information

If you want more information on plugins and their development, check out [the main tars repository](https://github.com/OldUser101/tars) and read the "Plugins" section of the Readme.
