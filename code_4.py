import csv
import pandas as pd
big_mac_file = './big-mac-full-index.csv'
df = pd.read_csv('./big-mac-full-index.csv')

def get_big_mac_price_by_year(year,country_code):
    # this is going to filter the file with equaling the date to the first four chracters so only the year is evaluated
    # this line is also converting iso_03 into all lowercase and making it equal the country code 
    #  & combined both booleans
    filtered_df = df[(df['date'].str[:4] == str(year)) & (df['iso_a3'].str.lower() == country_code)] 

    #processing the data by making sure conditions are met
    if not filtered_df.empty:
        mean_price = filtered_df['dollar_price'].mean()
        # round two decimals
        mean_rounded = round(mean_price,2)
        return mean_rounded
    return None


def get_big_mac_price_by_country(country_code):
    # converting iso_03 into all lowercase and making it equal the country code
    filtered_df = df[df['iso_a3'].str.lower() == country_code]

    if not filtered_df.empty:
        mean_price = filtered_df['dollar_price'].mean()
        mean_rounded = round(mean_price,2)
        return mean_rounded
    return None


def get_the_cheapest_big_mac_price_by_year(year):
    cheapest_year = str(year)
    # stores first 4 characters of date/ stores in in year_filter
    year_filter = df['date'].str[:4] == cheapest_year
    filtered_df = df[year_filter]

    if not filtered_df.empty:
        lowest_price = filtered_df.loc[filtered_df['dollar_price'].idxmin()]
        country = lowest_price['name']
        country_code = lowest_price['iso_a3']
        price_rounded = round(lowest_price['dollar_price'], 2)

        return f"{country}({country_code}): $ {price_rounded}"
    return None


def get_the_most_expensive_big_mac_price_by_year(year):
    expensive_year= str(year)
    # taking first four characters in date to only have the year
    year_filter = df['date'].str[:4] == expensive_year
    filtered_df = df[year_filter]

    if not filtered_df.empty:
        # used idxmax to find the man inside a column and .loc to stay in 'bounce'
        highest_price = filtered_df.loc[filtered_df['dollar_price'].idxmax()]
        country = highest_price['name']
        country_code = highest_price['iso_a3']
        price_rounded = round(highest_price['dollar_price'], 2)

        return f"{country}({country_code}): ${price_rounded}"
    return None


if __name__ == "__main__":
 
    result_a = get_big_mac_price_by_year(2010,"arg")
    print(result_a)
    result_b = get_big_mac_price_by_country("mex")
    print(result_b)
    result_c = get_the_cheapest_big_mac_price_by_year(2008)
    print(result_c)
    result_d = get_the_most_expensive_big_mac_price_by_year(2014)
    print(result_d)


    #Chat-GPT(GPT-4). Date of query (2024/09/29). "why do I keep getting the error 'none'"
    # (this was in reagard to def get_big_mac_price_by_year(year,country_code))
    # #Generated using OpenAI Chat-GPT. https://chat.openai.com/