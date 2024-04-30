import requests
from bs4 import BeautifulSoup
import json
import time

def handle():
    while True:
        data = scrape_data()
        print(data)
        response = requests.post('http://127.0.0.1:8000/update_data/', json=data)
        print('Data sent to Django:', response.status_code)
        time.sleep(5)

def scrape_data():
    url = 'https://coinmarketcap.com'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    data = []

    # Locate the table containing the cryptocurrency data
    table = soup.find('table', {'class': 'cmc-table'})
    rows = table.find_all('tr')[1:]  # Skip the header row

    for row in rows:
        cols = row.find_all('td')
        name = cols[1].text.strip()
        price = cols[3].text.strip()
        
        # Check if all columns exist before accessing them
        if len(cols) >= 7:
            change_1h = cols[4].text.strip()
            change_24h = cols[5].text.strip()
            change_7d = cols[6].text.strip()
        else:
            change_1h = "N/A"
            change_24h = "N/A"
            change_7d = "N/A"
        
        # Check if all columns exist before accessing them
        if len(cols) >= 10:
            market_cap = cols[7].text.strip()
            volume_24h = cols[8].text.strip()
            circulating_supply = cols[9].text.strip()
        else:
            market_cap = "N/A"
            volume_24h = "N/A"
            circulating_supply = "N/A"
            
        data.append({
            'name': name,
            'price': price,
            'change_1h': change_1h,
            'change_24h': change_24h,
            'change_7d': change_7d,
            'market_cap': market_cap,
            'volume_24h': volume_24h,
            'circulating_supply': circulating_supply
        })

    return data

if __name__ == '__main__':
    handle()
