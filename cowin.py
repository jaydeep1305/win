import json
import requests
from loguru import logger

authorization = 'Bearer xxx'
district_id = '775' # Rajkot Corporation [District]
date = '04-05-2021' # Date 
min_age_limit = 18 # or 45

try:
    headers = {
        'authority': 'cdn-api.co-vin.in',
        'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
        'accept': 'application/json, text/plain, */*',
        'authorization': authorization,
        'sec-ch-ua-mobile': '?0',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
        'origin': 'https://selfregistration.cowin.gov.in',
        'sec-fetch-site': 'cross-site',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://selfregistration.cowin.gov.in/',
        'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7,hi;q=0.6,gu;q=0.5,fr;q=0.4',
        'if-none-match': 'W/"1108a-UG0WBb8LhfkliVgLulCjRA0eczg"',
    }

    params = (
        ('district_id', district_id),
        ('date', date),
    )

    response = requests.get('https://cdn-api.co-vin.in/api/v2/appointment/sessions/calendarByDistrict', headers=headers, params=params)
    err_response = response = response.content.decode()
    response = json.loads(response)
    response = response['centers']
    for res in response:
        center_name = res['name']
        res = res['sessions']
        for rs in res:
            if rs['min_age_limit'] == min_age_limit:
                if rs['available_capacity'] != 0 :
                    logger.debug(center_name + " - " + str(rs['available_capacity']) + " - " + str(rs['date']))
    logger.info("dummy - " + center_name)
except Exception as ex:
    logger.error(ex)
    logger.error(err_response)
    