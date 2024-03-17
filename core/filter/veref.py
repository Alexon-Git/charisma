from core.settings import worksheet_paid



def Checking_phone(id) -> bool:
        call = worksheet_paid.col_values(3)
        have = False
        for i in range(len(call)):
            if (call[i] == str(id)):
                have = True
        return have