import streamlit as st
from datetime import datetime, timedelta

# =========================
# 🇫🇷 FORMAT DATE FRANÇAIS FIXE
# =========================

jours = {
    "Monday": "Lundi",
    "Tuesday": "Mardi",
    "Wednesday": "Mercredi",
    "Thursday": "Jeudi",
    "Friday": "Vendredi",
    "Saturday": "Samedi",
    "Sunday": "Dimanche"
}

mois = {
    "January": "janvier",
    "February": "février",
    "March": "mars",
    "April": "avril",
    "May": "mai",
    "June": "juin",
    "July": "juillet",
    "August": "août",
    "September": "septembre",
    "October": "octobre",
    "November": "novembre",
    "December": "décembre"
}

def format_date_fr(date_obj):
    raw_day = date_obj.strftime("%A")
    raw_month = date_obj.strftime("%B")
    day_num = date_obj.strftime("%d")
    return f"{jours[raw_day]} {day_num} {mois[raw_month]} {date_obj.year}"


# =========================
# 🕌 BASE KHATMA 138 OFFICIELLE
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
# 📌 RÉFÉRENCE
# =========================
BASE_KHATMA = 138
BASE_DATE = datetime(2026, 5, 19)

# =========================
# 🔁 ROTATION (bas → haut)
# =========================
def rotate(lst, n):
    n = n % len(lst)
    return lst[-n:] + lst[:-n]


# =========================
# 🎯 APP
# =========================
st.set_page_config(page_title="Khatma Generator", layout="centered")

st.markdown("<h2 style='text-align:center;'>🕌 Générateur de Khatma OFFICIEL 🕌</h2>", unsafe_allow_html=True)

khatma_number = st.number_input("🔢 Numéro de khatma", min_value=1, step=1)

if st.button("🚀 Générer"):

    shift = khatma_number - BASE_KHATMA
    rotated = rotate(names_base, shift)
    responsable = rotated[-1]
    end_date = BASE_DATE + timedelta(days=3 * shift)
    date_fr = format_date_fr(end_date)

    st.session_state.output = f"""بِسْمِ اللَّهِ الرَّحْمَنِ الرَّحِيمِ
وَالصَّلَاةُ وَالسَّلَامُ عَلَى سَيِّدِنَا وَحَبِيبِنَا مُحَمَّدٍ صَلَّى اللَّهُ عَلَيْهِ وَسَلَّمَ

🕌 {khatma_number}ᵉ khatma OFFICIEL 🕌
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
""".rstrip()

# =========================
# AFFICHAGE TOUJOURS
# =========================
if "output" in st.session_state:

    # =========================
    # 📋 BOUTON COPIE (NATIVE STREAMLIT)
    # =========================
   #st.markdown("### 📋 Copier le résultat")

    #st.info("👉 Clique dans le texte puis Ctrl+C (ou appui long sur téléphone)")
    
    # =========================
    # 📄 AFFICHAGE (EDITABLE)
    # =========================
    st.text_area("📋 Résultat", st.session_state.output, height=600)
