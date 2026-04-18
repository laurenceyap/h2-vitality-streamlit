import streamlit as st
import google.generativeai as genai

# --- 1. SETTINGS & PREMIUM THEME ---
st.set_page_config(page_title="H2 Vitality | Advanced Therapy", page_icon="💧", layout="wide")

# Custom CSS for the Apple/Obsidian Aesthetic
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700;800&display=swap');
    .main { background-color: #0f1115; color: #ffffff; font-family: 'Inter', sans-serif; }
    .stApp { background-color: #0f1115; }
    h1 { font-size: 72px; font-weight: 800; line-height: 1; color: #f5f5f7; letter-spacing: -2px; }
    .hero-sub { font-size: 20px; color: #a1a1a6; margin-bottom: 30px; }
    .stButton>button { background-color: #0071e3; color: white; border-radius: 40px; padding: 12px 30px; border: none; font-weight: bold; }
    .card { background-color: #1c1c1e; padding: 25px; border-radius: 15px; border: 1px solid #3a3a3c; margin-bottom: 20px; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. HERO SECTION ---
col1, col2 = st.columns([1, 1.2])

with col1:
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("<span style='color: #0071e3; font-weight: bold; letter-spacing: 1px;'>⚡ THE ULTIMATE BIOHACK</span>", unsafe_allow_html=True)
    st.markdown("<h1>Stop Aging.<br>Start Living.</h1>", unsafe_allow_html=True)
    st.markdown("<div class='hero-sub'>Unlock the secret to longevity. Molecular hydrogen is the world's most powerful selective antioxidant, engineered to reboot your cellular health.</div>", unsafe_allow_html=True)
    if st.button("START YOUR JOURNEY"):
        st.balloons()

with col2:
    st.markdown("<br>", unsafe_allow_html=True)
    st.image("https://images.unsplash.com/photo-1576091160550-2173bdd99802?q=80&w=1200", use_container_width=True)

# --- 3. THE 30 PATHWAYS SECTION ---
st.write("---")
st.markdown("<h2 style='text-align: center;'>The 30 Pathways of Vitality</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #a1a1a6;'>Systemic orchestration of health across 30 distinct biological pathways.</p>", unsafe_allow_html=True)

p1, p2, p3 = st.columns(3)

with p1:
    st.markdown("<div class='card'><h3>Cellular Defense</h3><p>Selective Antioxidant support targeting hydroxyl radicals and peroxynitrite.</p></div>", unsafe_allow_html=True)
    st.markdown("<div class='card'><h3>Nrf2 Activation</h3><p>Boosts your body's own antioxidant enzymes like SOD and Catalase.</p></div>", unsafe_allow_html=True)

with p2:
    st.markdown("<div class='card'><h3>Metabolic Health</h3><p>SIRT1 Activation to promote longevity and healthy aging at a genetic level.</p></div>", unsafe_allow_html=True)
    st.markdown("<div class='card'><h3>Mitochondrial Support</h3><p>Protects the energy-producing powerhouses of your cells.</p></div>", unsafe_allow_html=True)

with p3:
    st.markdown("<div class='card'><h3>Neuroprotection</h3><p>Effortlessly crosses the blood-brain barrier for direct cognitive protection.</p></div>", unsafe_allow_html=True)
    st.markdown("<div class='card'><h3>Cognitive Clarity</h3><p>Reduces neuro-inflammation for sharper focus and memory.</p></div>", unsafe_allow_html=True)

# --- 4. EDUCATIONAL DISCLAIMER ---
st.divider()
st.caption("Educational Disclaimer: This website is for informational purposes only. Molecular hydrogen inhalation is a wellness practice and not a substitute for professional medical advice.")
