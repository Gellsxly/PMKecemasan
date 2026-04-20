# GEJALA PSIKOLOGIS
gejala_psikologis = [
    {"kode": "G1", "nama": "Berpikir berlebihan terhadap kemungkinan terburuk"},
    {"kode": "G2", "nama": "Mudah tersinggung, gugup, atau merasa tersudut"},
    {"kode": "G3", "nama": "Tidak bisa mengontrol rasa khawatir"},
    {"kode": "G4", "nama": "Sulit berkonsentrasi"},
    {"kode": "G5", "nama": "Sulit tidur nyenyak"},
]

# GEJALA FISIK
gejala_fisik = [
    {"kode": "G6", "nama": "Mudah lelah"},
    {"kode": "G7", "nama": "Sakit kepala"},
    {"kode": "G8", "nama": "Gemetar"},
    {"kode": "G9", "nama": "Berkeringat berlebihan"},
    {"kode": "G10", "nama": "Nyeri otot"},
    {"kode": "G11", "nama": "Kesulitan menelan"},
    {"kode": "G12", "nama": "Detak jantung meningkat"},
    {"kode": "G13", "nama": "Mual"},
    {"kode": "G14", "nama": "Sering buang air kecil"},
]

# Gabungan semua (untuk proses)
gejala = gejala_psikologis + gejala_fisik

rules = [
    {
        "if": ["G1", "G3", "G4"],
        "then": "Kecemasan Ringan"
    },
    {
        "if": ["G1", "G2", "G3", "G4", "G6", "G7"],
        "then": "Kecemasan Sedang"
    },
    {
        "if": ["G1", "G2", "G3", "G4", "G5", "G6", "G7", "G12"],
        "then": "Kecemasan Berat"
    }
]