# =========================================================
# initialize_db.py
# Initialize SQLite Database
# =========================================================

import sqlite3

DATABASE_PATH = "app/database/mentor_caring_system.db"

SCHEMA_PATH = "app/database/schema.sql"


def initialize_database():

    connection = sqlite3.connect(DATABASE_PATH)

    cursor = connection.cursor()

    with open(SCHEMA_PATH, "r", encoding="utf-8") as file:

        schema_sql = file.read()

    cursor.executescript(schema_sql)

    connection.commit()

    connection.close()

    print("Database initialized successfully.")


if __name__ == "__main__":

    initialize_database()
