""" import pandas as pd

def remove_duplicates_and_print(file_path):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(file_path)

    # Remove duplicates and keep the first occurrence
    df_no_duplicates = df.drop_duplicates()

    # Filter data for "Virgin Islands (U.S.)"
    df_virgin_islands = df_no_duplicates[df_no_duplicates['Country Name'] == 'Cuba']

    # Print the resulting DataFrame
    print("Data for Cuba:\n")
    print(df_virgin_islands.to_string(index=False))

if __name__ == "__main__":
    file_path = "Pop.csv"
    remove_duplicates_and_print(file_path)
 """


""" import pandas as pd

def analyze_population(file_path):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(file_path)

    # Remove duplicates and keep the last occurrence (to get the latest data)
    df_no_duplicates = df.drop_duplicates(keep='last')

    # Find the country with the highest population
    country_highest_population = df_no_duplicates[df_no_duplicates['2013 [YR2013]'] == df_no_duplicates['2013 [YR2013]'].max()]['Country Name'].values[0]

    # Find the country with the lowest population
    country_lowest_population = df_no_duplicates[df_no_duplicates['2013 [YR2013]'] == df_no_duplicates['2013 [YR2013]'].min()]['Country Name'].values[0]

    # Find the country with the most declining population over time
    df_sorted_by_population = df_no_duplicates.sort_values(by='2013 [YR2013]', ascending=False)
    country_most_declining_population = df_sorted_by_population.iloc[-1]['Country Name']

    # Print the results
    print("Country with the highest population: ", country_highest_population)
    print("Country with the lowest population: ", country_lowest_population)
    print("Country with the most declining population over time: ", country_most_declining_population)

if __name__ == "__main__":
    file_path = "Pop.csv"
    analyze_population(file_path) """

import pandas as pd

def find_country_with_most_declining_population(df):
    # Calculate the difference in population between 2010 and 2019
    df['Population_Difference'] = df['2019 [YR2019]'] - df['2010 [YR2010]']

    # Find the country with the most declining population over time
    index_min_decline = df['Population_Difference'].idxmin()
    country_most_declining_population = df.loc[index_min_decline, 'Country Name']

    # Drop the Population_Difference column as it was just for intermediate calculations
    df.drop(columns=['Population_Difference'], inplace=True)

    return country_most_declining_population

if __name__ == "__main__":
    file_path = "exerciseB/Csv_manupulation/Pop.csv"
    df = pd.read_csv(file_path)

    # Remove duplicates and keep the first occurrence
    df_no_duplicates = df.drop_duplicates()

    country_most_declining_population = find_country_with_most_declining_population(df_no_duplicates)
    print(f"The country with the most declining population from 2010 to 2019: {country_most_declining_population}")
