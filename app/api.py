"""Mini API (opsional).
Pilih salah satu: FastAPI atau Flask.
Default di bawah menggunakan FastAPI. Jika ingin Flask, lihat komentar di bawah.

Jalankan (FastAPI):
  uvicorn app.api:app --reload --port 8000
"""

try:
    from fastapi import FastAPI, HTTPException
    from pydantic import BaseModel, Field
except Exception:
    # Jika FastAPI belum terpasang, kandidat bisa memasang via requirements.txt
    raise

app = FastAPI(title="Mini API - Checkout")

PRICE_TABLE = {
    "A1": 15000,
    "B7": 15000,
}

class Item(BaseModel):
    sku: str = Field(..., min_length=1)
    qty: int = Field(..., ge=1)

class CheckoutPayload(BaseModel):
    user: str = Field(..., min_length=1)
    items: list[Item] = Field(..., min_items=1)

@app.post("/api/checkout")
def checkout(payload: CheckoutPayload):
    total = 0
    for it in payload.items:
        if it.sku not in PRICE_TABLE:
            raise HTTPException(status_code=400, detail=f"Unknown SKU: {it.sku}")
        total += PRICE_TABLE[it.sku] * it.qty

    # Dummy order id generator (cukup untuk test)
    order_id = "ORD-2025-0001"
    return {"ok": True, "order_id": order_id, "total": total}


# --- Alternatif Flask (opsional) ---
# from flask import Flask, request, jsonify
# app = Flask(__name__)
# @app.post("/api/checkout")
# def checkout_flask():
#     ...  # implementasi validasi sederhana seperti di atas
#     return jsonify(...), 200
