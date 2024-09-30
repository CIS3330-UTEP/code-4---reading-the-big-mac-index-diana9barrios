import csv
import pandas as pd
big_mac_file = './big-mac-full-index.csv'
df = pd.read_csv('./big-mac-full-index.csv')

def get_big_mac_price_by_year(year,country_code):
    filtered_df = df[(df['date'].str[:4] == str(year)) & (df['iso_a3'].str.lower() == country_code)]
    #processing the data
    if not filtered_df.empty:
        mean_price = filtered_df['dollar_price'].mean()
        mean_rounded = round(mean_price,2)
        return mean_rounded
    return None



def get_big_mac_price_by_country(country_code):
    filtered_df = df[df['iso_a3'].str.lower() == country_code]

    if not filtered_df.empty:
        mean_price = filtered_df['dollar_price'].mean()
        mean_rounded = round(mean_price,2)
        return mean_rounded
    return None


def get_the_cheapest_big_mac_price_by_year(year):
    cheapest_year = str(year)
    year_filter = df['date'].str[:4] == cheapest_year
    filtered_df = df[year_filter]

    if not filtered_df.empty:
        cheapest_price = filtered_df[filtered_df['dollar_price'].idmin()]
        country = cheapest_price['name']
        country_code = cheapest_price['iso_a3']
        price_rounded = round(cheapest_price['dollar_price'],2)
        return f"{country}({country_code}): $ {price_rounded}"


def get_the_most_expensive_big_mac_price_by_year(year):
    expensive_year= str(year)
    year_filter = df['date'].str[:4] == expensive_year
    filtered_df = df[year_filter]

    if not filtered_df.empty:
        highest_price = filtered_df.loc[filtered_df['dollar_price'].idxmax()]
        country = highest_price['name']
        country_code = highest_price['iso_a3']
        price_rounded = round (highest_price['dollar_price',2])

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