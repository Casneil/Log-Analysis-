# Log-Analysis-Udacity
Log Analysis Project for Udacity's FullStack Nanodegree

# DESCRIPTION
The aim of this project was to create a reporting tool that prints out information from the given dataase file within the console. This reporting tool was written in Python 2.7 using the psycopg2 module to connect to the database. The database_setup.py file within the project folder creates PostgreSQL database for a news website. The provided Python script uses the psycopg2 library to query the database and produce a report that answers the following three questions:

What are the most popular three articles of all time?
Who are the most popular article authors of all time?
On which days did more than 1% of requests lead to errors?

# How To Run The Programm
It is recommendable to use a virtual machine to ensure that you are using the same environment that this project was developed on,as this will limit possible errors. You can download Vagrant and VirtualBox to install and manage your virtual machine.

Download or clone the data provided by Udacity's Full-Stack Github Page. Unzip the file in order to extract newsdata.sql file which you will find inside the Vagrant folder.

Use vagrant up to bring the virtual machine online and then use vagrant ssh to login.

# Run these commands in the terminal from the directory where your vagrant is installed in:

1. psql -d news -f newsdata.sql To load the news database

2. Connect to the database using psql -d news.

3. Now execute the Python file - python logs.py.


