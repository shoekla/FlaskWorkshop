echo "Installing Necessities for Flask Workshop\n"
sudo python getpip.py
sudo pip install flask
sudo pip install requests
sudo pip install bs4
sudo pip install BeautifulSoup


echo "TESTING INSTALLATION ---------------------------\n"

python testInstallation.py



echo "ASK ORGANIZER If you see an error message above------\n"
timeout /t -1
