### What is Pandas
* Pandas is an open-sources library that allows to you to perform
data manipulation in Python.
* Pandas aims to be the fundamental high-level building 
block for doing practical real world data analysis in Python.
* Pandas provide an easy way to create, manipulate and wrangle 
the data.

#### Two Primary Data Structure 
1. Series(1-Dimensional)
2. Data-Frame(2-Dimensional)

### Why to Use Pandas 
* We can easily handle missing data.
* It provides an efficient way to manipulate data 
* It includes a powerful times series tool to work with
* Powerful and flexible group by functionality to perform.
* We can easily convert one form of data into another form

### How to install Pandas 
* Just open an command prompt and run below code : 
* If you haven't set the path for pip you have to set the 
path first to run this command, or else you go where 
the python is install and that find the folder name 
'Scripts' and then run there cmd.
```
pip install pandas
    or
python -m pip install pandas //This way you will install
the library in user admin
```
#### What is a data Frame ?
* Data frame is a two-dimensional array,with labeled
axes(rows and columns)
* A data frame is a tabular data, with rows to store the 
information and columns to name the information,

#### What is a series ?
* A series is a one-dimensional data structure.
* It can have any data structure like integer, float
and string.
* It is useful when you want to perform computation
on a one-dimensional array.

### Creating a Data Frame
```
import pandas as pd

d = {'Name':['Aditya','Rahul'], 'Surname':['Patel','Pandey']}

pd.DataFrame(d)
```
Output :

| Name 	| Surname|
|--:	|--:
|Aditya |Patel|
|Rahul  |Pandey |

#### Reading a Tabular data file into pandas
```
import pandas as pd
orders = pd.read_table('http://bit.ly/chiporders')

orders.head() ##By default the head will display 5 items
```
#### Output : 
**order\_id**|**quantity**|**item\_name**|**choice\_description**|**item\_price**
:-----:|:-----:|:-----:|:-----:|:-----:
1|1|Chips and Fresh Tomato Salsa|NULL|$2.39 
1|1|Izze|[Clementine]|$3.39 
1|1|Nantucket Nectar|[Apple]|$3.39 
1|1|Chips and Tomatillo-Green Chili Salsa|NULL|$2.39 
2|2|Chicken Bowl|[Tomatillo-Red Chili Salsa (Hot), [Black Beans, Rice, Cheese, Sour Cream]]|$16.98 

##### Another Example
```
import pandas as pd

user_name = pd.read_table('http://bit.ly/movieusers') #It will not show in proper formater 
#to correct this we use deliminator to correct this 

user_name = pd.read_table('http://bit.ly/movieusers', sep = '|')
```
#### Output : 
| |**0**|**1**|**2**|**3**|**4** |
:-----:|:-----:|:-----:|:-----:|:-----:|:-----:
0|1|24|M|technician|85711
1|2|53|F|other|94043
2|3|23|M|writer|32067
3|4|24|M|technician|43537
4|5|33|F|other|15213

##### In the above example there is no column name so we will defined it using a list

``` 
import pandas as pd

cols = ['user_id','age','gender','occupation','zip_code']

user_name = pd.read_table('http://bit.ly/movieusers', sep = '|', names = cols)

user_name.head()
```
#### Output : 
| |**user\_id**|**age**|**gender**|**occupation**|**zip\_code**
:-----:|:-----:|:-----:|:-----:|:-----:|:-----:
0|1|24|M|technician|85711
1|2|53|F|other|94043
2|3|23|M|writer|32067
3|4|24|M|technician|43537
4|5|33|F|other|15213

#### Note :
```
So that is how you work through using read_table.
If you have tabular data, just trying reading it see
what happens if it does'nt look right iterate through process
until it get it right 
Difference between the read_table and read_csv 
is by default the read_csv have a ',' seperator
```

#### How to select a series from a Data frame ? 
```
import pandas as pd
ufo = pd.read_csv('http://bit.ly/uforeports')
## We will use bracket to select the series
type(ufo['City'])
```
#### Output :
**0**|**Ithaca**
:-----:|:-----:
1|Willingboro
2|Holyoke
3|Abilene
4|New York Worlds Fair

