
import sqlite3
from models import Entry
from models import Mood
import json


def get_all_entries():
    
    with sqlite3.connect("./dailyjournal.db") as conn:

        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            e.id,
            e.datetime,
            e.content,
            e.tag,
            e.mood,
            m.name
        FROM entry e
        JOIN Mood m
            ON m.id = e.mood
        """)

        entries = []
        dataset = db_cursor.fetchall()

        for row in dataset:

            entry = Entry(row['id'],
                          row['datetime'],
                          row['content'], 
                          row['tag'], 
                          row['mood'])

            mood = Mood(row['id'],
                        row['name'])

            entry.mood = mood.__dict__

            entries.append(entry.__dict__)

    return json.dumps(entries)


def get_single_entry(id):

    with sqlite3.connect("./dailyjournal.db") as conn:

        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            e.id,
            e.datetime,
            e.content,
            e.tag,
            e.mood,
            m.name
        FROM entry e
        JOIN Mood m
            ON m.id = e.mood
        WHERE e.id = ?
        """, (id, ))

        data = db_cursor.fetchone()

        entry = Entry(data['id'],
                      data['datetime'],
                      data['content'], 
                      data['tag'], 
                      data['mood'])
                      
        mood = Mood(data['mood'],
                    data['name'])

        entry.mood = mood.__dict__

        return json.dumps(entry.__dict__)


def delete_entry(id):

    with sqlite3.connect("./dailyjournal.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM entry
        WHERE id = ?
        """, (id, ))


def search_entries(searchTerm):

    with sqlite3.connect("./dailyjournal.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            e.id,
            e.datetime,
            e.content,
            e.tag,
            e.mood
        FROM entry e
        WHERE e.content LIKE = ?
        """, ("% + searchTerm + %", ) )

        filtered_entries = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            entry = Entry(row['id'],
                          row['datetime'],
                          row['content'], 
                          row['tag'], 
                          row['mood'])

            filtered_entries.append(entry.__dict__)

    return json.dumps(filtered_entries)