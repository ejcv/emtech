from lifestore_file import lifestore_products, lifestore_sales, lifestore_searches
from quick_sort import quick_sort
# Is needed to print into a file
import sys

number_products = len(lifestore_products)
# empty list of [id_product, smth_of_interest]
empty_list = [[i + 1, 0] for i in range(number_products)]

year_dictionary = {
    1: 'January',
    2: 'February',
    3: 'March',
    4: 'April',
    5: 'May',
    6: 'June',
    7: 'July',
    8: 'August',
    9: 'September',
    10: 'October',
    11: 'November',
    12: 'December'
}


def calculate_sales_per_product(refund=False):
    """
    A function that gets the number of sales per product
    :param refund: a flag that tells if returned and refunded products are taken into account
    :return: A list of lists with the product id and the total sales per product [product_id, total_sales]
    """
    sales_per_product_list = [[i + 1, 0] for i in range(number_products)]
    for sale in lifestore_sales:
        if refund:
            if sale[4] == 0:
                sales_per_product_list[sale[1] - 1][1] += 1
        else:
            # we modify the position [id-1][1] and increase by one each time it is called
            sales_per_product_list[sale[1] - 1][1] += 1
    return sales_per_product_list


def calculate_searches_per_product():
    searches_per_product_list = empty_list.copy()
    for search in lifestore_searches:
        # we modify the position [id-1][1] and increase by one each time it is called
        searches_per_product_list[search[1] - 1][1] += 1
    return searches_per_product_list


def sort_products_by_sales():
    """
    A function that calculates the number of sales per product and sorts them from best to worst
    and prints them in stdout
    :return sales_per_product_list: an ordered list with [id_product, #sales]
    """
    # holds the index and the number of sales of each product_id
    sales_per_product_list = calculate_sales_per_product()
    # Sort the list from minimum to maximum
    quick_sort(sales_per_product_list, lambda x: x[1])

    return sales_per_product_list


def sort_products_by_searches():
    """
    A function that calculates the number of searches per product and sorts them from best to worst
    and prints them in stdout
    :return searches_per_product_list: an ordered list
    """
    # holds the index and the number of searches of each product_id
    searches_per_product_list = calculate_searches_per_product()

    quick_sort(searches_per_product_list, lambda x: x[1])

    return searches_per_product_list


def get_categories():
    sales_per_category_list = []
    previous_category = None
    for product in lifestore_products:
        category = product[3]
        if category != previous_category:
            # Append to the list a list that holds [category, # sales]
            sales_per_category_list.append([category, 0])
        previous_category = category

    return sales_per_category_list


def calculate_by_categories(array):
    for element in array:
        product_id = element[0]
        product_category = lifestore_products[product_id - 1][3]
        element.append(product_category)

    per_category_list = []
    previous_category = array[0][2]
    accumulation_category = 0
    for product in array:
        category = product[2]
        if category == previous_category:
            # if the category is t same, accumulate the number of sales
            accumulation_category += product[1]
        else:
            per_category_list.append([category, accumulation_category])
        previous_category = category

    return per_category_list


def sort_categories_by_sales():
    sales_per_product = calculate_sales_per_product()
    sales_per_category_list = calculate_by_categories(sales_per_product)
    quick_sort(sales_per_category_list, lambda x: x[1])

    return sales_per_category_list


def sort_categories_by_searches():
    searches_per_product = calculate_searches_per_product()
    searches_per_category_list = calculate_by_categories(searches_per_product)
    quick_sort(searches_per_category_list, lambda x: x[1])

    return searches_per_category_list


def best_and_worst_reviewed_products():
    """

    :return average_score_per_product: Sorted list of lists [product_id, average_score]
    """
    average_score_per_product = []
    cumulative_score_per_product = empty_list.copy()
    # Copying the list of lists is not working due to python binding, the element lists are bound
    sales_per_product_list = calculate_sales_per_product()

    for sale in lifestore_sales:
        product_id = sale[1]
        cumulative_score_per_product[product_id - 1][1] += sale[2]

    for cumulative_score in cumulative_score_per_product:
        product_id = cumulative_score[0]
        sales = sales_per_product_list[product_id - 1][1]
        # Only count them if they have been sold
        if sales > 0:
            average_score = cumulative_score[1] / sales
            average_score_per_product.append([product_id, average_score])

    # Sort the list from minimum to maximum
    quick_sort(average_score_per_product, lambda x: x[1])

    return average_score_per_product


def calculate_total_revenue():
    # declare total_revenue equal to zero
    total_revenue = 0
    sales_per_product = calculate_sales_per_product(refund=True)
    for sales in sales_per_product:
        product_id = sales[0]
        total_revenue += lifestore_products[product_id - 1][2] * sales[1]
    return total_revenue


def calculate_monthly_sales():
    # Create a list of lists with elements [month, sales_per_month]
    monthly_sales_list = [[month, 0] for month in range(1, 13)]
    total_concreted_sales = 0
    for sale in lifestore_sales:
        month = int(sale[3].split('/')[1])
        if sale[4] == 0:
            # Increment the sales per month if the in the monthly_sales_list
            monthly_sales_list[month - 1][1] += 1
            total_concreted_sales += 1

    quick_sort(monthly_sales_list, lambda x: x[1])
    return monthly_sales_list, total_concreted_sales


def option_1():
    sales_per_product_list = sort_products_by_sales()
    # show the top 10 selling products
    # Not the best approach, I did not know about reverse method
    # Gonna leave it like this as a reminder
    print('The top 10 selling products are: ')
    for index in range(1, 11):
        print(
            f'{index}.- {sales_per_product_list[-index][1]} sells for'
            f' {lifestore_products[sales_per_product_list[-index][0] - 1][1]}')
    print('\n')

    searches_per_product_list = sort_products_by_searches()
    print('The top 10 searched products are: ')
    for index in range(1, 11):
        print(
            f'{index}.- {searches_per_product_list[-index][1]} searches for'
            f' {lifestore_products[searches_per_product_list[-index][0] - 1][1]}')
    print('\n')

    sales_per_categories_list = sort_categories_by_sales()
    print(f'The 3 worst selling categories are:')
    for index in range(3):
        print(
            f'{index + 1}.- {sales_per_categories_list[index][1]} for {sales_per_categories_list[index][0]}'
        )
    print('\n')

    searches_per_categories_list = sort_categories_by_searches()
    print(f'The 3 least searched categories are:')
    for index in range(3):
        print(
            f'{index + 1}.- {searches_per_categories_list[index][1]} for {searches_per_categories_list[index][0]}'
        )


def option_2():
    average_score_per_product = best_and_worst_reviewed_products()
    print('The top 10 rated products are: ')
    # Not the best approach, I did not know about reverse method
    # Gonna leave it like this as a reminder
    for index in range(1, 21):
        print(
            f'{index}.- {average_score_per_product[-index][1]:.2f}/5 stars for'
            f' {lifestore_products[average_score_per_product[-index][0] - 1][1]}')
    print('\n')
    print('The worst 10 rated products are: ')
    for index in range(10):
        print(
            f'{index + 1}.- {average_score_per_product[index][1]:.2f}/5 stars for'
            f' {lifestore_products[average_score_per_product[index][0] - 1][1]}')


def option_3():
    total_revenue = calculate_total_revenue()
    sorted_monthly_sales_list, total_concreted_sales = calculate_monthly_sales()
    sorted_monthly_sales_list.reverse()
    print(f'The total amount of income was: {total_revenue}')
    print(f'The average monthly income was: {total_revenue / 12:.2f}')
    print(f'The total concreted sales of 2020 are: {total_concreted_sales} \n')
    print(f'The monthly sales are:')
    for index, month in enumerate(sorted_monthly_sales_list):
        print(f'{index + 1} .- {month[1]} concreted sales in {year_dictionary[month[0]]}')


def option_4():
    # Redirect the standard output to a file
    original_stdout = sys.stdout  # Save a reference to the original standard output

    with open('report.txt', 'w') as f:
        sys.stdout = f  # Change the standard output to the file we created.
        option_1()
        print('\n')
        option_2()
        print('\n')
        option_3()
        sys.stdout = original_stdout  # Reset the standard output to its original value
