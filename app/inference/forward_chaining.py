from app.rules.rules_data import rules


def forward_chaining(input_gejala):
    """
    Forward Chaining dengan pendekatan persentase kecocokan
    """
    hasil_akhir = {
        "penyakit": "Tidak terdeteksi",
        "keyakinan": 0,
        "detail": []
    }

    semua_kandidat = []

    for rule in rules:
        gejala_rule = rule["if"]

        gejala_cocok = [g for g in gejala_rule if g in input_gejala]
        jumlah_cocok = len(gejala_cocok)
        total = len(gejala_rule)

        persentase = (jumlah_cocok / total) * 100 if total > 0 else 0

        semua_kandidat.append({
            "penyakit": rule["then"],
            "keyakinan": round(persentase, 1)
        })

        # threshold utama
        if persentase >= 60:
            hasil_akhir["detail"].append({
                "penyakit": rule["then"],
                "keyakinan": round(persentase, 1),
                "gejala_cocok": jumlah_cocok,
                "total_gejala_rule": total
            })

    # Jika ada yang lolos threshold
    if hasil_akhir["detail"]:
        terbaik = max(hasil_akhir["detail"], key=lambda x: x["keyakinan"])
        hasil_akhir["penyakit"] = terbaik["penyakit"]
        hasil_akhir["keyakinan"] = terbaik["keyakinan"]

    else:
        # fallback → ambil yang paling mendekati
        terbaik = max(semua_kandidat, key=lambda x: x["keyakinan"])
        hasil_akhir["penyakit"] = terbaik["penyakit"]
        hasil_akhir["keyakinan"] = terbaik["keyakinan"]

    return hasil_akhir


def hitung_skor(data):
    """
    Menghitung tingkat kecemasan berdasarkan standar GAD-7
    Skala: 0–3 per item, total 0–21
    """

    try:
        skor = sum(int(v) for v in data.values())
    except:
        skor = 0

    # Mapping GAD-7 (VALID JURNAL)
    if skor <= 4:
        tingkat = "Minimal"
    elif skor <= 9:
        tingkat = "Ringan"
    elif skor <= 14:
        tingkat = "Sedang"
    else:
        tingkat = "Berat"

    return tingkat