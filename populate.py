# module imports
import mariadb
import sys
import csv
from datetime import datetime
import re

try:
    # set the user and password
    # connect to mariaDB platform
    conn = mariadb.connect(
        user="root",
        password="",
        host="127.0.0.1",     # localhost will also do
        port=3306             # possibly some other port
    )

    # make and get the cursor
    cur = conn.cursor()

    cur.execute("DROP DATABASE IF EXISTS `pollution-db2`")
    cur.execute("CREATE DATABASE `pollution-db2`") 

 # empty list to hold records
    records = [];

    # read in the csv file as a list one at a time
    with open('clean.csv','r') as csvfile: 
        reader = csv.reader(csvfile, delimiter=',') 
        for row in reader:
            records.append(row)
        
    # records[] is now a list of lists
    
    # get rid of the header row
    records.pop(0)
	  # get a database handle
    cur.execute("USE `pollution-db2`")
    
    # define the SQL for the tables
    stations_sql = """CREATE TABLE `stations` (
          `stationid` int(11) NOT NULL,
             `location` varchar(48) DEFAULT NULL,
            `geo_point_2d` varchar(45) DEFAULT NULL
              );"""
    
    readings_sql = """CREATE TABLE `readings` (
  `readingid` int(11) NOT NULL,
  `datetime` datetime DEFAULT NULL,
  `nox` float NOT NULL,
  `no2` float DEFAULT NULL,
  `no` float DEFAULT NULL,
  `pm10` float DEFAULT NULL,
  `nvpm10` float DEFAULT NULL,
  `vpm10` float DEFAULT NULL,
  `mvpm2.5` float DEFAULT NULL,
  `pm2.5` float DEFAULT NULL,
  `vpm2.5` float DEFAULT NULL,
  `co` float DEFAULT NULL,
  `o3` float DEFAULT NULL,
  `so2` float DEFAULT NULL,
  `temperature` double DEFAULT NULL,
  `rh` int(11) DEFAULT NULL,
  `airpressure` int(11) DEFAULT NULL,
  `datestart` datetime DEFAULT NULL,
  `dateend` datetime DEFAULT NULL,
  `current` tinytext,
  `instrumenttype` varchar(32) DEFAULT NULL,
  `stationid` int(11) DEFAULT NULL
);"""
            
    schema_sql = """CREATE TABLE `schema` (
  `measure` varchar(32) DEFAULT NULL,
  `description` varchar(64) DEFAULT NULL,
  `unit` varchar(24) DEFAULT NULL
);"""

            
    cur.execute(stations_sql)
    cur.execute(readings_sql)
    cur.execute(schema_sql)
	
	
	#Indexes for table `readings`

    cur.execute("ALTER TABLE `readings` ADD PRIMARY KEY (`readingid`), ADD KEY `stationid` (`stationid`);")


    #Indexes for table `stations`
    cur.execute("ALTER TABLE `stations` ADD PRIMARY KEY (`stationid`);")

    
    # add the relationships
    cur.execute("ALTER TABLE `readings` ADD CONSTRAINT `readings_ibfk_1` FOREIGN KEY (`stationid`) REFERENCES `stations` (`stationid`);")
    # get the current timestamp
	
	
    now = datetime.now()
    
    for row in records:
                
        # set the autocommit flag to false
        conn.autocommit = False 
        
        #insert station
        station_sql =  """INSERT IGNORE INTO stations values(%s, %s, %s)"""
        svalues = (row[5], row[18], row[19])
         
        cur.execute(station_sql, svalues)
        
        # get source id using SQL since using INSERT IGNORE above
        cur.execute("SELECT stationid FROM stations WHERE \
            stationid = ?", (row[5],))
        
        # set sid to query result
        stationid = cur.fetchone()[0]  
        
        #insert quote
        reading_sql = """INSERT INTO readings VALUES (%s, %s, %s, %s,%s, %s, %s, %s,%s, %s, %s, %s,%s, %s, %s, %s,%s, %s, %s, %s, %s, %s)"""
        qvalues = (row[0], row[1], row[2],row[3], row[4], row[6],row[7], row[8], row[9],row[10], row[11], row[12],row[13], row[14], row[15], row[16], row[17], row[20], row[21], row[22], row[23], row[5]) 
        
        cur.execute(reading_sql, qvalues)
        qval = cur.lastrowid
        
        # populate the  schema table
    schema_data = """
    INSERT INTO `schema` VALUES
    ('date time', 'Date and time of measurement', 'datetime'),
    ('nox', 'Concentration of oxides of nitrogen', 'μg/m3'),
    ('no2', 'Concentration of nitrogen dioxide', 'μg/m3'),
    ('no', 'Concentration of nitric oxide', 'μg/m3'),
    ('siteid', 'Site ID for the station', 'integer'),
    ('pm10', 'Concentration of particulate matter <10 micron diameter', 'μg/m3'),
    ('nvpm10', 'Concentration of non - volatile particulate matter <10 micron diameter', 'μg/m3'),
    ('vpm10', 'Concentration of volatile particulate matter <10 micron diameter', 'μg/m3'),
    ('nvpm2.5', 'Concentration of non volatile particulate matter <2.5 micron diameter', 'μg/m3'),
    ('pm2.5', 'Concentration of particulate matter <2.5 micron diameter', 'μg/m3'),
    ('vpm2.5', 'Concentration of volatile particulate matter <2.5 micron diameter', 'μg/m3'),
    ('co', 'Concentration of carbon monoxide', 'mg/m3'),
    ('o3', 'Concentration of ozone', 'μg/m3'),
    ('so2', 'Concentration of sulphur dioxide', 'μg/m3'),
    ('temperature', 'Air temperature', '°C'),
    ('rh', 'Relative Humidity', '%'),
    ('air pressure', 'Air Pressure', 'mbar'),
    ('location', 'Text description of location', 'text'),
    ('geo_point_2d', 'Latitude and longitude', 'geo point'),
    ('datestart', 'The date monitoring started', 'datetime'),
    ('dateend', 'The date monitoring ended', 'datetime'),
    ('currentb', 'Is the monitor currently operating', 'text'),
    ('instrument type', 'Classification of the instrument', 'text');
    """
    cur.execute(schema_data)
    print("successfully populate schema table")
        
    conn.commit()
    conn.close()
	
	# catch and report on any error
# exit with 1 (non-error scripts automatically exit with 0)
except BaseException as err:
    print(f"An error occured: {err}")
    sys.exit(1)