import streamlit as st

# --- KONFIGURASI HALAMAN ---
st.set_page_config(page_title="MaduraPoint - Fuzzy System", layout="centered")

# --- FUNGSI INTI FUZZY (Pertahankan) ---
def fuzzify(x, a, b):
    """Fungsi linear untuk menghitung derajat keanggotaan"""
    if x <= a: return 0.0
    if x >= b: return 1.0
    return (x - a) / (b - a)

# --- TAMPILAN WEB (Pengganti Tkinter) ---
st.title("🏪 MaduraPoint Digital")
st.subheader("Sistem Fuzzy Penentu Poin Loyalitas")
st.markdown("---")

st.write("Silakan atur parameter pelanggan di bawah ini:")

# Input menggunakan Slider (Lebih modern daripada Entry box)
belanja = st.slider("Total Belanja (Ribu Rp):", 0, 100, 20)
freq = st.slider("Frekuensi Datang (Kali/Bulan):", 0, 10, 2)
masa = st.slider("Lama Jadi Member (Bulan):", 0, 12, 1)

if st.button("Analisis & Hitung Poin"):
    # 1. FUZZIFIKASI
    b_banyak = fuzzify(belanja, 40, 90)
    b_sedikit = 1 - b_banyak
    
    f_sering = fuzzify(freq, 2, 8)
    f_jarang = 1 - f_sering
    
    m_lama = fuzzify(masa, 3, 10)
    m_baru = 1 - m_lama

    # 2. INFERENSI (SUGENO)
    rules = []
    rules.append((min(b_sedikit, f_jarang, m_baru), 5))  
    rules.append((min(b_sedikit, f_jarang, m_lama), 10)) 
    rules.append((min(b_sedikit, f_sering, m_baru), 15)) 
    rules.append((min(b_sedikit, f_sering, m_lama), 20)) 
    rules.append((min(b_banyak, f_jarang, m_baru), 25))  
    rules.append((min(b_banyak, f_jarang, m_lama), 30))  
    rules.append((min(b_banyak, f_sering, m_baru), 40))  
    rules.append((min(b_banyak, f_sering, m_lama), 50))  

    # 3. DEFUZZIFIKASI
    pembilang = sum(alpha * z for alpha, z in rules)
    penyebut = sum(alpha for alpha, z in rules)
    hasil = pembilang / penyebut if penyebut != 0 else 5

    # TAMPILAN HASIL (Berkelas)
    st.markdown("### 📊 Hasil Perhitungan")
    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="Skor Loyalitas", value=f"{round(hasil, 2)}")
    with col2:
        st.metric(label="Total Poin", value=f"{int(hasil)} Poin")
    
    if hasil > 35:
        st.success("**Status: Pelanggan Sangat Loyal!**")
    elif hasil > 15:
        st.info("**Status: Pelanggan Potensial.**")
    else:
        st.warning("**Status: Pelanggan Baru/Jarang Belanja.**")