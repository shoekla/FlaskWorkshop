#!/bin/sh
#chmod u+x
echo "Installing Necessities for Flask Workshop\n"
BASEDIR=$(dirname "$0")
cd $BASEDIR
sudo python getpip.py
sudo pip install flask
sudo pip install requests
sudo pip install bs4
sudo pip install BeautifulSoup
BLUE='\033[1;34m'
WHITE='\033[1;37m'  
echo "${BLUE}TESTING INSTALLATION ---------------------------\n"
python testInstallation.py


echo "${BLUE}ASK ORGANIZER If you see an error message above------\n"
echo "${WHITE}Press enter to exit"
read "..."








