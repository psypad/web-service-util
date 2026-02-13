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
def getUID(job_id):
    query = "SELECT user_id FROM request_table WHERE job_id = %s"
    cursor.execute(query, (job_id,))
    result = cursor.fetchall()  # Fetch all matching rows

    if result:
        # Extract user_ids from the result tuples
        user_ids = [row[0] for row in result]  # row[0] gets the user_id from each tuple
        return user_ids
    else:
        return [-1]  # Return [-1] if no results are found

print(getUID(21))

	
