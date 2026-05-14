import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# Creates the database file in the root of RecordSubsystem
DB_PATH = os.path.normpath(os.path.join(BASE_DIR, "..", "mentor_caring_system.db"))


def get_connection() -> sqlite3.Connection:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn
