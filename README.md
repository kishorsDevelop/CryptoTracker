# Web Scrapper Using Django and React

## Description

This Web Scrapper scrapes data from coinmarketcap.com and shows that data in tabular format on a web
page.
Web Scrapper implements the following features:
- It scrapes the following columns from coinmarketcap.com and
sends the data to Django via HTTP POST request every 5 seconds. The columns are
Name, Price, 1h%, 24h%, 7d%, Market Cap, Volume(24h), and Circulating Supply.
- A Django API accepts the HTTP POST request and updates the data in the
database.
- An HTTP GET request in the backend retrieves the latest data from the
database.
- Used React-based frontend that requests the data from the
backend using the GET request and displays the data in a tabular format on a web page.
The data should be automatically refreshed every 3 seconds.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)

## Installation

1. Clone the repository: 
```bash
git clone https://github.com/kishorsDevelop/Web_Scrapper.git
```
2. Install Dependencies:
  ```bash
pip install django
npm i axios@0.21.4
``` 

## Usage

1. Go to the web_scrapper folder and run the following command to start the Django server:
```bash
python manage.py runserver
```
2. Go to the web_scapper_app folder and run the following command to run the scrapper.py script to start fetching scrapped data from the website:
  ```bash
python scrapper.py
```
3. Go to the frontend/crypto-dashboard folder and run the following command to start the react app:
 ```bash
npm start
```

and now go to http://127.0.0.1:3000.

## Features

1. Scrap/Fetch data from coinmarketcap.com every 5 seconds.
2. Display data in the browser fetched every 3-5 seconds from HTTP GET API.
