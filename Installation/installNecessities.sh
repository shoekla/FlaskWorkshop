#!/bin/sh
#chmod u+x
echo "Installing Necessities for Flask Workshop\n"
BASEDIR=$(dirname "$0")
cd $BASEDIR
python getpip.py
pip install flask
pip install requests
pip install bs4
pip install BeautifulSoup
BLUE='\033[1;34m'
  
echo "${BLUE}TESTING INSTALLATION ---------------------------\n"
python testInstallation.py


echo "${BLUE}ASK ORGANIZER If you see an error message above------\n"
echo "Press enter to exit"
read "..."








