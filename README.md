# Spotter_Activation
A Spotter Activation script
It checks the NWS Hazardous weather Statement for the phrase "Spotter Activation is expected" 
  If true then it pushes the activation message thru Notify-run chrome to my phone and laptop. 
  
Installation Instructions:
Pre-requisite installs:
BeautifulSoup4
Python3
notify_run
regex

Run the command "Notify-run register"
Scan the QR code with the Notification Device and set notifications to "Allow"

Install the spotter activation script
change the URL to match your county/region website. 

Setup a cronjob to execute the script every x hours 

"0 0/6 * * * python3 /home/pi/spotter_activation.py >> /home/pi/log.txt 2>&1"

All is complete 
