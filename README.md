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

Best-selling products and lagging products:
Generate a list of the 50 products with the highest sales and one with the 100 most searched products.
By category, generate a list with the 50 products with less sales and one with the 100 products with the fewest searches.
Products per review in the service 
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
  cd Project-1
  python main.py

Depending on your python installation, it may be needed to run as:
  python3 main.py

## PROJECT 2
Coming soon!!
