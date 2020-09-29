# EMTECH SCHOLARSHIP PROJECTS
This repository contains the two projects given as assignments in the Santander-EMTECH TECH scholarship in data science.
## PROJECT 1
In this project we were asked to write a program that generates a report for the managers of our hypothetical store “LifeStore”. We were given the information in the form of python lists. The elements of this lists contained the following:

- lifestore_products [id_product, name, price, category, stock]
- lifestore_sales [id_sale, id_product, score (from 1 to 5), date, refund (1 for true or 0 to false)]
- lifestore_searches [id_search, id product]

The management asked us to do the following:

Top selling products and lagging products based on the analysis of the categories with the lowest sales and categories with the lowest searches.
Products by review in the service from category analysis with higher sales and categories with higher searches.
Suggest a product strategy to be withdrawn from the market as well as suggestion of how to reduce inventory backlog by considering the monthly sales and income data.

To accomplish it we developed a program that generates three different analysis:

#### Best-selling products and lagging products:
Generate a list of the 50 products with the highest sales and one with the 100 most searched products.
#### By category:
Generate a list with the 50 products with less sales and one with the 100 products with the fewest searches.
#### Products per review in the service 
Show two listings of 20 products each, one listing for products with the best reviews and another for the worst, considering products with return.
Total income and average monthly sales, annual total and months with more sales per year

The program is written as a python script that is runned directly on the terminal, as a challenge and as an exercise for the EMTECH scholarship it was written avoiding to use any external libraries and built-in functions.

### CODE
The code was splitted into different files and functions to reuse code and to maintain order.

* lifestore_file.py
* quick_sort.py
* operations.py
* main.py

Almost all the code contains comments and docstrings, variables were named in a way that are easy to understand (there may be some exceptions).

#### lifestore_file.py
This file contains all the data provided by the management, as mentioned in the introduction. There are three lists, each of them contain lists with different information. 

- lifestore_products [id_product, name, price, category, stock]
- lifestore_sales [id_sale, id_product, score (from 1 to 5), date, refund (1 for true or 0 to false)]
- lifestore_searches [id_search, id product]

#### quick_sort.py
To avoid the usage of the built-in method sort() associated to lists, we implemented a version of quick sort. This function takes a list as input and acts in place ordering the list in ascending order. 

#### operations.py
This file contains all the business logic. Here we calculate all of the operations needed to show the results to the management.

#### main.py
Finally, this file contains the logic that interacts with the user, the login authentication, the selection of the analysis and the exit of the program. 

### EXECUTION
To run the project move to the location it was downloaded and type:
```
cd Project-1
python main.py
```
Depending on your python installation, it may be needed to run as:
```
python3 main.py
```
## PROJECT 2
In this final project we were asked to write a program that generates a report for the managers of our hypothetical company “Synergy Logistics”. We were given the information in a csv file. The elements of this file were organized in this columns:

| register_id | direction | origin | destination | year | date     | product | transport_mode | company_name | total_value | 
|-------------|-----------|--------|-------------|------|----------|---------|----------------|--------------|-------------| 
| 1           | Exports   | Japan  | China       | 2015 | 31/01/15 | Cars    | Sea            | Honda        | 33000000    | 
| 2           | Exports   | Japan  | China       | 2015 | 01/02/15 | Cars    | Sea            | Honda        | 16000000    | 
| 3           | Exports   | Japan  | China       | 2015 | 02/02/15 | Cars    | Sea            | Honda        | 29000000    | 


We were asked to determine a strategy for the 2021 plan. To accomplish this we were given three options, import and export routes, transportation means and total value of imports and exports.

The program is written as a python script that is runned directly on the terminal, pandas library was used to make the development easier.

The available options are:
#### Option 1:
The top 10 import and the top 10 export routes according to their number of operations and average yearly total value.
#### Option 2:
The transportation means sorted by total value, taking import and exports independently and as a whole.
#### Option 3:
The countries sorted by total value and considering their cumulative percentage of the total value.

We need to choose wich option (or combination of them) is going to serve best to the company.

### Code
Given that we used the Pandas library to assist us in the analysis and also tried to comment where needed, the code is pretty much self-explaining.

* **analysis.ipynb** .- Is the Jupyter notebook that was used for testing and debugging, contains all the analysis.
* **operations.py** .- Is the python script that contains the functions that assisted in the analysis.
* **main.py** .- Contains the main logic of the program.

#### Execution
To run the project move to the location it was downloaded and type:
```
cd Project-2
python main.py
```
Depending on your python installation, it may be needed to run as:
```
python3 main.py
```
