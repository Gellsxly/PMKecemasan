from flask import Blueprint, render_template, request, session, redirect, url_for
from app.rules.rules_data import gejala_gad7
from app.inference.forward_chaining import forward_chaining, hitung_skor
from database.db import get_db_connection

konsultasi = Blueprint('konsultasi', __name__, url_prefix='/konsultasi')


# =========================
# 🧠 HALAMAN KONSULTASI
# =========================
@konsultasi.route('/', methods=['GET', 'POST'])
def konsultasi_page():

    # 🔒 WAJIB LOGIN
    if not session.get('username'):
        return redirect(url_for('auth.login'))

    # =========================
    # POST → PROSES DIAGNOSA
    # =========================
    if request.method == 'POST':
        data = request.form.to_dict()

        print("DATA MASUK:", data)

        # Ambil gejala aktif (nilai > 0)
        gejala_aktif = [k for k, v in data.items() if int(v) > 0]

        # Forward chaining (interpretasi tambahan)
        hasil_fc = forward_chaining(gejala_aktif)

        # Handle jika return bukan dict (biar aman)
        if isinstance(hasil_fc, dict):
            hasil = hasil_fc.get("penyakit", "Indikasi kecemasan")
            keyakinan = hasil_fc.get("keyakinan", 0)
        else:
            hasil = hasil_fc
            keyakinan = 0

        # Hitung skor GAD-7
        tingkat = hitung_skor(data)

        # Hitung total skor
        skor = sum(int(v) for v in data.values())

        # =========================
        # 💾 SIMPAN KE DATABASE
        # =========================
        try:
            conn = get_db_connection()

            # Coba simpan dengan keyakinan
            try:
                conn.execute(
                    '''
                    INSERT INTO hasil_konsultasi (username, hasil, tingkat, keyakinan)
                    VALUES (?, ?, ?, ?)
                    ''',
                    (session['username'], hasil, tingkat, keyakinan)
                )
            except:
                # fallback kalau kolom belum ada
                conn.execute(
                    '''
                    INSERT INTO hasil_konsultasi (username, hasil, tingkat)
                    VALUES (?, ?, ?)
                    ''',
                    (session['username'], hasil, tingkat)
                )

            conn.commit()
            conn.close()

        except Exception as e:
            print("ERROR SIMPAN DB:", e)

        return render_template(
            'konsultasi/hasil.html',
            hasil=hasil,
            tingkat=tingkat,
            keyakinan=keyakinan,
            skor=skor
        )

    # =========================
    # GET → FORM GAD-7
    # =========================
    return render_template(
        'konsultasi/form.html',
        gejala_gad7=gejala_gad7
    )


# =========================
# 📊 RIWAYAT KONSULTASI
# =========================
@konsultasi.route('/riwayat')
def riwayat():

    if not session.get('username'):
        return redirect(url_for('auth.login'))

    try:
        conn = get_db_connection()

        data = conn.execute(
            '''
            SELECT * FROM hasil_konsultasi
            WHERE username = ?
            ORDER BY tanggal DESC
            ''',
            (session['username'],)
        ).fetchall()

        conn.close()

    except Exception as e:
        print("ERROR AMBIL DATA:", e)
        data = []

    return render_template(
        'konsultasi/riwayat.html',
        data=data
    )