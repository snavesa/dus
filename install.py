#!/bin/bash

#install python2.7 python-pip
sudo apt install python2.7 python-pip -y

#check to make sure Python is installed
python --version

#install the python requests module
sudo apt-get install python-requests -y

#install sqlite3
sudo apt-get install sqlite3 -y

#set some necessary permissions
cd /home
sudo useradd -m -s /bin/bash pan_dhcp
sudo chmod 755 pan_dhcp
cd pan_dhcp
sudo mkdir pan_dhcp
chmod 777 pan_dhcp
cd pan_dhcp

#create the devices database
echo 'CREATE TABLE DevicesDynamic (DeviceName "TEXT", DeviceMac "TEXT", Groups "Text");' > create.sql
sqlite3 devices.sql < create.sql
sudo rm create.sql
chmod 777 devices.sql

#install the code that updates the firewall
wget https://raw.githubusercontent.com/snavesa/dus/master/dhcp.py
sudo chmod 777 dhcp.py

#update cron to execute the script every minute
cd /etc/cron.d
sudo wget https://raw.githubusercontent.com/snavesa/dus/master/pan_dhcp_cron

#install apache2 and configure it to allow cgi
sudo apt-get install apache2 -y
sudo a2enmod cgid
sudo service apache2 restart

#copy cgi scripts into the cgi directory
cd /usr/lib/cgi-bin
sudo wget https://raw.githubusercontent.com/snavesa/dus/master/index.cgi
sudo chmod 755 index.cgi
sudo wget https://raw.githubusercontent.com/snavesa/dus/master/keygen.cgi
sudo chmod 755 keygen.cgi

#copy default web page
cd /var/www/html
sudo rm index.html
sudo wget https://raw.githubusercontent.com/snavesa/dus/master/index.html
sudo chmod 755 index.html
sudo wget https://raw.githubusercontent.com/snavesa/dus/master/dus.css
sudo chmod 755 dus.css
sudo wget https://raw.githubusercontent.com/snavesa/dus/master/logo.svg
sudo chmod 755 logo.svg
