import os 
import uuid
import pika 
import hashlib
import json
import psycopg2
from zipfile import ZipFile
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message
import zipfile
import datetime


import smtplib
import smtplib
from db_connection import get_shared_db_connection


connection = get_shared_db_connection()
cursor = connection.cursor()

def enterTH(job_id , trailHash):
	query="update malware_table set status = %s,trailhash = %s where job_id = %s"
	query2="select * from malware_table where job_id = %s"
	cursor.execute(query,(2,trailHash,job_id,))
	result = cursor.fetchone
	if result:
		cursor.execute(query2,(job_id,))
		result2 = cursor.fetchone()
		Job_id = result2[0]
		return Job_id
		
	else:
		return -1
print(enterTH(21,1727932818126))
	
