import os
from services.DataBase import *
import datetime

statistics = DB("STATISTICS", date="TEXT", shop_map="INTEGER", call_staff="INTEGER", item_checker="INTEGER", \
                place_order="INTEGER", wrong_receipt="INTEGER", feedback="INTEGER")


def edit_stat(column):
    now = datetime.datetime.now()
    current_date = str('/'.join([str(now.year), str(now.day), str(now.month)]))

    res = statistics.get_items(date=current_date)

    if len(res) == 0:
        statistics.add_item(date=current_date, shop_map=0, call_staff=0, item_checker=0, place_order=0, \
                            wrong_receipt=0, feedback=0)

    with conn.begin() as temp:
        temp.execute(f"UPDATE {statistics.table_name} SET {column} = {column} + 1 WHERE date='{current_date}'")

    return 1
