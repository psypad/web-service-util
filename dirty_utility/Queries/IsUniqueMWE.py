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


import datetime

import datetime
import time


def checkMalware(filehash):
	query = "select * from malware_table where filehash = %s"
	cursor.execute(query,(filehash,))
	result = cursor.fetchone()
	if result:
		jobId = result[0]
		trail = result[2]
		status= result[4]
		return  status,trail
	else:
		return -1,-1
		
	
	
status,th = checkMalware('aa')
print(status)
print(th)
			


 

