sudo yum install python-pip
sudo pip install --upgrade pip
sudo pip install flask
sudo curl --fail -sSLo /etc/yum.repos.d/passenger.repo https://oss-binaries.phusionpassenger.com/yum/definitions/el-passenger.repo
sudo yum install -y mod_passenger || sudo yum-config-manager --enable cr && sudo yum install -y mod_passenger
sudo mkdir /var/www/lab8
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null && pwd )"
sudo cp -R $DIR /var/www/lab8
cat > /etc/httpd/conf.d/myapp.conf << EOF
<VirtualHost *:80>
    DocumentRoot /var/www/myapp/
    PassengerAppRoot /var/www/myapp/
    PassengerAppType wsgi
    PassengerStartupFile passenger_wsgi.py

    <Directory /var/www/myapp>
      Allow from all
      Options -MultiViews
      Require all granted
    </Directory>
</VirtualHost>
EOF
sudo service httpd restart
