import os
import streamlit as st

# Mengunci lokasi folder agar file media pasti terbaca dengan benar
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PATH_FOTO = os.path.join(BASE_DIR, "foto.jpg")
PATH_LAGU = os.path.join(BASE_DIR, "lagu.mp3")

# Konfigurasi Halaman Web
st.set_page_config(page_title="Happy Birthday, My Love! ❤️", page_icon="💖", layout="centered")

# Custom Styling Tampilan Romantis (CSS)
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #fff0f5 0%, #ffe4e1 50%, #ffd1dc 100%);
    }
    .love-title {
        color: #d81b60;
        text-align: center;
        font-family: 'Georgia', serif;
        font-size: 2.8em;
        font-weight: bold;
        margin-bottom: 10px;
    }
    .love-card {
        background-color: rgba(255, 255, 255, 0.95);
        padding: 25px;
        border-radius: 20px;
        box-shadow: 0px 8px 20px rgba(216, 27, 96, 0.15);
        border: 2px solid #ffb6c1;
        text-align: center;
        margin-top: 20px;
    }
    .romantic-text {
        color: #4a4a4a;
        font-size: 1.15em;
        line-height: 1.9;
    }
    .highlight {
        color: #e91e63;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# Judul Utama
st.markdown('<h1 class="love-title">🌹 Happy Birthday, My Love! 🌹</h1>', unsafe_allow_html=True)

# Input Nama Pasangan
nama = st.text_input("Masukkan nama panggilan kesayanganmu:", placeholder="Contoh: Sayang / Nama Pasangan")

# Tombol Kejutan
if st.button("💖 Buka Kejutan Spesial Buat Kamu 💖", use_container_width=True):
    if nama:
        # 1. Efek Balon Terbang
        st.balloons()
        
        # 2. Kartu Ucapan Pembuka
        st.markdown(f"""
        <div class="love-card">
            <h2 style="color: #d81b60;">🎉 Selamat Ulang Tahun, <span class="highlight">{nama}</span>! 🥰✨</h2>
            <hr style="border: 1px solid #ffb6c1;">
        </div>
        """, unsafe_allow_html=True)

        # 3. Pemutar Musik (lagu.mp3)
        st.write("🎵 **Dengarkan lagu spesial ini ya:**")
        if os.path.exists(PATH_LAGU):
            st.audio(PATH_LAGU, autoplay=True)
        else:
            st.error("❌ File 'lagu.mp3' belum ditemukan! Pastikan nama file lagumu sudah diubah jadi 'lagu.mp3'.")

        st.markdown("<br>", unsafe_allow_html=True)

        # 4. Tampilan Foto (foto.jpg)
        if os.path.exists(PATH_FOTO):
            st.image(PATH_FOTO, caption=f"Special Moment with {nama} ❤️", use_container_width=True)
        else:
            st.error("❌ File 'foto.jpg' belum ditemukan! Pastikan nama file fotomu sudah diubah jadi 'foto.jpg'.")

        # 5. Doa & Pesan Romantis
        st.markdown(f"""
        <div class="love-card">
            <p class="romantic-text">
                Terima kasih sudah lahir ke dunia dan menjadi alasan di balik senyumku setiap hari. 
                Di hari ulang tahunmu ini, aku berharap semua kebaikan dan kebahagiaan selalu menyertaimu.<br><br>
                <i>"Terima kasih sudah mau dirayakan, dan terima kasih sudah merayakanku."</i> 🎶❤️<br><br>
                Semoga kita bisa terus tumbuh bersama, melewati setiap momen indah maupun duka, 
                dan merayakan banyak hari ulang tahun berikutnya bareng-bareng lagi.
            </p>
            <h3 style="color: #e91e63; margin-top: 25px;">🎂 💕 🎁 🎂 💕 🎁</h3>
            <p style="color: #ad1457; font-weight: bold; font-size: 1.1em;">
                I love you always and forever! 💑✨
            </p>
        </div>
        """, unsafe_allow_html=True)
        
    else:
        st.warning("⚠️ Masukkan nama panggilan kesayanganmu dulu ya!")