import csv
import pandas as pd
big_mac_file = './big-mac-full-index.csv'
df = pd.read_csv('./big-mac-full-index.csv')

def get_big_mac_price_by_year(year,country_code):
    date_query = f"('date' >= '{year}-01-01' and 'date' <= '{year}-12-31') & ('iso_a3' == '{country_code.upper()}')"
    
   
    price_df = df.query(date_query)
    # print(price_df)
    print(date_query)
    # price_mean = price_df['dollar_price'].mean()
    # return(round(price_mean,2))


def get_big_mac_price_by_country(country_code):
    pass

def get_the_cheapest_big_mac_price_by_year(year):
    cheapest_year = str(year)
    pass


def get_the_most_expensive_big_mac_price_by_year(year):
   pass

if __name__ == "__main__":
 
    result_a = get_big_mac_price_by_year(2010,"arg")
    print(result_a)
    # result_b = get_big_mac_price_by_country("mex")
    # print(result_b)
    # result_c = get_the_cheapest_big_mac_price_by_year(2008)
    # print(result_c)
    # result_d = get_the_most_expensive_big_mac_price_by_year(2014)
    # print(result_d)


 
  