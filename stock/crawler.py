# -*- coding: utf-8 -*-
"""
Created on Sun Apr 2 10:52:45 2023

@author: <jeyakumar.kasi@hyproid.com>
"""

import os
import re
import sys
import requests
import pandas as pd
import datetime as dt
from bs4 import BeautifulSoup

from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = 'all'



# file_url = r'./stocks.xlsx'
file_url = r'C:\ebooks\Hyproid\Stocks\stocks.xlsx'


is_create_list = True
ticker_sheet_name = 'stocks'
default_stocks_list = {
    'ticker': ['TATASTEEL', 'ONGC', 'ASHOKLEY', 'HINDZINC', 'ITC', 'SBIN', 'AXISBANK',
               'BHARTIARTL', 'TATAMOTORS', 'TVSMOTOR', 'ICICIBANK', 'GODREJCP', 'TCS',
               'HINDUNILVR', 'MARUTI', 'NESTLEIND', 'RELIANCE', 'INFY'],
    'type': ['L', 'L', 'L', 'L', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'H', 'H', 'H', 'H', 'H', 'H'],
    'stockName': [],
    'isActive': []
}


# ----------------------------------------------------------
is_fresh_start = False
now = dt.datetime.now()
file_url = os.path.abspath(file_url)


def get_excel_writer(file_url, **kwargs):
    mode = kwargs.pop('mode', 'w')
    engine = kwargs.pop('engine', 'openpyxl') # xlsxwriter
    return pd.ExcelWriter(file_url, mode=mode, engine=engine, **kwargs)


def create_ticker_list(file_url):
    print(f'Creating "{file_url}"...')
    with get_excel_writer(file_url) as writer:
        tickers_len = len(default_stocks_list['ticker'])
        for k, v in default_stocks_list.items():
            if k != 'ticker' and len(v) < tickers_len:
                default_stocks_list[k] = [None] * tickers_len

        df = pd.DataFrame.from_dict(default_stocks_list)
        print(f'Writing the tickers list into <{ticker_sheet_name}> sheet...', end=' ')
        df.to_excel(writer, sheet_name=ticker_sheet_name, index=False)
        print('Done.')


def curl(ticker):
    # https://www.google.com/finance/quote/SBIN:NSE?window=1Y
    url = f'https://www.google.com/finance/quote/{ticker.upper()}:NSE'
    print(f'[GET] {url} ...')
    res = requests.get(url)
    # print(res.status_code)
    # print(res.content)
    return res


def parse_datetime(s):
    # s = 'Mar 31, 3:59:41 PM GMT+5:30 · INR · NSE · Disclaimer'

    s = s.encode('ascii', 'ignore').decode()
    datetime_str = re.search('([\w\s,\d:]+)([\+\-]\d{1,2}):(\d{1,2})', s)
    # print(datetime_str.groups())

    if datetime_str.groups():
        timezone_h, timezone_m = datetime_str.group(2), datetime_str.group(3)
        if int(timezone_h) < 10: timezone_h = timezone_h[0] + '0' + timezone_h[1:]
        datetime_str = datetime_str.group(1)

    # return dt.datetime.strptime(str(now.year) + datetime_str + timezone_h + timezone_m, '%Y%b %d, %I:%M:%S%p %Z%z')
    return dt.datetime.strptime(str(now.year) + datetime_str[:-3].rstrip(), '%Y%b %d, %I:%M:%S%p')



def extract_features(res, is_new):
    soup = BeautifulSoup(res.content, 'lxml') #, from_encoding='iso-8859-8')  # html.parser, xml, html5lib
    main_tag = soup.find('main')

    features_list = {}
    if is_new:
        features_list['stockName'] = 'div.zzDege'

    features_list['price'] = 'div.YMlKec.fxKbKc'
    # features_list['prevPrice'] = 'div.P6K39c'
    features_list['datetime'] = 'div.ygUjEc'

    features = {}
    for feature, select_query in features_list.items():
        # stock_name = main_tag.find_all('div', {'class': 'zzDege'})
        features[feature] = main_tag.select_one(select_query).text
    return features


def run(ticker, is_new):
    res = curl(ticker)
    features = extract_features(res, is_new)
    return features


if not os.path.isfile(file_url):
    if not is_create_list:
        sys.exit(f"Input {file_url} is not found, exiting.")

    # create the one.
    is_fresh_start = True
    create_ticker_list(file_url)


xls = pd.ExcelFile(file_url)
# dir(xls)

# Stock list
stock_sheet_list = list(map(str.upper, xls.sheet_names))

df_tickers = pd.read_excel(xls, sheet_name=ticker_sheet_name) #, header=None, names=["ticker", "isActive"])
df_tickers['isActive'].fillna(True, inplace=True)
df_active_tickers = df_tickers.loc[df_tickers['ticker'].notnull() & df_tickers['isActive']]
print(df_active_tickers)
print(stock_sheet_list)


new_tickers_found = 0
with pd.ExcelWriter(file_url, mode='a', if_sheet_exists='overlay', engine='openpyxl') as writer: #, engine='xlsxwriter')
    for idx, row in df_active_tickers.iterrows():
        # print(idx, row)

        ticker = row['ticker'].upper()
        is_new=ticker not in stock_sheet_list
        features = run(ticker, is_new)

        # Filter the ticker meta columns from the list
        data = {k: v for k, v in features.items() if k not in df_tickers.columns}

        if is_new:
            new_tickers_found += 1
            # @todo: Add meta info in the 'ticker' (main) sheet
            df_tickers.loc[df_tickers['ticker'] == ticker, 'stockName'] = features.get('stockName')

            # Parse Datetime field
            data['datetime'] = parse_datetime(data['datetime'])
            df = pd.DataFrame.from_dict({k: [v] for k, v in data.items()})
            df.set_index('datetime', inplace=True, drop=True)

            # Create the new sheet
            print(f"Writing new <{ticker}> sheet...", end=" ")
            df.to_excel(writer, sheet_name=ticker)
        else:
            # update existing sheet
            df_sheet = pd.read_excel(xls, sheet_name=ticker, parse_dates=True, index_col='datetime')

            datetime = parse_datetime(data.pop('datetime'))
            if datetime not in df_sheet.index:
                df = pd.DataFrame({k: [v] for k, v in data.items()}, index=[datetime])
                df = pd.concat([df_sheet, df])
                print(f"Adding to <{ticker}> sheet...", end=" ")
                df.to_excel(writer, sheet_name=ticker)
            else:
                print(f"{datetime} is already exists! No changes.", end=" ")

        print("[Done]")
    if new_tickers_found > 0:
        print(f"<{new_tickers_found}> new tickers found.")

        # if not is_fresh_start:
        # This file just now got updated while running this script.
        print(f"Updating the <{ticker_sheet_name}> sheet...", end='')
        df_tickers.to_excel(writer, sheet_name=ticker_sheet_name, index=False)
        print("[Done]")

# Close the file.
xls.close()
