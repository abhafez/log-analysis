## Project Name: News Website Logs Analysis Statistics ...
The first full-stack web development nanodegree project

### Overview
This project is a deep exercise using python and sql to query data out of a database and report analysis needs.

#### Requirements
[Vagrant](https://www.vagrantup.com/downloads.html) - A virtual environment builder and manager

[VirtualBox](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1) - An open source virtualiztion product.

#### The data
To download the data use next link in the terminal
```
wget https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip
```
This project makes use of the same Linux-based virtual machine (VM)
f you need to bring the virtual machine back online (with vagrant up), do so now. Then log into it with vagrant ssh.


If you need to bring the virtual machine back online (with vagrant up), do so now. Then log into it with vagrant ssh.
```
cd /vagrant
```

```
# Unzip this file then import news database using this command
psql -d news -f newsdata.sql
# Connect to the database using
psql -d news
# Here you can run queries provided in python file and get the same results
# Then run this to quit
psql \q
```
Running this command will connect to your installed database server and execute the SQL commands in the downloaded file, creating tables and populating them with data.

### Running the file
Python3 in included in vagrant
run the following command in the terminal
```
python3 catalog/log.py
```

### What does this report ?
it answers three questions
What are the most popular three articles of all time?
Who are the most popular article authors of all time?
On which days did more than 1% of requests lead to errors?