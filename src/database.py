import sqlite3

def save_to_db(df):
    conn = sqlite3.connect("burs.db")
    df.to_sql("compliance", conn, if_exists="replace", index=False)
    conn.close()
