import requests

url = 'https://api.weatherbit.io/v2.0/history/daily'



parameters = {
    'city_id': '4887398',
    'country': 'US',
    'start_date': '2020-01-01',
    'end_date': '2020-12-31',
    'key': 'c547694de9584ea1a649bdef2b8f3bb2'
}