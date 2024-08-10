import os
import time
import sqlite3

from helper import validate_hex_color


def open_db() -> tuple[sqlite3.Connection, sqlite3.Cursor]:
    db_name = os.environ.get("DB_NAME")
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    return conn, c


def test_db():
    conn, cur = open_db()

    # Create table
    cur.executescript('''
    CREATE TABLE IF NOT EXISTS msg (id INTEGER PRIMARY KEY, content TEXT, image TEXT, time DATETIME DEFAULT CURRENT_TIMESTAMP, deleted INTEGER DEFAULT 0);
    CREATE TABLE IF NOT EXISTS theme (msg_color TEXT, bg_color TEXT, bg_img TEXT)
    ''')
    conn.commit()
    conn.close()


def get_msgid(msgid) -> dict:
    conn, cur = open_db()
    cur.execute("SELECT * FROM msg WHERE id = ? AND deleted = 0", (msgid,))
    row = cur.fetchone()
    conn.close()

    if row:
        return {
            "id": row[0],
            "content": row[1],
            "image": row[2],
            "time": row[3],
        }


def get_msg(offset, length) -> list[dict]:
    conn, cur = open_db()
    cur.execute("SELECT * FROM msg WHERE deleted = 0 ORDER BY time DESC LIMIT ? OFFSET ?", (length, offset))
    rows = cur.fetchall()
    conn.close()

    messages = []
    for row in rows:
        messages.append({
            "id": row[0],
            "content": row[1],
            "image": row[2],
            "time": row[3],
        })

    return messages


def create_msg(msg, img_name) -> dict:
    conn, cur = open_db()
    cur.execute("INSERT INTO msg (content, image) VALUES (?, ?)", (msg, img_name))
    conn.commit()

    msgid = cur.lastrowid
    cur.execute("SELECT * FROM msg WHERE id = ?", (msgid,))
    new_msg = cur.fetchone()
    conn.close()

    return {
        "id": new_msg[0],
        "content": new_msg[1],
        "image": new_msg[2],
        "time": new_msg[3],
    }


def delete_msg(msgid):
    conn, cur = open_db()
    cur.execute("UPDATE msg SET deleted = 1 WHERE id = ?", (msgid,))
    conn.commit()
    conn.close()


def get_total_msg() -> int:
    conn, cur = open_db()
    cur.execute("SELECT COUNT(*) FROM msg WHERE deleted = 0")
    count = cur.fetchone()[0]
    conn.close()

    return count


def get_theme() -> dict:
    conn, cur = open_db()
    cur.execute("SELECT * FROM theme LIMIT 1")
    row = cur.fetchone()
    conn.close()

    if row:
        return {
            "msg_color": row[0],
            "bg_color": row[1],
            "bg_img": row[2]
        }


def set_theme(msg_color, bg_color, bg_img_path) -> dict:
    conn, cur = open_db()
    if msg_color is not None:
        validate_hex_color(msg_color)
    if bg_color is not None:
        validate_hex_color(bg_color)

    # Check if a theme already exists
    cur.execute("SELECT COUNT(*) FROM theme")
    count = cur.fetchone()[0]
    if count == 0:
        # Insert a new theme if none exists
        cur.execute("INSERT INTO theme (msg_color, bg_color, bg_img) VALUES (?, ?, ?)",
                    (msg_color, bg_color, bg_img_path))
    else:
        # Update the existing theme
        if msg_color is not None:
            cur.execute("UPDATE theme SET msg_color = ? WHERE 1", (msg_color,))
        if bg_color is not None:
            cur.execute("UPDATE theme SET bg_color = ? WHERE 1", (bg_color,))
        if bg_img_path is not None:
            cur.execute("UPDATE theme SET bg_img = ? WHERE 1", (bg_img_path,))

    conn.commit()

    # Return the updated theme
    cur.execute("SELECT * FROM theme LIMIT 1")
    updated_theme = cur.fetchone()
    conn.close()

    return {
        "msg_color": updated_theme[0],
        "bg_color": updated_theme[1],
        "bg_img": updated_theme[2]
    }
