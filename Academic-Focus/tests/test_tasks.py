import os
import pytest
from models import init_db, create_task, get_tasks, update_task, delete_task

def setup_function():
    try:
        os.remove('sstp.db')
    except OSError:
        pass
    init_db()

def test_create_and_get():
    tid = create_task('Test task', '2025-12-01', 'High', 'COMP2663')
    tasks = get_tasks()
    assert len(tasks) == 1
    assert tasks[0]['title'] == 'Test task'

def test_update_delete():
    tid = create_task('T', None, 'Low', None)
    update_task(tid, completed=True)
    tasks = get_tasks()
    assert tasks[0]['completed'] == 1
    delete_task(tid)
    tasks = get_tasks()
    assert tasks == []
