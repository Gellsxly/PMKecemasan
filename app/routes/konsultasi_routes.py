from flask import Blueprint, render_template, request
from app.rules.rules_data import gejala_psikologis, gejala_fisik
from app.inference.forward_chaining import forward_chaining, hitung_skor

konsultasi = Blueprint('konsultasi', __name__)

@konsultasi.route('/konsultasi', methods=['GET', 'POST'])
def konsultasi_page():

    if request.method == 'POST':

        data = request.form.to_dict()

        # DEBUG (optional, lihat di terminal)
        print(data)

        # Ambil gejala aktif (nilai > 0)
        gejala_aktif = [k for k, v in data.items() if int(v) > 0]

        # Forward chaining
        hasil = forward_chaining(gejala_aktif)

        # Hitung skor
        tingkat = hitung_skor(data)

        return render_template(
            'konsultasi/hasil.html',
            hasil=hasil,
            tingkat=tingkat
        )

    return render_template(
        'konsultasi/form.html',
        gejala_psikologis=gejala_psikologis,
        gejala_fisik=gejala_fisik
    )