import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint

scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secreat.json',scope)
client = gspread.authorize(creds)

sheet = client.open('Bar chart 1').sheet1
pp = pprint.PrettyPrinter() 
Bar = sheet.get_all_records()
row = sheet.row_values(3)
col = sheet.col_values(3)
cell = sheet.cell(2,2).value
pp.pprint(Bar)
pp.pprint(row)
print(col)
print(cell)
# print(Bar)