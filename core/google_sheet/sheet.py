from core.settings import *


def all_sheet_no_pay():
    sheet = worksheet_no_pay.get_all_values()
    return sheet


def all_sheet_speakers():
    sheet = worksheet_speaker.get_all_values()
    return sheet


def all_tariff():
    tariffs = worksheet_tariffs.col_values(1)
    return tariffs

def msg_tarif():
    msg = worksheet_tariffs.cell(2, 3).value  # строка столбец
    print(worksheet_tariffs.get_all_values())
    return msg


def text_timetable():
    text = worksheet_Dop.cell(2,1).value
    return text