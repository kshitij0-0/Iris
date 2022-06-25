import requests
from bs4 import BeautifulSoup

def query():
    
    user_query = input('Enter your query: ')

    URL = "https://www.google.co.in/search?q=" + user_query

    headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36 OPR/86.0.4363.70'
    }

    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    result = soup.find(class_='VwiC3b yXK7lf MUxGbd yDYNvb lyLwlc lEBKkf').get_text()
    print(result)
#hgKElc
#VwiC3b yXK7lf MUxGbd yDYNvb lyLwlc lEBKkf
while True:
    try:
        query()
    except Exception:
        print('Sorry no result, please be clear')
    user_input = input('To continue press y: ')
    if user_input != 'y':
        break
