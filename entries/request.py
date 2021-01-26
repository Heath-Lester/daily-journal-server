
import sqlite3
import json


def get_all_entries():
    
    with sqlite3.connect("./dailyjournal.db") as conn:

        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            e.datetime,
            e.content,
            e.tag,
            e.mood,
            e.id
        FROM entry e
        """)

        entries = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            entry = Entry(row['datetime'],
                          row['content'], 
                          row['tag'], 
                          row['mood'],
                          row['id'])

            entries.append(entry.__dict__)

    return json.dumps(entries)


def get_single_entry(id):

    with sqlite3.connect("./dailyjournal.db") as conn:

        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            e.datetime,
            e.content,
            e.tag,
            e.mood,
            e.id
        FROM entry e
        WHERE e.id = ?
        """, (id, ))

        data = db_cursor.fetchone()

        entry = entry(row['datetime'],
                      row['content'], 
                      row['tag'], 
                      row['mood'],
                      row['id'])

        return json.dumps(entry.__dict__)


def delete_entry(id):

    with sqlite3.connect("./dailyjournal.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM entry
        WHERE id = ?
        """, (id, ))