from flask import Blueprint, render_template
from database.db import get_db_connection

main = Blueprint('main', __name__)


# =========================
# 🏠 DASHBOARD
# =========================
@main.route('/')
def dashboard():
    return render_template('dashboard/index.html')


# =========================
# 📚 EDUKASI (USER)
# =========================
@main.route('/edukasi')
def edukasi():
    conn = get_db_connection()

    data = conn.execute(
        "SELECT * FROM edukasi ORDER BY tanggal DESC"
    ).fetchall()

    conn.close()

    return render_template('edukasi/index.html', data=data)