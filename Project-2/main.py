import pandas as pd

# Upload the data and ignore the column register_id
synergy_logistics_info_df = pd.read_csv('synergy_logistics_database.csv', usecols=lambda x: x != 'register_id')


def get_routes(dataframe):
    """

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

    """
    # We need to normalize using feature scaling the avg_total_value and total_sales,
    # add them together by using a weighted average and sort them in descending order

    # Get the min and max values of each column
    max_avg_total_value = dataframe['avg_total_value'].max()
    max_total_sales = dataframe['total_sales'].max()
    min_avg_total_value = dataframe['avg_total_value'].min()
    min_total_sales = dataframe['total_sales'].min()

    # Use this statistics to normalize and create an index to sort the routes
    scaled_avg_total_value = (dataframe['avg_total_value'] - min_avg_total_value) / (
                max_avg_total_value - min_avg_total_value)
    scaled_total_sales = (dataframe['total_sales'] - min_total_sales) / (max_total_sales - min_total_sales)

    # We perform an arithmetic mean to get the index
    dataframe['index'] = (scaled_avg_total_value + scaled_total_sales) / 2

    dataframe = dataframe.sort_values(by='index', ascending=False)

    return dataframe


def option_1():
    """

    """
    # copy the dataframe to avoid modifying it
    option_1_df = synergy_logistics_info_df.copy()
    option_1_df.drop(columns=['product', 'transport_mode', 'date', 'company_name'], inplace=True)

    # divide in two df, one for imports and the other for exports
    option_1_df_exports = option_1_df[option_1_df['direction'] == 'Exports']
    option_1_df_imports = option_1_df[option_1_df['direction'] == 'Imports']

    option_1_df_exports = get_routes(option_1_df_exports)
    option_1_df_imports = get_routes(option_1_df_imports)

    option_1_df_exports = sort_routes_by_index(option_1_df_exports).reset_index(drop=True)
    option_1_df_imports = sort_routes_by_index(option_1_df_imports).reset_index(drop=True)

    option_1_df_exports.index = option_1_df_exports.index + 1
    option_1_df_imports.index = option_1_df_imports.index + 1

    print(option_1_df_exports[:10])
    print('\n')
    print(option_1_df_imports[:10])


def option_2():
    return None


def option_3():
    return None


def analysis(option):
    """
    A function that emulates a switch-case to select the analysis to perform
    :param option: selected choice, inputed by user
    :return: the associated function to the option it was selected
    """
    switcher = {
        1: option_1,
        2: option_2,
        3: option_3
    }
    func = switcher.get(option, "Invalid option")
    return func()


finish = 'n'

while finish != ('y' or 'Y'):
    print('''
    Available options:
        1.- Analyze the exports and imports routes and give a top 10 for each of them.
        2.- Sort the transportation means based on income. 
        3.- Total income from import and exports and the countries that generate 80% income for the company.
    ''')

    analysis(int(input('Type the selected option: ')))
    finish = input('Exit? (y/n): ')
