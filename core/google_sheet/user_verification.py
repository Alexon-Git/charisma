from core.settings import worksheet_dop, client

"https://docs.google.com/spreadsheets/d/1y8OzKj8DtOIwHoSW94pPAxUktwt24n3ECb5Uzjqb2UY/edit#gid=691351806"

worksheet_sheet = worksheet_dop.cell(2,3).value
worksheet_name = worksheet_dop.cell(3,3).value
# print(chek_sheet)
chek_sheet = client.open_by_url(worksheet_sheet)
worksheet_check = chek_sheet.worksheet(worksheet_name)

def check_user(phone):
    col_phone = worksheet_check.col_values(5)[7:]
    print(col_phone)
    print(phone)
    for i in col_phone:
        print(phone, str(i)[-10:])
        if  phone == str(i)[-10:]:
            return True
        
    return False
 









