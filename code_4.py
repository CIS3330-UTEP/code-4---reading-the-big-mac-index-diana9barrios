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





# def get_big_mac_price_by_country(country_code):
#     pass # Remove this line and code your function MEAN

# def get_the_cheapest_big_mac_price_by_year(year):
#     pass # Remove this line and code your function MIN INDEXES

# def get_the_most_expensive_big_mac_price_by_year(year):
#     pass # Remove this line and code your function MAM INDEXES

if __name__ == "__main__":
 
    result_a = get_big_mac_price_by_year(2010,"arg")
    print(result_a)