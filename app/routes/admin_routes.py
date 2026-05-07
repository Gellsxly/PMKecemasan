from flask import Blueprint, render_template, session, redirect, url_for, request, flash
from database.db import get_db_connection

admin = Blueprint('admin', __name__, url_prefix='/admin')


# =========================
# MIDDLEWARE ADMIN
# =========================
def admin_required():
    return session.get('username') and session.get('role') == 'admin'


# =========================
# DASHBOARD ADMIN
# =========================
@admin.route('/')
def admin_dashboard():

    if not admin_required():
        return redirect(url_for('auth.login'))

    conn = get_db_connection()

    users = conn.execute("SELECT * FROM users").fetchall()

    total_konsultasi = conn.execute(
        "SELECT COUNT(*) as total FROM hasil_konsultasi"
    ).fetchone()['total']

    conn.close()

    return render_template(
        'admin/dashboard.html',
        users=users,
        total_konsultasi=total_konsultasi
    )


# =========================
# EDUKASI - LIST
# =========================
@admin.route('/edukasi')
def edukasi():

    if not admin_required():
        return redirect(url_for('auth.login'))

    conn = get_db_connection()
    data = conn.execute(
        "SELECT * FROM edukasi ORDER BY tanggal DESC"
    ).fetchall()
    conn.close()

    return render_template('admin/edukasi/index.html', data=data)


# =========================
# EDUKASI - TAMBAH
# =========================
@admin.route('/edukasi/tambah', methods=['GET', 'POST'])
def tambah_edukasi():

    if not admin_required():
        return redirect(url_for('auth.login'))

    if request.method == 'POST':
        judul = request.form.get('judul')
        isi = request.form.get('isi')

        if not judul or not isi:
            flash('Judul dan isi wajib diisi!', 'danger')
            return redirect(request.url)

        conn = get_db_connection()
        conn.execute(
            "INSERT INTO edukasi (judul, isi) VALUES (?, ?)",
            (judul, isi)
        )
        conn.commit()
        conn.close()

        flash('Data edukasi berhasil ditambahkan!', 'success')
        return redirect(url_for('admin.edukasi'))

    return render_template('admin/edukasi/tambah.html')


# =========================
# EDUKASI - EDIT
# =========================
@admin.route('/edukasi/edit/<int:id>', methods=['GET', 'POST'])
def edit_edukasi(id):

    if not admin_required():
        return redirect(url_for('auth.login'))

    conn = get_db_connection()

    if request.method == 'POST':
        judul = request.form.get('judul')
        isi = request.form.get('isi')

        if not judul or not isi:
            flash('Judul dan isi wajib diisi!', 'danger')
            return redirect(request.url)

        conn.execute(
            "UPDATE edukasi SET judul=?, isi=? WHERE id=?",
            (judul, isi, id)
        )
        conn.commit()
        conn.close()

        flash('Data edukasi berhasil diupdate!', 'success')
        return redirect(url_for('admin.edukasi'))

    data = conn.execute(
        "SELECT * FROM edukasi WHERE id=?",
        (id,)
    ).fetchone()

    conn.close()

    return render_template('admin/edukasi/edit.html', data=data)


# =========================
# EDUKASI - HAPUS
# =========================
@admin.route('/edukasi/hapus/<int:id>', methods=['POST'])
def hapus_edukasi(id):

    if not admin_required():
        return redirect(url_for('auth.login'))

    conn = get_db_connection()
    conn.execute("DELETE FROM edukasi WHERE id=?", (id,))
    conn.commit()
    conn.close()

    flash('Data edukasi berhasil dihapus!', 'success')
    return redirect(url_for('admin.edukasi'))


# =========================
# GEJALA - LIST
# =========================
@admin.route('/gejala')
def gejala():

    if not admin_required():
        return redirect(url_for('auth.login'))

    conn = get_db_connection()
    data = conn.execute(
        "SELECT * FROM gejala ORDER BY id DESC"
    ).fetchall()
    conn.close()

    return render_template('admin/gejala/index.html', data=data)