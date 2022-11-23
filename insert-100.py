import pandas as pd
from sqlalchemy import create_engine
import pymysql

'''
If pymysql is not installed, use the command conda install -c anaconda pymysql to install it
If pymongo is not installed, use the command conda install -c anaconda pymongo dnspython to install it as well
'''

# user:password
conn_str = 'mysql+pymysql://root:root@localhost/pollution-db2'
conn = create_engine(conn_str).connect()

def parse_if_None(value):
    if value:
        return value
    return 'NULL'

def to_string(value):
    return '"' + value + '"'

select_100 = "SELECT * FROM reading LIMIT 100"

sql_str = 'INSERT INTO reading VALUES'
for row in conn.execute(select_100):
    sql_str = sql_str + (' ({0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11}, {12}, {13}, {14}, {15}, {16}, {17}, {18}, {19}, {20}, {21}, {22}, {23}),'
                         .format(parse_if_None(row[0]), to_string(row[1]) if row[1] else 'NULL', parse_if_None(row[2]), parse_if_None(row[3]), parse_if_None(row[4]), 
                                 parse_if_None(row[5]), parse_if_None(row[6]), parse_if_None(row[7]), parse_if_None(row[8]), parse_if_None(row[9]), 
                                 parse_if_None(row[10]), parse_if_None(row[11]), parse_if_None(row[12]), parse_if_None(row[13]), parse_if_None(row[14]), 
                                 parse_if_None(row[15]), parse_if_None(row[16]), parse_if_None(row[17]), to_string(row[18]) if row[18] else 'NULL', to_string(row[19]) if row[19] else 'NULL', 
                                 to_string(row[20]) if row[20] else 'NULL', to_string(row[21]) if row[21] else 'NULL', parse_if_None(row[22]), to_string(row[23]) if row[23] else 'NULL'))

if sql_str[-1] == ',':
    sql_str = sql_str[:-1] + ';'


f = open("insert-100.sql", "w+")
f.write(sql_str)
f.close()