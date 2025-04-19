#!/bin/bash

# Installs tars standard plugins for the current running user

cd ~
git clone https://github.com/OldUser101/tars-plugins.git
mkdir -p ~/.tars/plugins
cp ~/tars-plugins/*.py ~/.tars/plugins/
rm -rf ~/tars-plugins