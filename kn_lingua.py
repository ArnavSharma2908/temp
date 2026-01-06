import streamlit as st
import random

# ---------- MASTER DATA (NO MATRAs) ----------

kannada_letters = [
    # Vowels
    ("ಅ", "अ"), ("ಆ", "आ"), ("ಇ", "इ"), ("ಈ", "ई"), ("ಉ", "उ"), ("ಊ", "ऊ"),
    ("ಋ", "ऋ"), ("ಎ", "ए(s)"), ("ಏ", "ए(l)"), ("ಐ", "ऐ"),
    ("ಒ", "ओ(s)"), ("ಓ", "ओ(l)"), ("ಔ", "औ"),

    # Consonants
    ("ಕ", "क"), ("ಖ", "ख"), ("ಗ", "ग"), ("ಘ", "घ"), ("ಙ", "ङ"),
    ("ಚ", "च"), ("ಛ", "छ"), ("ಜ", "ज"), ("ಝ", "झ"), ("ಞ", "ञ"),
    ("ಟ", "ट"), ("ಠ", "ठ"), ("ಡ", "ड"), ("ಢ", "ढ"), ("ಣ", "ण"),
    ("ತ", "त"), ("ಥ", "थ"), ("ದ", "द"), ("ಧ", "ध"), ("ನ", "न"),
    ("ಪ", "प"), ("ಫ", "फ"), ("ಬ", "ब"), ("ಭ", "भ"), ("ಮ", "म"),
    ("ಯ", "य"), ("ರ", "र"), ("ಲ", "ल"), ("ವ", "व"),
    ("ಶ", "श"), ("ಷ", "ष"), ("ಸ", "स"), ("ಹ", "ह"), ("ಳ", "ळ")
]

# All Hindi sounds for generating options
hindi_sounds = list({hi for _, hi in kannada_letters})


# ---------- FUNCTIONS ----------

def generate_question():
    ka, correct_hi = random.choice(kannada_letters)

    # Generate wrong options
    wrong = random.sample(
        [x for x in hindi_sounds if x != correct_hi], 5
    )

    options = wrong + [correct_hi]
    random.shuffle(options)

    return {
        "ka": ka,
        "hi": correct_hi,
        "options": options
    }


# ---------- SESSION STATE ----------

if "question" not in st.session_state:
    st.session_state.question = generate_question()
    st.session_state.answer = None


# ---------- THEME ----------

st.markdown("""
<style>
.correct { color:#16A34A; font-size:26px; font-weight:bold; }
.wrong { color:#DC2626; font-size:26px; font-weight:bold; }
button { font-size:22px !important; }
</style>
""", unsafe_allow_html=True)


# ---------- UI ----------

st.title("🟡 Kannada → Hindi Sound Quiz")
st.caption("Select the correct Hindi sound")

st.markdown(
    f"<h1 style='text-align:center;font-size:90px;'>"
    f"{st.session_state.question['ka']}</h1>",
    unsafe_allow_html=True
)

# ---------- OPTIONS ----------

cols = st.columns(2)
for i, opt in enumerate(st.session_state.question["options"]):
    if cols[i % 2].button(opt, use_container_width=True):
        st.session_state.answer = opt


# ---------- FEEDBACK ----------

if st.session_state.answer:
    if st.session_state.answer == st.session_state.question["hi"]:
        st.markdown("<div class='correct'>✅ Correct!</div>", unsafe_allow_html=True)
        st.balloons()
    else:
        st.markdown(
            f"<div class='wrong'>❌ Wrong! Correct answer: "
            f"{st.session_state.question['hi']}</div>",
            unsafe_allow_html=True
        )

    if st.button("Next Question▶️"):
        st.session_state.question = generate_question()
        st.session_state.answer = None
        st.rerun()
