# Mini Technical Test – Fullstack Developer (Middle)

Fokus tes ini ada di:

* **Fundamental Python** (bisa nulis fungsi sederhana dengan benar).
* **Logical thinking** (cara berpikir runtut & masuk akal).
* **Komunikasi & dokumentasi** (jelas menuliskan apa yang dibuat).
* **Problem solving** (menjelaskan langkah/ide dengan bahasa sederhana).

Estimasi waktu pengerjaan: **90–120 menit**.

---

## Aturan

* Gunakan **Python 3.10+**.
* Testing boleh menggunakan **pytest**.
* **Bagian B (Mini API)** opsional tapi nilai plus. Bisa pilih **FastAPI** atau **Django**.
* Jawaban dikumpulkan dalam bentuk repository (GitHub/GitLab).
* Boleh gunakan repo template yang diberikan sebagai dasar.

---

## Bagian A — Python Fundamentals & Logic

Buat fungsi berikut di `app/core.py`:

* `total_paid_by_user(txns: list[dict]) -> dict[str, int]`
* `top_user_by_paid_amount(txns: list[dict]) -> tuple[str, int]`
* `to_snake_case(s: str) -> str`

**Contoh data transaksi:**

```json
[
  {"user": "anna", "amount": 12000, "status": "PAID"},
  {"user": "budi", "amount": 8000,  "status": "PENDING"},
  {"user": "anna", "amount": 3000,  "status": "PAID"},
  {"user": "cici", "amount": 15000, "status": "PAID"},
  {"user": "budi", "amount": 7000,  "status": "FAILED"}
]
```

* Tambahkan unit test di `tests/test_core.py`.
* Uji **kasus normal** dan **edge case sederhana** (misal: transaksi kosong).

**Tambahan:**
Di bagian akhir README ini, tulis singkat analisis performa fungsi kamu pakai **big-O notation**.
👉 Tidak perlu detail matematis, cukup 2–3 kalimat.
Contoh:

> “Fungsi `total_paid_by_user` loop semua transaksi 1 kali → O(n). Space O(u) untuk jumlah user unik.”

---

## Bagian B — Mini API (opsional tapi disarankan)

Buat endpoint `POST /api/checkout` di `app/api.py`.
Aturan request:

* `user`: string, wajib diisi.
* `items`: list minimal 1 item, tiap item punya `sku` (string) & `qty` (integer ≥ 1).

Gunakan tabel harga kecil (hardcode, in-memory), misalnya:

* `A1 = 15000`
* `B7 = 15000`

**Contoh request:**

```json
{"user":"anna","items":[{"sku":"A1","qty":2},{"sku":"B7","qty":1}]}
```

**Contoh response sukses:**

```json
{"ok": true, "order_id":"ORD-2025-0001", "total":45000}
```

Kalau request tidak valid → balas dengan **HTTP 400** + pesan error sederhana.
👉 Tidak perlu database, cukup in-memory. Fokus ke validasi & struktur kode.

---

## Bagian C — Problem Solving & Komunikasi

Tulis jawaban di README (cukup 5–10 kalimat tiap poin):

1. **Debug Scenario**
   API `POST /api/checkout` kadang error 500 di staging.
   → Jelaskan langkah-langkah **sederhana & runtut** yang kamu lakukan untuk mencari penyebab (contoh: cek log, cek input data, dll).

2. **Design Decision**
   Kalau API ini butuh **idempotency** (supaya tidak double charge kalau user klik submit 2x), jelaskan dengan kata-kata:

   * Apa idenya?
   * Data/identifier apa yang dipakai untuk memastikan request sama tidak dieksekusi 2x?
     👉 Tidak perlu bikin diagram/DFD, cukup penjelasan singkat.

---

## Bagian D — Dokumentasi

Di README jelaskan secara ringkas:

* Cara menjalankan aplikasi.
* Cara menjalankan test.
* Struktur folder singkat.
* Keputusan teknis penting (misal: kenapa pilih FastAPI, kenapa test ditulis seperti itu).

---

## Cara Menjalankan (contoh)

```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt

# Menjalankan test
pytest -q

# (Opsional) Menjalankan API dengan FastAPI
uvicorn app.api:app --reload --port 8000
```

---

## Struktur Folder (template)

```
app/
  __init__.py
  core.py        # fungsi-fungsi Bagian A
  api.py         # (opsional) mini API
tests/
  test_core.py   # unit tests
README.md
DECISION_LOG.md  # catatan keputusan singkat
requirements.txt
```

---

## Kejujuran & Anti-AI Ringan

* Tambahkan catatan 5–8 bullet di `DECISION_LOG.md` tentang keputusanmu saat mengerjakan (contoh: “Pilih FastAPI karena lebih familiar”).
* Commit harus bertahap, bukan sekali commit semua.
* Boleh baca dokumentasi resmi, tapi **kerjakan sendiri**.

---

## Kompleksitas (diisi kandidat)

*Tulis di sini analisis big-O singkat dari fungsi di Bagian A.*