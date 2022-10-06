# web-scraping

## Install needed python packages
- Request
  - `import requests`
- BeautifulSoup
  - `from bs4 import BeautifulSoup`
- Pandas
  - `import pandas as pd`

## Two webpages selected to extract data from
- Alzheimer's Association - 2022 Featured News
  - https://www.alz.org/news/2022
- Long Island City 10 Day Weather
  - https://weather.com/weather/tenday/l/Long+Island+City+NY+USNY0833:1:US

## Approach for scrapping data
- Use Google Chrome
- After open the webpage, right click the mouse and select "inspector"
- Press crtl + F to add a search bar
- Copy paste the needed content (such as header, footer) in the search bar and locate the tag for that content
- Add/Type the tag in python file
- OR just hoover the mouse over the tags until find the needed content in highlight 
