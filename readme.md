# 🏪 MaduraPoint - Sistem Fuzzy Penentu Poin Loyalitas

📝 Deskripsi Proyek
MaduraPoint adalah aplikasi berbasis web yang menggunakan **Logika Fuzzy (Metode Sugeno)** untuk menentukan jumlah poin bonus bagi pelanggan Warung Madura. Sistem ini menggantikan perhitungan poin konvensional yang kaku menjadi lebih dinamis dan adil.

🚀 Urgensi & Nilai Guna
* **Masalah:** Perhitungan poin manual seringkali tidak adil. Pelanggan yang belanja banyak namun jarang datang disamakan dengan pelanggan yang belanja sedikit tapi sangat loyal (sering datang).
* **Solusi:** Dengan Logika Fuzzy, sistem dapat mempertimbangkan "area abu-abu" antara total belanja, frekuensi kedatangan, dan lama keanggotaan untuk menghasilkan skor loyalitas yang akurat.

🛠️ Metodologi (Fuzzy Logic)
Sistem ini menggunakan 3 variabel input dan 1 output:
1.  **Input:**
    * `Total Belanja` (Sedikit, Sedang, Banyak)
    * `Frekuensi Datang` (Jarang, Sering)
    * `Lama Member` (Baru, Lama)
2.  **Proses:**
    * **Fuzzifikasi:** Mengubah input tegas (Rupiah/Jumlah) menjadi nilai linguistik menggunakan fungsi keanggotaan linear.
    * **Inferensi:** Menerapkan 12 Rule Sugeno (contoh: *JIKA Belanja Banyak DAN Datang Sering, MAKA Poin Tinggi*).
    * **Defuzzifikasi:** Menghitung rata-rata berbobot (*Weighted Average*) untuk mendapatkan angka poin akhir.
3.  **Output:** Skor Loyalitas (0-50 Poin).

🖥️ Teknologi
* Python 3.x
* Streamlit (Web Framework)
* Deploy: Streamlit Cloud