#FLASK + PYTHON INSTALL

# Update Packages
sudo apt-get update
sudo apt-get install -y apache2
sudo apache2ctl configtest

# remove firewll
sudo ufw app list
sudo ufw app info "Apache Full"
sudo ufw allow in "Apache Full"


# install basics
sudo apt-get install -y libapache2-mod-wsgi python-dev
sudo a2enmod wsgi

# python pip
sudo apt-get update
sudo apt-get install python3-pip


# Install Flask
sudo pip install Flask 

# Basic Linux Stuff
apt-get install -y git

# Apache
apt-get install -y apache2

# Enable Apache Mods
a2enmod rewrite

#Add Onrej PPA Repo
apt-add-repository ppa:ondrej/php
apt-get update

# Restart Apache
service apache2 restart


# Set MySQL Pass
debconf-set-selections <<< 'mysql-server mysql-server/root_password password root'
debconf-set-selections <<< 'mysql-server mysql-server/root_password_again password root'

# Install MySQL
apt-get install -y mysql-server

# Restart Apache
sudo service apache2 restart