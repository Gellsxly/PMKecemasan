from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from database.db import get_db_connection

auth = Blueprint('auth', __name__, url_prefix='/auth')


# =========================
# REGISTER
# =========================
@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = get_db_connection()

        # cek user sudah ada atau belum
        user = conn.execute(
            "SELECT * FROM users WHERE username = ?",
            (username,)
        ).fetchone()

        if user:
            flash('Username sudah digunakan!', 'danger')
            conn.close()
            return redirect(url_for('auth.register'))

        # insert user baru (default role user)
        conn.execute(
            "INSERT INTO users (username, password, role) VALUES (?, ?, ?)",
            (username, password, 'user')
        )
        conn.commit()
        conn.close()

        flash('Register berhasil! Silakan login.', 'success')
        return redirect(url_for('auth.login'))

    return render_template('auth/register.html')


# =========================
# LOGIN
# =========================
@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = get_db_connection()

        user = conn.execute(
            "SELECT * FROM users WHERE username = ? AND password = ?",
            (username, password)
        ).fetchone()

        conn.close()

        if user:
            # simpan session
            session['user_id'] = user['id']
            session['username'] = user['username']
            session['role'] = user['role']

            flash('Login berhasil!', 'success')
            return redirect(url_for('main.dashboard'))

        else:
            flash('Username atau password salah!', 'danger')
            return redirect(url_for('auth.login'))

    return render_template('auth/login.html')


# =========================
# LOGOUT
# =========================
@auth.route('/logout')
def logout():
    session.clear()
    flash('Berhasil logout!', 'info')
    return redirect(url_for('auth.login'))