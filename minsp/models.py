from flask_login import UserMixin
from . import conn, login_manager
from psycopg2 import sql


@login_manager.user_loader
def load_user(user_id):
    cur = conn.cursor()
    id = 'cpr_number'

    user_sql = sql.SQL("""
    SELECT * FROM Patients
    WHERE cpr_number = %s
    """)

    cur.execute(user_sql, (int(user_id),))
    if cur.rowcount > 0:
        return Patients(cur.fetchone())
    else:
        return None



class Patients(tuple, UserMixin):
    def __init__(self, user_data):
        self.cpr_number = user_data[0]
        self.name = user_data[1]
        self.password = user_data[2]
        self.adress = user_data[3]

    def get_id(self):
        return self.cpr_number


class HbA1c_results(tuple):
    def __init__(self, user_data):
        self.test_id = user_data[0]
        self.result = user_data[1]
        self.date_of_test = user_data[2]
        self.cpr_number = user_data[3]

    def get_id(self):
        return self.test_id


def insert_Patients(cpr_number, name, password, address):
    cur = conn.cursor()
    sql = """
    INSERT INTO Patients(cpr_number, name, password, address)
    VALUES (%s, %s, %s, %s)
    """
    cur.execute(sql, (cpr_number, name, password, address))
    conn.commit()
    cur.close()

def insert_result(result, date_of_test, cpr_number):
    cur = conn.cursor()
    sql = """
        INSERT INTO HbA1c_results(result, date_of_test, cpr_number)
        VALUES (%s, %s, %s)
    """
    cur.execute(sql, (result, date_of_test, cpr_number))
    conn.commit()
    cur.close


def select_Patients(cpr_number):
    cur = conn.cursor()
    sql = """
    SELECT * FROM Patients
    WHERE cpr_number = %s
    """
    cur.execute(sql, (cpr_number,))
    user = Patients(cur.fetchone()) if cur.rowcount > 0 else None
    cur.close()
    return user

def select_all_data(cpr_number):
    cur = conn.cursor()
    sql = """
    SELECT result, date_of_test FROM HbA1c_results
    WHERE CPR_number = %s
    """
    cur.execute(sql, (cpr_number,))
    result = cur.fetchall() if cur.rowcount > 0 else None
    return result

