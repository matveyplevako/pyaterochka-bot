from sqlalchemy import create_engine, update
import os
import psycopg2

link = os.environ['DATABASE_URL']
conn = create_engine(link)


class DB:

    def __init__(self, table_name, **kwargs):
        self.table_name = table_name
        self.fields = kwargs
        columns = ", ".join([arg + " " + arg_type for (arg, arg_type) in kwargs.items()])
        request = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns})"
        conn.execute(request)

    def add_item(self, **kwargs):
        columns = " AND ".join([arg + " = " + f"'{arg_value}'" for (arg, arg_value) in kwargs.items()])
        request = f"SELECT COUNT(*) FROM {self.table_name} WHERE {columns}"
        count = conn.execute(request)
        count = list(count)[0][0]
        if count != 0:
            return False

        order = list(kwargs.keys())
        columns_to_choose = ', '.join(order)
        values = [f"'{kwargs[arg]}'" for arg in order]
        values = ', '.join(values)
        request = f"INSERT INTO {self.table_name} ({columns_to_choose}) VALUES ({values})"
        conn.execute(request)
        return True

    def delete_item(self, **kwargs):
        columns = " AND ".join([arg + " = " + f"'{arg_value}'" for (arg, arg_value) in kwargs.items()])
        request = f"DELETE FROM {self.table_name} WHERE {columns}"
        conn.execute(request)

    def get_items(self, *args, **kwargs):
        sign = " = "
        if "sign" in kwargs:
            sign = kwargs[sign]

        columns = " AND ".join([arg + sign + f"'{arg_value}'" for (arg, arg_value) in kwargs.items()])
        request = f"SELECT * FROM {self.table_name} WHERE {columns}"
        return self.excecute(request)

    def get_all_rows(self):
        request = f"SELECT * FROM {self.table_name}"
        return self.excecute(request)

    def excecute(self, request):
        return [x for x in conn.execute(request)]

    def edit_stat(self, new_date, column):

        statistics_t = DB("STATISTICS", date="TEXT", shop_map="INTEGER", call_staff="INTEGER", item_checker="INTEGER", \
                        place_order="INTEGER", wrong_receipt="INTEGER", feedback="INTEGER")

        res = statistics_t.get_items(date=new_date)

        #statistics_t.excecute(f"DELETE FROM {statistics_t.table_name}")  #delete all  databse

        if len(res) == 0:
            statistics_t.add_item(date=new_date, shop_map=0, call_staff=0,  item_checker=0, place_order=0, \
                                  wrong_receipt=0, feedback=0)

        with conn.begin() as temp:
            temp.execute(f"UPDATE {statistics_t.table_name} SET {column} = {column} + 1 WHERE date='{new_date}'")



        return 1




