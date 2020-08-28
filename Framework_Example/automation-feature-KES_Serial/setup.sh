#!/bin/bash

if [[ "$(python3 -V)" =~ "Python 3" ]]
then 
	echo "Python 3 is installed"
	echo "$(python3 -V)"
else
	sudo apt install python3
fi

sudo apt install python3-pip -y &>/dev/null

rm -rf ~/.local

pip3 install -r requirements.txt

