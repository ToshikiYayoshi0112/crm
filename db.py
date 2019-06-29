import sqlite3


def init_db():
    """データベースの初期化を行う関数"""
    conn = sqlite3.connect("crm.sqlite")

    cursor = conn.cursor()

    with open("scema.sql", mode="r") as f:
        sql = f.read()

    cursor.executescript(sql)

    conn.commit()

    conn.close()


if __name__ == "__main__":
    init_db()