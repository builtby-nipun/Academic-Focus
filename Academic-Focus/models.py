import sqlite3
DB = 'sstp.db'

def get_db():
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db()
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            due_date TEXT,
            priority TEXT,
            course TEXT,
            completed INTEGER DEFAULT 0
        );
    ''')
    conn.commit()
    conn.close()

def create_task(title, due_date=None, priority='Normal', course=None):
    conn = get_db()
    cur = conn.cursor()
    cur.execute('INSERT INTO tasks (title,due_date,priority,course) VALUES (?,?,?,?)',
                (title, due_date, priority, course))
    conn.commit()
    tid = cur.lastrowid
    conn.close()
    return tid

def get_tasks():
    conn = get_db()
    cur = conn.cursor()
    cur.execute('SELECT id,title,due_date,priority,course,completed FROM tasks ORDER BY completed ASC, due_date')
    rows = cur.fetchall()
    conn.close()
    return [dict(r) for r in rows]

def update_task(task_id, completed=False):
    conn = get_db()
    cur = conn.cursor()
    cur.execute('UPDATE tasks SET completed=? WHERE id=?', (1 if completed else 0, task_id))
    conn.commit()
    conn.close()

def delete_task(task_id):
    conn = get_db()
    cur = conn.cursor()
    cur.execute('DELETE FROM tasks WHERE id=?', (task_id,))
    conn.commit()
    conn.close()
