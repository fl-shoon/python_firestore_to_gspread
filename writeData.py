import gspread, csv
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials

# gathering essentials
# create a new project on Google Cloud Console
# create a service account in that project and download the json file of created service account
cred = ServiceAccountCredentials.from_json_keyfile_name('wired-name-363807-9beb11de2acd.json') 

# authorize the clientsheet 
client = gspread.authorize(cred)

# get the sample of the Spreadsheet
sheet = client.open("kostritzer_members.xlsx")

# tell csv path
csv_path = 'mydutiescsvfile.csv'

sheet.values_update(
    'datasheet',
    params={'valueInputOption': 'USER_ENTERED'},
    body={'values': list(csv.reader(open(csv_path, encoding='utf_8_sig')))}
)