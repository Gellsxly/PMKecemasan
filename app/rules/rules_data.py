# =========================
# 🧠 INSTRUMEN GAD-7 (VALID)
# =========================
gejala_gad7 = [
    {"kode": "G1", "nama": "Merasa gugup, cemas, atau tegang"},
    {"kode": "G2", "nama": "Tidak mampu mengontrol rasa khawatir"},
    {"kode": "G3", "nama": "Khawatir berlebihan tentang berbagai hal"},
    {"kode": "G4", "nama": "Kesulitan untuk rileks"},
    {"kode": "G5", "nama": "Gelisah sehingga sulit diam"},
    {"kode": "G6", "nama": "Mudah merasa kesal atau marah"},
    {"kode": "G7", "nama": "Merasa takut sesuatu buruk akan terjadi"},
]

# =========================
# 📊 KATEGORI GAD-7 (VALID JURNAL)
# =========================
kategori_gad7 = {
    "minimal": range(0, 5),
    "ringan": range(5, 10),
    "sedang": range(10, 15),
    "berat": range(15, 22)
}

# =========================
# 🔗 RULES (INTERPRETASI TAMBAHAN)
# =========================
# Digunakan untuk memberi insight, bukan diagnosis utama

rules = [

    # 🔹 Kecemasan Kognitif
    {
        "if": ["G1", "G2", "G3"],
        "then": "Indikasi kecemasan kognitif (overthinking)"
    },

    # 🔹 Kesulitan relaksasi
    {
        "if": ["G4", "G5"],
        "then": "Indikasi kesulitan relaksasi dan ketegangan"
    },

    # 🔹 Emosi tidak stabil
    {
        "if": ["G5", "G6"],
        "then": "Indikasi kecemasan dengan gangguan emosional"
    },

    # 🔹 Ketakutan berlebih
    {
        "if": ["G1", "G7"],
        "then": "Indikasi rasa takut berlebihan"
    },

    # 🔹 Kombinasi berat
    {
        "if": ["G1", "G2", "G3", "G4", "G5"],
        "then": "Indikasi kecemasan tinggi (perlu perhatian serius)"
    }
]

# =========================
# 🔄 BACKWARD COMPATIBILITY
# =========================
# Supaya tidak error di file lain

gejala_panik = gejala_gad7
gejala_sosial = []
gejala_umum = []

semua_gejala = gejala_gad7