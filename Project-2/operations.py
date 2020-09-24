import pandas as pd


def get_routes(dataframe):
    """
    Function that calculate the total value and total sales per route

    :param dataframe: a dataframe that has the original information
    :return: the modified dataframe
    """
    # Get the yearly sum of the sales per route
    dataframe = dataframe.drop(columns='direction')
    dataframe = dataframe.groupby(['origin', 'destination', 'year'], sort=False).agg(
        total_value=pd.NamedAgg(column='total_value', aggfunc='sum'),
        total_sales=pd.NamedAgg(column='total_value', aggfunc='count'))

    # Get the mean total_value per route
    dataframe = dataframe.reset_index().drop(columns='year')
    dataframe = dataframe.groupby(['origin', 'destination'], sort=False).agg(
        avg_total_value=pd.NamedAgg(column='total_value', aggfunc='mean'),
        total_sales=pd.NamedAgg(column='total_sales', aggfunc='sum'))
    dataframe = dataframe.reset_index()

    return dataframe


def sort_routes_by_index(dataframe):
    """
    Function that create a column that holds the value of an index
    which helps to sort the routes based on it.

    :param dataframe: a dataframe that has the routes
    :return: the dataframe with the data sorted by the index

    """
    # We need to normalize using feature scaling the avg_total_value and total_sales,
    # add them together by using a weighted average and sort them in descending order

    # Get the min and max values of each column
    max_avg_total_value = dataframe['avg_total_value'].max()
    max_total_sales = dataframe['total_sales'].max()
    min_avg_total_value = dataframe['avg_total_value'].min()
    min_total_sales = dataframe['total_sales'].min()

    # Use this statistics to normalize and create an index to sort the routes
    scaled_avg_total_value = (dataframe['avg_total_value'] - min_avg_total_value) / \
                             (max_avg_total_value - min_avg_total_value)
    scaled_total_sales = (dataframe['total_sales'] - min_total_sales) / (max_total_sales - min_total_sales)

    # We perform an arithmetic mean to get the index
    dataframe['index'] = (scaled_avg_total_value + scaled_total_sales) / 2

    dataframe = dataframe.sort_values(by='index', ascending=False)

    return dataframe
