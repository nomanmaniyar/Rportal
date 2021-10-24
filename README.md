# Rportal
Residential Management System

Systeam requirements
 
1. Python
2. Mysql
------------------------------------------------------------------------------------
Config SQL Database

1. install MySql
2. set localhost password :- 1234
3. You can Change Password and Other Credentials in Credential File
4. Rportal\config\credentials.py   

Add SQL file

1. Folder: Rportal\config\database\3 databse rportal.sql
2. In your MySql Database Set database name as a "rportal" 
3. Run SQL File in MySqlWorkBench
------------------------------------------------------------------------------------
Project run commands in cmd 

optional install VIRTUAL ENVIRONMENT 

1. cd Rportal\venv\Scripts
2. activate
3. pip install Flask
4. pip install flask_mysqldb
5. pip install Flask_Mail
6. cd..
7. python main.py
8. open link in your browser :- 127.0.0.1:5000/
