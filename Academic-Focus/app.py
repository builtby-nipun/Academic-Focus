from flask import Flask, render_template, request, redirect, url_for, jsonify, send_file, session
from models import init_db, create_task, get_tasks, update_task, delete_task
import csv, io
import datetime as dt
from config import Config

app = Flask(__name__, static_folder='static', template_folder='templates')
app.config.from_object(Config)
app.secret_key = "academic-focus-secret-key"

# Initialise database
init_db()


# ---------------------------
# Fake Authentication
# ---------------------------
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None

    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        password = request.form.get('password', '').strip()

        if username == "" or password == "":
            error = "Username and password are required."
        else:
            # Fake login - accept any creds that are non-empty
            session['user'] = username
            return redirect(url_for('index'))

    return render_template('login.html', error=error)


@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))


# ---------------------------
# Helper functions
# ---------------------------
def parse_date(s):
    if not s:
        return None
    try:
        return dt.datetime.strptime(s, "%Y-%m-%d").date()
    except ValueError:
        return None


def compute_stats(all_tasks):
    today = dt.date.today()
    week_end = today + dt.timedelta(days=7)

    total = len(all_tasks)
    completed = sum(1 for t in all_tasks if t["completed"])
    pending = total - completed

    due_today = 0
    due_this_week = 0

    for t in all_tasks:
        d = parse_date(t["due_date"])
        if not d:
            continue
        if d == today:
            due_today += 1
        if today <= d <= week_end:
            due_this_week += 1

    if total == 0:
        completion_pct = 0
    else:
        completion_pct = round((completed / total) * 100)

    return {
        "total": total,
        "completed": completed,
        "pending": pending,
        "due_today": due_today,
        "due_this_week": due_this_week,
        "completion_pct": completion_pct,
    }


def sort_and_filter(tasks, sort_by, priority_filter, status_filter):
    # Filter by priority
    if priority_filter != "all":
        tasks = [t for t in tasks if (t["priority"] or "").lower() == priority_filter.lower()]

    # Filter by completion status
    if status_filter == "pending":
        tasks = [t for t in tasks if not t["completed"]]
    elif status_filter == "completed":
        tasks = [t for t in tasks if t["completed"]]

    # Sorting
    if sort_by == "due":
        def sort_key(t):
            d = parse_date(t["due_date"])
            # None dates go to the end
            return (d is None, d or dt.date.max)
        tasks = sorted(tasks, key=sort_key)
    elif sort_by == "priority":
        order = {"High": 0, "Normal": 1, "Low": 2}
        tasks = sorted(tasks, key=lambda t: order.get(t["priority"], 3))
    elif sort_by == "course":
        tasks = sorted(tasks, key=lambda t: (t["course"] or "").lower())
    else:
        # default: most recent id last
        tasks = sorted(tasks, key=lambda t: t["id"])

    return tasks


# ---------------------------
# Dashboard / Home
# ---------------------------
@app.route('/')
def index():
    if 'user' not in session:
        return redirect(url_for('login'))

    # read sorting & filtering from query params
    sort_by = request.args.get("sort", "due")
    priority_filter = request.args.get("priority", "all")
    status_filter = request.args.get("status", "all")

    all_tasks = get_tasks()
    stats = compute_stats(all_tasks)
    visible_tasks = sort_and_filter(all_tasks, sort_by, priority_filter, status_filter)

    return render_template(
        'index.html',
        tasks=visible_tasks,
        username=session['user'],
        stats=stats,
        sort=sort_by,
        priority=priority_filter,
        status=status_filter,
    )


# ---------------------------
# Task operations
# ---------------------------
@app.route('/tasks', methods=['GET', 'POST'])
def tasks_route():
    if 'user' not in session:
        return redirect(url_for('login'))

    if request.method == 'POST':
        data = request.form
        create_task(
            data.get('title'),
            data.get('due_date'),
            data.get('priority'),
            data.get('course'),
        )
        # keep current filters after form submit
        return redirect(url_for('index'))

    else:
        return jsonify(get_tasks())


@app.route('/tasks/<int:task_id>', methods=['PATCH', 'DELETE'])
def modify_task(task_id):
    if 'user' not in session:
        return redirect(url_for('login'))

    if request.method == 'PATCH':
        completed_flag = request.form.get('completed', 'true').lower() in ('1', 'true', 'yes')
        update_task(task_id, completed=completed_flag)
        return jsonify({'status': 'ok'})
    else:
        delete_task(task_id)
        return jsonify({'status': 'deleted'})


@app.route('/export')
def export_csv():
    if 'user' not in session:
        return redirect(url_for('login'))

    tasks = get_tasks()
    si = io.StringIO()
    cw = csv.writer(si)
    cw.writerow(['id', 'title', 'due_date', 'priority', 'course', 'completed'])
    for t in tasks:
        cw.writerow([t['id'], t['title'], t['due_date'], t['priority'], t['course'], t['completed']])

    mem = io.BytesIO()
    mem.write(si.getvalue().encode('utf-8'))
    mem.seek(0)
    return send_file(mem, mimetype='text/csv', as_attachment=True, download_name='tasks_export.csv')


if __name__ == '__main__':
    app.run(debug=True)
