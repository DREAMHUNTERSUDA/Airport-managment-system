# Airport Management System 

## Install components

 apt-get update
 apt-get install python-pip python-dev mysql-server libmysqlclient-dev
apt-get install wkhtmltopdf
```

### Setting up MySQL 
```bash
 mysql_secure_installation
mysql -u root -p
create database airportdb character set utf8;
create user airportuser@localhost identified by 'SUDA@1610';
grant all privileges on airportdb.* to airportuser@localhost;
flush privileges;
exit
```

### Setting up Virtual Environment and Install Requirements
```bash
 pip install virtualenv
python3 -m venv myvenv
source myvenv/bin/activate
pip3 install -r requirements.txt
```

### Running the project
```bash
cd ~/Airport_Management-System
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```


