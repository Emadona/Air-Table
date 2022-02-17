import requests
from fundedandhiring import Fundedandhiring
import os


AIRTABLE_BASE_ID=os.environ.get("AIRTABLE_BASE_ID")
AIRTABLE_API_KEY=os.environ.get("AIRTABLE_API_KEY")
AIRTABLE_TABLE_NAME=os.environ.get("AIRTABLE_TABLE_NAME")

endpoint=f'https://api.airtable.com/v0/{AIRTABLE_BASE_ID}/{AIRTABLE_TABLE_NAME}'

headers = {
    "Authorization": f"Bearer {AIRTABLE_API_KEY}",
    "Content-Type": "application/json"
}

fi = Fundedandhiring()
all_data = fi.get_the_data()


database = []
if len(all_data)> 0:
    for da in all_data:
        database.append(da)
        if len(database) > 9:
            data ={
                'records' : database
            }
            re = requests.post(endpoint,headers=headers, json=data)
            print(re.json())
            database = []
    data = {
        'records' : database
    }
    re = requests.post(endpoint,headers=headers, json=data)
else:
    print('close')
