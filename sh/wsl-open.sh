#!/bin/bash

# wsl open
# opens a file or url with the default program 
# on a Windows system equipped with WSL

if [ -e $1 ]; then
	/bin/bash -c "powershell.exe -Command Start-Process \`wslpath -aw $1\`"
else
	/bin/bash -c "powershell.exe -Command Start-Process $1"
fi
