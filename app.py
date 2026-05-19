import streamlit as st
from datetime import datetime, timedelta
import locale

# 🇫🇷 date en français
try:
    locale.setlocale(locale.LC_TIME, "fr_FR.UTF-8")
except:
    try:
        locale.setlocale(locale.LC_TIME, "fr_FR")
    except:
        pass


# =========================
# BASE OFFICIELLE KHATMA 138 (TON TEXTE)
# =========================
names_base = [
    "Mediba","Saber","Bahich","Kebe","Youssef34",
    "Abdelilah","Ousman","Abdelhedi","Dibassy","Bakar Timera",
    "Adama Timera","Ahmad","Mohamed Ali","Youssef","Moussa",
    "Brahim Ba","Bilel","Mamadou N","Zeid Timera","Ali E"
]

blocks = [
    "01 – 03","04 – 06","07 – 09","10 – 12","13 – 15",
    "16 – 18","19 – 21","22 – 24","25 – 27","28 – 30",
    "31 – 33","34 – 36","37 – 39","40 – 42","43 – 45",
    "46 – 48","49 – 51","52 – 54","55 – 57","58 – 60"
]

# =========================
# RÉFÉRENCE
# =========================
BASE_KHATMA = 138
BASE_DATE = datetime(2026, 5, 19)


# =========================
# ROTATION (DU HAUT VERS LE BAS)
# =========================
def rotate(lst, n):
    n = n % len(lst)
    return lst[-n:] + lst[:-n]


st.set_page_config(page_title="Khatma Generator", layout="centered")

st.markdown("## 🕌 Générateur de Khatma **OFFICIEL**")

khatma_number = st.number_input("🔢 Numéro de khatma", min_value=1, step=1)

if st.button("🚀 Générer"):

    shift = khatma_number - BASE_KHATMA

    rotated = rotate(names_base, shift)

    responsable = rotated[-1]

    end_date = BASE_DATE + timedelta(days=3 * shift)

    date_fr = end_date.strftime("%A %d %B %Y")

    output = f"""بِسْمِ اللَّهِ الرَّحْمَنِ الرَّحِيمِ
وَالصَّلَاةُ وَالسَّلَامُ عَلَى سَيِّدِنَا وَحَبِيبِنَا مُحَمَّدٍ صَلَّى اللَّهُ عَلَيْهِ وَسَلَّمَ

🕌 {khatma_number}ᵉ khatma 🕌
📅 Fin : {date_fr} au soir
👤 Responsable de la khatma : {responsable}

01 – 03 :: (60 – 58) : {rotated[0]}
04 – 06 :: (57 – 55) : {rotated[1]}
07 – 09 :: (54 – 52) : {rotated[2]}
10 – 12 :: (51 – 49) : {rotated[3]}
13 – 15 :: (48 – 46) : {rotated[4]}
16 – 18 :: (45 – 43) : {rotated[5]}
19 – 21 :: (42 – 40) : {rotated[6]}
22 – 24 :: (39 – 37) : {rotated[7]}
25 – 27 :: (36 – 34) : {rotated[8]}
28 – 30 :: (33 – 31) : {rotated[9]}
31 – 33 :: (30 – 28) : {rotated[10]}
34 – 36 :: (27 – 25) : {rotated[11]}
37 – 39 :: (24 – 22) : {rotated[12]}
40 – 42 :: (21 – 19) : {rotated[13]}
43 – 45 :: (18 – 16) : {rotated[14]}
46 – 48 :: (15 – 13) : {rotated[15]}
49 – 51 :: (12 – 10) : {rotated[16]}
52 – 54 :: (09 – 07) : {rotated[17]}
55 – 57 :: (06 – 04) : {rotated[18]}
58 – 60 :: (03 – 01) : {rotated[19]}

اللّهُمَّ اجعل هذه المشاركة بالآيات القرآنية في صحيفة حسناتكم،
اللّهُمَّ آمين يا ربّ العالمين
"""

    st.text_area("📋 Copie WhatsApp", output, height=600)