from core.settings import worksheet_no_pay, worksheet_speaker


def all_sheet_no_pay():
    sheet = worksheet_no_pay.get_all_values()
    return sheet


def all_sheet_speakers():
    sheet = worksheet_speaker.get_all_values()
    return sheet




