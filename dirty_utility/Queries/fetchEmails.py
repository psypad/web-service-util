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
def getEmail(user_ids):
    # Create placeholders for each user_id in the tuple
    placeholders = ', '.join(['%s'] * len(user_ids))
    query = f"SELECT email FROM user_table WHERE user_id IN ({placeholders})"
    
    # Execute the query with the tuple of user_ids
    cursor.execute(query, user_ids)  # user_ids is already a tuple
    result = cursor.fetchall()  # Fetch all matching rows

    if result:
        # Extract emails from the result tuples
        emails = [row[0] for row in result]  # row[0] gets the email from each tuple
        return emails
    else:
        return [""]  # Return an empty string if no results are found

# Example call with a tuple
print(getEmail((21, 22)))

	
