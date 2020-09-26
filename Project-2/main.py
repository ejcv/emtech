import pandas as pd
import operations as op
import sys

# Upload the data and ignore the column register_id
synergy_logistics_info_df = pd.read_csv('synergy_logistics_database.csv', usecols=lambda x: x != 'register_id')


def option_1():
    """
    Function that gets the top 10 import and export routes and prints them
    """
    # copy the dataframe to avoid modifying it
    option_1_df = synergy_logistics_info_df.copy()
    option_1_df.drop(columns=['product', 'transport_mode', 'date', 'company_name'], inplace=True)

    # divide in two df, one for imports and the other for exports
    option_1_df_exports = option_1_df[option_1_df['direction'] == 'Exports']
    option_1_df_imports = option_1_df[option_1_df['direction'] == 'Imports']

    option_1_df_exports = op.get_routes(option_1_df_exports)
    option_1_df_imports = op.get_routes(option_1_df_imports)

    option_1_df_exports = op.sort_routes_by_index(option_1_df_exports).reset_index(drop=True)
    option_1_df_imports = op.sort_routes_by_index(option_1_df_imports).reset_index(drop=True)

    option_1_df_exports.index = option_1_df_exports.index + 1
    option_1_df_imports.index = option_1_df_imports.index + 1
    print('Top 10 export routes:')
    print(option_1_df_exports[:10])
    print('\n')
    print('Top 10 import routes:')
    print(option_1_df_imports[:10])


def option_2():
    """
    Function that sorts the dataframe by transportation mean and its associated total value and prints them
    """
    option_2_df = synergy_logistics_info_df.copy()
    option_2_df = option_2_df.drop(columns=['origin', 'destination', 'year', 'date', 'product', 'company_name'])
    print(option_2_df.groupby(['transport_mode', 'direction']).sum().sort_values(by='total_value', ascending=False))
    print("\n")
    print(option_2_df.groupby(['transport_mode']).sum().sort_values(by='total_value', ascending=False))


def option_3():
    """
    Function that calculate that calculates the cumulative percentage of the total value for each country
    and prints them
    """
    option_3_df = synergy_logistics_info_df.copy()

    # We will get the origin or destination and create a new column based on that
    option_3_df['country'] = option_3_df.apply(
        lambda row: row['origin'] if row['direction'] == 'Exports' else row['destination'], axis=1)
    option_3_df = option_3_df[['country', 'total_value']]
    option_3_df = option_3_df.groupby('country').sum()
    option_3_df = option_3_df.sort_values(by='total_value', ascending=False)
    option_3_df['cumulative_percentage'] = 100 * option_3_df['total_value'].cumsum() / option_3_df['total_value'].sum()
    print(option_3_df)


def option_4():
    """
    Function that prints all the analysis in the previous options into a .txt file
    :return:
    """
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


def analysis(option):
    """
    A function that emulates a switch-case to select the analysis to perform

    :param option: selected choice, inputed by user
    :return: the associated function to the option it was selected
    """
    switcher = {
        1: option_1,
        2: option_2,
        3: option_3,
        4: option_4
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
        4.- Print the whole analysis into a text file.
    ''')

    analysis(int(input('Type the selected option: ')))
    finish = input('Exit? (y/n): ')
