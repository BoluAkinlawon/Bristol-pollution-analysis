#Reflective Report of the tasks 1-5 


**Task 1**: For this task, I initially approached the cropping and cleaning with my previous knowledge of SQL where 
you use the delete statement to crop out unwanted rows of data.
Upon further studying, I began to use external python libraries such as pandas to properly visualize the data more easily and
crop out the unwanted data. Then I put the output into a new csv file.
For the second part of the task, I was able to use pandas more confortably and I was then able to clean out mismatches between the Site ID and the Location.
I was then able to crop the required data into another csv file.

**Task 2**: This task was generally easier to do since I had previous experience with MySQL. I was able to use MySQLworkbench
to create the required tables and  the entire structure including the relationships and the schema.

**Task3**: For this task, I was able to use the pymysql library to create the tables and populate them using the clean.csv file that had been generated from the 
Task 2b work. i initially ran into a roadblock when attempting the task. I tried a number of modules like sqlalchemy before going back to the lecture notes and the 
revious workshops. Upon doing this I was able to do the task correctly

**Task4**: Task 4 was also easier for me to do since it was purely SQL work. I was able to use the MySQlworkbench to perform the task and save the required queries
 into sql files

**Task 5**: The final task was the task I had to do a lot of further studying on the NoSql databases
I choose mongo db for the nosql task. Modelling and implementing the data was not very easy but finally found a way. It was an interesting experience creating and 
working with the markdown files.

##  visualization Tools and Libraries.

* **Matplotlib**: This a plotting library in python that uses high functional methods to create plots.Its numerical mathematics 
extension NumPy. 

* **Seaborn**: it was built from matplotlib but unlike the matplotlib, it has high level commands that are easy to understand.
it also works more comfortably with pandas.

* **ggplot**: grammar of graphics for data visualization. this package was created to emulate ggplot in R programming language.

* **Geoplotlib**: This is a python toolbox for visualizing geographical data.


## Maps / charts
The following maps and charts can be used to visualize the data that has been handled
1. Bar chats:
    * Number of readings in each station
    * Number of monitors that are both in use and not in use
2. Histogram: VIsualizing the frequency distribution of Nox,No2,No etc
3. Line graph: time series data for Nox,No2,No etc
4. scatter plot: 
   * visualize the relationship between No2 and temperature.
   * visualize the relationship between No and temperature.
   * other useful relationships that can be investigated.
5. map plot: To visualize station locations from geo_point_2d.
6. Bar plot:
    * To visualize the number of readings each station have stored over the years



# Learning Outcomes achieved

- [x] Modelling, cleansing, normalizing, mapping, querying and analyzing substantial real-world big data (the assignment data having a size of 230mb+);
- [x] Understand the data cleansing, normalization and sharding processes by writing PYTHON scripts to process and convert the data to first (cleansed) CSV and then (normalized) SQL;
- [x] Designing and implementation of a relational (MySQL) database and then writing a PYTHON script to import the SQL into the appropriate tables while ensuring all referential integerity constraints are met.
- [x] Construct and implement a set of SQL queries to extract data using various filters and constraints.
- [x] Map (forward engineer) the data to a NoSQL database of your choice (MongoDB, BaseX, CouchBase, ArangoDB etc.)
- [x] Getting exposure to and learning the use of a range of data oriented technologies (databases, python & sql.)
- [x] Learn and use the MARKDOWN  markup syntax.

