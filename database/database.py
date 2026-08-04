# database/database.py

import sqlite3

DATABASE_NAME = "chatbot.db"


def get_connection():
    """
    Create and return a SQLite connection.
    """
    return sqlite3.connect(DATABASE_NAME)


def initialize_database():
    """
    Create required tables if they don't exist.
    """

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS conversations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            role TEXT NOT NULL,
            message TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.commit()
    conn.close()


def save_message(role: str, message: str):
    """
    Save a message to the database.
    """

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO conversations(role, message)
        VALUES(?, ?)
        """,
        (role, message)
    )

    conn.commit()
    conn.close()


def get_history():
    """
    Return all conversation history.
    """

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT role, message
        FROM conversations
        ORDER BY id
    """)

    rows = cursor.fetchall()

    conn.close()

    return [
        {
            "role": row[0],
            "content": row[1]
        }
        for row in rows
    ]


def clear_history():
    """
    Delete all stored conversations.
    """

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM conversations")

    conn.commit()
    conn.close()
