import csv
import pandas as pd
big_mac_file = './big-mac-full-index.csv'
df = pd.read_csv('./big-mac-full-index.csv')

def get_big_mac_price_by_year(year,country_code):
    date_query = f"(date >= '{year}-01-01' and date <= '{year}-12-31') & (iso_a3 == '{country_code.upper()}')"
    price_df = df.query(date_query)
    # print(price_df)
    # print(date_query)
    price_mean = price_df['dollar_price'].mean()
    return(round(price_mean,2))


def get_big_mac_price_by_country(country_code):
    country_query = f"(iso_a3 == '{country_code.upper()}')"
    price_df = df.query(country_query)
    price_mean = price_df['dollar_price'].mean()
    return(round(price_mean,2))

def get_the_cheapest_big_mac_price_by_year(year):
    # lecture 7
    year_query = f"(date >= '{year}-01-01' and date <= '{year}-12-31')"
    price_df = df.query(year_query)
    min_idx = price_df['dollar_price'].idxmin()
    price = round(price_df.loc[min_idx]['dollar_price'],2)
    country_name = (price_df.loc[min_idx]['name'])
    country_code = (price_df.loc[min_idx]['iso_a3'])
    
    # return (country_code)
    return f"{country_name}({country_code}): ${price}"


def get_the_most_expensive_big_mac_price_by_year(year):
    year_query = f"(date >= '{year}-01-01' and date <= '{year}-12-31')"
    price_df = df.query(year_query)
    max_idx = price_df['dollar_price'].idxmax()
    price = round(price_df.loc[max_idx]['dollar_price'],2)
    country_name = (price_df.loc[max_idx]['name'])
    country_code = (price_df.loc[max_idx]['iso_a3'])

    return f"{country_name}({country_code}): ${price}"
   

if __name__ == "__main__":
 
    result_a = get_big_mac_price_by_year(2012,"arg")
    print(result_a)
    result_b = get_big_mac_price_by_country("mex")
    print(result_b)
    result_c = get_the_cheapest_big_mac_price_by_year(2008)
    print(result_c)
    result_d = get_the_most_expensive_big_mac_price_by_year(2003)
    print(result_d)


 
  