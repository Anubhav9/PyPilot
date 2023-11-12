"""
Utility methods for some of the most common database interactions (SQL)

Author: Anubhav Sanyal
Creation Date: 12/11/2023
"""

import logging
import os
import json
from mysql.connector import pooling

CONNECTION=None
DBCONFIG_GLOBAL=None

def establish_pool_connection(dbconfig_json,service_database_name):
    """
    Utility Method to establish PoolConnection with the Database

    Parameters
    dbconfig_json (json): JSON file containing DB Configuration
    service_database_name (string): Filter Out DB Details using this value
    """
    dbconfig=dbconfig_json[service_database_name]
    try:
        connection_pool=pooling.MySQLConnectionPool(pool_name="sql-pool",pool_size=10,**dbconfig)
        connection=connection_pool.get_connection()
        return connection
    except Exception as e:
        logging.error("Unable to establish pool connection due to error %s",e)
        return None


def execute_query(sql_query,params=None):
    """
    Utility Method to execute query in the database

    Parameters
    sql_query (string): SQL Query with Parameters to avoid SQL Injection
    params : Parameters passed to the query (optional)
    """
    try:
        cursor=CONNECTION.cursor()
        cursor.execute(sql_query,params)
        CONNECTION.commit()
    except Exception as e:
        logging.error("Unable to connect to MySQL DB with error as %s",e)



env=os.environ.get("ENV","local")
if env=="local":
    try:
        with open("../databases/database_config_local.json", 'r') as file:
            file_content=file.read()
            file_content=file_content.replace("{SENDGRID_DATABASE_PASSWORD}",os.environ.get("SENDGRAID_DATABASE_PASSWORD"))
            dbconfig_global=json.load(file_content)
    except Exception as e:
        logging.error("Unable to open file because of Error as %s",e)

CONNECTION=establish_pool_connection(DBCONFIG_GLOBAL,"SENDGRID_SQL_DB")
