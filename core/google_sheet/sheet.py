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
    text = worksheet_paid.cell(3,3).value
    return text

def text_paid():
    text = str(worksheet_paid.cell(2,1).value)
    print(text)
    return  text

def text_how_get_there():
    text = worksheet_paid.cell(4,3).value
    return text

def text_our_partner():
    text = worksheet_paid.cell(5,3).value
    return text

def text_download():
    text = worksheet_paid.cell(6,3).value
    return text