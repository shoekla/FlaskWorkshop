echo "Installing Necessities for Flask Workshop\n"
python getpip.py
pip install flask
pip install requests
pip install bs4
pip install BeautifulSoup


echo "TESTING INSTALLATION ---------------------------\n"

python testInstallation.py



echo "ASK ORGANIZER If you see an error message above------\n"
timeout /t -1
