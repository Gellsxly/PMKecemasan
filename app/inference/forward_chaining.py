from app.rules.rules_data import rules

def forward_chaining(input_gejala):
    hasil = "Tidak terdeteksi"

    for rule in rules:
        if all(g in input_gejala for g in rule["if"]):
            hasil = rule["then"]

    return hasil


def hitung_skor(data):
    total = sum(int(v) for v in data.values())

    if total <= 10:
        return "Ringan"
    elif total <= 20:
        return "Sedang"
    else:
        return "Berat"