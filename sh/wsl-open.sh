#!/bin/bash

# wsl open
# opens a file or url with the default program 
# on a Windows system equipped with WSL

if [ -e "$1" ]; then
	itemPathRaw=$(wslpath -aw "$1" )
	itemPathCleaned=$(echo "$itemPathRaw" | sed -e 's/\ /\` /g')
	powershell.exe -Command Start-Process "$itemPathCleaned"
else
	powershell.exe -Command Start-Process "$1"
fi
