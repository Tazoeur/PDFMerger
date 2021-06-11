#!/bin/bash
# You can either store this project in `/opt/scripts/pdfmerger`
# Or you can create a symbolic link of this project to `/opt/scripts/pdfmerger`
# Then you only need to add an alias in your `~/.bashrc` file
# alias pdfmerge="/opt/scripts/pdfmerger/pdfmerger.sh"
/opt/scripts/pdfmerger/venv/bin/python /opt/scripts/pdfmerger/main.py "$@"
