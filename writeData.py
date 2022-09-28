import gspread, csv
from oauth2client.service_account import ServiceAccountCredentials

# gathering essentials
# create a new project on Google Cloud Console
# create a service account in that project and download the json file of created service account
cred = ServiceAccountCredentials.from_json_keyfile_name('your_google_cloud_service_key_file.json') 

# authorize the clientsheet 
client = gspread.authorize(cred)

# get the sample of the Spreadsheet
sheet = client.open("your_google_sheet_file.xlsx")

# tell csv path
csv_path = 'mycsvfile.csv'

sheet.values_update(
    'datasheet',
    params={'valueInputOption': 'USER_ENTERED'},
    body={'values': list(csv.reader(open(csv_path, encoding='utf_8_sig')))}
)
