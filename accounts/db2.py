import pyodbc
from django.conf import settings


def get_connection():
    cfg = settings.DB2_ODBC

    conn_str = (
        f"DSN={cfg['DSN']};"
        f"UID={cfg['UID']};"
        f"PWD={cfg['PWD']};"
        "CHARSET=UTF-8;"
    )

    return pyodbc.connect(conn_str)


def check_login(userid, password):
    conn = None

    try:
        conn = get_connection()
        cursor = conn.cursor()

        sql = """
            SELECT USERID
            FROM KVXA.XAA0300
            WHERE USERID = ?
              AND PASSWD = ?
            FETCH FIRST 1 ROWS ONLY
        """

        cursor.execute(sql, (userid, password))
        row = cursor.fetchone()

        return row is not None

    except Exception as e:
        print("DB2 Login Error:", e)
        return False

    finally:
        if conn:
            conn.close()