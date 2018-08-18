## Bible Rest API

**Installation**

```
pip install pipenv

pipenv install
```

**MYSQL setup**

```
sudo apt-get install python3-dev libmysqlclient-dev

pipenv install mysqlclient

sudo apt-get install mysql-server
```

### Setup the mysql as the following

- Open MySQL shell
     ```
     $ mysql -u <user> -p
     ```
- Inside shell
     ```
     >> create database <your_db_name> character set utf8;
     >> create user '<your_db_username>@localhost' identified by '<your_db_pass>'
     >> grant all on <your_db_name>.* to <your_db_username>;
     >> flush privileges;
     >> exit
     ```

**Please note : I am using django-environ for hiding secrets in my settings.py .Check Project url for [setup](https://github.com/joke2k/django-environ)
