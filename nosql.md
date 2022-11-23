#Modeling, Implementing and Querying Mongodb.

MongoDB is a nosql database that stores data in JSON-like documents.
For this task, I used the MongoDBcompass application.
The Mongo DB compass is a GUI application for the MongoDB database. 
This application can be used to store NoSQL databases as a document store database without necesarily having to hard code it with python.
Document stores/ document-oriented databse is specifically used for storing document-oriented information.
The data stored in such databses are known as semi-structured data.
The semi-structured data is different form data stored in Relational databses which needs to be normalized and requires primary keys.
Document-oriented databases are encoded mainly in JSON or in XML 

## Data
The station to be used is station 270 in Wells road. The total number readings from that
station is 1000. The readings taken at this station will be saved in a readings collection in a mongodb database. Unlike
sql, mongodb database schemas is dynamic  making them responsive to changes in the structure of data.This decreases the 
amount of space needed to store data in the database and the processing time for retrieval. 


##Implementation
I used the MOngo DB application to answer the task 5 question.
while querying the database I got the following results

```
Query result

```
```
{
    "_id": {
        "$oid": "61e98d138a755ae2a0797a52"
    },
    "stationid": "270",
    "location": "Wells Road",
    "geo_point_2d": "51.4278638883,-2.56374153315",
    "readingid": "3",
    "datetime": "2013-08-23 14:00:00",
    "nox": "197.75",
    "no2": "73.25",
    "no": "81.25",
    "pm10": "0",
    "nvpm10": "0",
    "vpm10": "0",
    "mvpm2": [null, null, null, null, null, "0"],
    "pm2": [null, null, null, null, null, "0"],
    "vpm2": [null, null, null, null, null, "0"],
    "co": "0",
    "o3": "0",
    "so2": "0",
    "temperature": "0",
    "rh": "0",
    "airpressure": "0",
    "datestart": "2003-05-23 00:00:00",
    "dateend": "0000-00-00 00:00:00",
    "current": "TRUE",
    "instrumenttype": "Continuous (Reference)"
}
```

```
{
    "_id": {
        "$oid": "61e98d138a755ae2a0797a53"
    },
    "stationid": "270",
    "location": "Wells Road",
    "geo_point_2d": "51.4278638883,-2.56374153315",
    "readingid": "14",
    "datetime": "2013-08-24 03:00:00",
    "nox": "23.5",
    "no2": "12.75",
    "no": "6.75",
    "pm10": "0",
    "nvpm10": "0",
    "vpm10": "0",
    "mvpm2": [null, null, null, null, null, "0"],
    "pm2": [null, null, null, null, null, "0"],
    "vpm2": [null, null, null, null, null, "0"],
    "co": "0",
    "o3": "0",
    "so2": "0",
    "temperature": "0",
    "rh": "0",
    "airpressure": "0",
    "datestart": "2003-05-23 00:00:00",
    "dateend": "0000-00-00 00:00:00",
    "current": "TRUE",
    "instrumenttype": "Continuous (Reference)"
}
```

```
{
    "_id": {
        "$oid": "61e98d138a755ae2a0797a54"
    },
    "stationid": "270",
    "location": "Wells Road",
    "geo_point_2d": "51.4278638883,-2.56374153315",
    "readingid": "40",
    "datetime": "2013-08-25 05:00:00",
    "nox": "43.75",
    "no2": "22.25",
    "no": "14.25",
    "pm10": "0",
    "nvpm10": "0",
    "vpm10": "0",
    "mvpm2": [null, null, null, null, null, "0"],
    "pm2": [null, null, null, null, null, "0"],
    "vpm2": [null, null, null, null, null, "0"],
    "co": "0",
    "o3": "0",
    "so2": "0",
    "temperature": "0",
    "rh": "0",
    "airpressure": "0",
    "datestart": "2003-05-23 00:00:00",
    "dateend": "0000-00-00 00:00:00",
    "current": "TRUE",
    "instrumenttype": "Continuous (Reference)"
}
```