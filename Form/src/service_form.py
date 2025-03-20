from openpyxl import Workbook
from typing import Dict



def save_form(data:Dict):
    print(data["name"].get())
    wb = Workbook()
    ws = wb.active
    ws.append(["FirstName","LastName","Email","Phone","Address"])
    ws.append(
        [
            data["name"].get(),
            data["lastName"].get(),
            data["email"].get(),
            data["phone"].get(),
            data["address"].get()
        ]
    )
    wb.save("info.xlsx")
