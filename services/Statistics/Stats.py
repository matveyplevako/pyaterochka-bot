import os
from services.Database.DataBase import DB

statistics = DB("STATISTICS", date="TEXT", shop_map="INTEGER", call_staff="INTEGER", item_checker="INTEGER",\
                place_order="INTEGER", wrong_receipt="INTEGER", feedback="INTEGER")