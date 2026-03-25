# 📊 E-Commerce Data Analysis Dashboard

Dashboard ini dibuat untuk menganalisis data e-commerce menggunakan metode Exploratory Data Analysis (EDA) dan RFM (Recency, Frequency, Monetary).

---

## 📌 Pertanyaan Bisnis

1. Bagaimana tren perubahan jumlah order setiap bulan dalam periode dataset, dan apakah terdapat pola tertentu seperti peningkatan atau penurunan yang signifikan?
2. Bagaimana distribusi total revenue pada setiap kota, dan kota mana yang memiliki kontribusi revenue terbesar dalam periode dataset?
3. Produk atau kategori produk mana yang paling diminati dan paling kurang diminati oleh pelanggan berdasarkan jumlah pembelian dan total revenue dalam periode dataset?
4. Bagaimana segmentasi pelanggan berdasarkan analisis RFM ke dalam kategori Lost, Low, Medium, High, dan Top, serta bagaimana karakteristik masing-masing segmen dalam periode dataset?

---

## 🚀 Setup Environment - Anaconda
conda create --name main-ds python=3.9
conda activate main-ds
pip install -r requirements.txt

## 📦 Setup Environment - Terminal
mkdir Proyek_Analisis_Data
cd Proyek_Analisis_Data
pipenv install
pipenv shell
pip install -r requirements.txt

---

## ▶️ Menjalankan Dashboard

Jalankan aplikasi Streamlit dengan perintah:

streamlit run dashboard.py

Setelah itu, dashboard akan terbuka di browser secara otomatis.

## 🌐 Akses Online

Dashboard juga dapat diakses melalui link berikut:

👉 (https://ecommerce-dashboard-vxtnsmtmb3dtmzvgcbnfsu.streamlit.app/)

---

## 🧠 Insight Utama

* Tren transaksi menunjukkan pola fluktuatif setiap bulan.
* Beberapa kota memiliki kontribusi revenue yang dominan.
* Terdapat perbedaan signifikan antara produk paling diminati dan kurang diminati.
* Segmentasi RFM berhasil mengelompokkan pelanggan menjadi Lost, Low, Medium, High, dan Top.
