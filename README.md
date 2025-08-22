# Mini Technical Test – Fullstack Developer (Middle)

Fokus: **Fundamental Python**, **logical thinking**, **komunikasi/dokumentasi**, dan **alur problem solving**.
Estimasi waktu: **90–120 menit** total.

## Aturan
- Gunakan **Python 3.10+**.
- Anda boleh menggunakan **pytest** untuk unit test.
- **Bagian B (Mini API)** opsional (disarankan). Boleh menggunakan **FastAPI** atau **Flask**.
- Kirimkan jawaban dalam repository (GitHub/GitLab). Sertakan repo ini sebagai dasar (fork/clone atau copy).

## Tugas
### Bagian A — Python Fundamentals & Logic
Implementasikan fungsi-fungsi berikut di `app/core.py`:
- `total_paid_by_user(txns: list[dict]) -> dict[str, int]`
- `top_user_by_paid_amount(txns: list[dict]) -> tuple[str, int]`
- `to_snake_case(s: str) -> str`

Contoh data transaksi (boleh Anda letakkan di test atau file JSON kecil):
```
[
  {"user": "anna", "amount": 12000, "status": "PAID"},
  {"user": "budi", "amount": 8000,  "status": "PENDING"},
  {"user": "anna", "amount": 3000,  "status": "PAID"},
  {"user": "cici", "amount": 15000, "status": "PAID"},
  {"user": "budi", "amount": 7000,  "status": "FAILED"}
]
```

Tambahkan unit test di `tests/test_core.py`. Uji kasus normal dan edge case sederhana.

Di **README ini**, jelaskan singkat kompleksitas waktu/spasi (big-O) dari fungsi di atas (2–4 kalimat).

### Bagian B — Mini API (opsional, disarankan)
Implementasikan endpoint `POST /api/checkout` di `app/api.py` (FastAPI/Flask). Validasi sederhana:
- `user`: string non-kosong
- `items`: list minimal 1; tiap item berisi `sku` (string) dan `qty` (int ≥ 1)

Gunakan price table kecil (in-memory) misal: `A1=15000`, `B7=15000`.
Response sukses contoh:
```
{"ok": true, "order_id": "ORD-2025-0001", "total": 45000}
```

Jika validasi gagal: HTTP 400 dengan pesan ringkas.

### Bagian C — Problem Solving & Komunikasi
Di akhir **README** ini (atau file terpisah), tuliskan secara ringkas & runtut:
1. **Debug Scenario:** `POST /api/checkout` kadang 500 di staging. Apa langkah Anda untuk isolasi & menemukan root cause?
2. **Design Decision:** Desain singkat untuk **idempotency** pada endpoint tersebut.

### Bagian D — Dokumentasi
- Jelaskan **cara menjalankan** & **cara menjalankan test**.
- Jelaskan **struktur folder** singkat.
- Tuliskan **keputusan teknis** penting.

## Cara Menjalankan
```
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt

# menjalankan test
pytest -q

# (opsional) menjalankan API - FastAPI
uvicorn app.api:app --reload --port 8000
# atau Flask (lihat komentar di app/api.py)
```

## Struktur Folder
```
app/
  __init__.py
  core.py        # tempat fungsi Bagian A
  api.py         # (opsional) mini API
tests/
  test_core.py   # unit tests
README.md
DECISION_LOG.md  # catat keputusan singkat Anda
requirements.txt
```

## Kejujuran & Anti‑AI Ringan
Tambahkan poin keputusan Anda di `DECISION_LOG.md` (5–8 bullet). Commit bertahap & wajar. Boleh pakai dokumentasi resmi sebagai referensi, tapi **kerjakan sendiri**.

---

## Kompleksitas (isi oleh kandidat)
_Tulis di sini analisis big‑O singkat untuk fungsi di Bagian A._