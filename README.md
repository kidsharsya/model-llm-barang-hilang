# Model Pencocokan Barang Hilang (LLM Similarity API)

Proyek ini adalah microservice berbasis Python FastAPI yang digunakan untuk mencocokkan laporan barang **hilang** dengan laporan **temuan**, berdasarkan kemiripan teks menggunakan model **sentence-transformers**.

Tujuannya adalah untuk membantu sistem manajemen barang hilang secara otomatis mencocokkan data dari dua jenis laporan dengan akurasi tinggi.

---

## 🚀 Teknologi & Model yang Digunakan

- **FastAPI** – Web framework ringan & cepat untuk API
- **Sentence-Transformers** – Model NLP untuk embedding teks
- Model yang digunakan: [`all-MiniLM-L6-v2`](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2)
  - Cepat dan cocok untuk task semantic text similarity
  - Mendukung banyak bahasa

---

## 🧠 Skema Input & Output

### 🔁 Endpoint: `POST /cocokkan`

**Request JSON:**

```json
{
  "hilang": ["Dompet coklat isi KTP dan ATM"],
  "temuan": ["Menemukan dompet kulit warna coklat berisi SIM dan ATM"]
}

Response JSON:

[
  {
    "index_hilang": 0,
    "index_temuan": 0,
    "similarity": 0.91
  }
]
```

### 🛠️ Cara Menjalankan Lokal

1. Clone Repo & Masuk ke Folder
   git clone https://github.com/kidsharsya/model-llm-barang-hilang.git
   cd model-llm-barang-hilang

2. Buat dan Aktifkan Virtual Environment

   python -m venv venv

   Windows: venv\Scripts\activate

   Mac: source venv/bin/activate

3. Install Dependencies
   pip install -r requirements.txt

4. Jalankan Server
   uvicorn embedding_service:app --reload --port 8000

5. Coba di Browser
   http://localhost:8000/docs

### 🔗 Integrasi

Layanan ini dirancang untuk diintegrasikan dengan frontend seperti Next.js, yang bisa mengirimkan laporan-laporan dari API utama ke endpoint ini untuk mendapatkan pasangan data yang memiliki kemiripan tinggi.

### 📝 Catatan Tambahan

Proses pencocokan hanya dilakukan untuk data yang status == "proses"
Cocok untuk di-deploy ke Render, Railway, atau VPS
