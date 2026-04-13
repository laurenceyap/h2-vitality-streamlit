import streamlit as st

st.set_page_config(page_title="H2 Vitality", page_icon="💧", layout="wide")

# Enhanced CSS for better spacing and fonts
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700;800&display=swap');
    
    .main { background-color: #0f1115; color: #ffffff; font-family: 'Inter', sans-serif; }
    .hero-title { 
        font-size: 85px; 
        font-weight: 800; 
        line-height: 0.9; 
        margin-bottom: 30px; 
        letter-spacing: -2px;
        color: white;
    }
    .hero-sub { font-size: 20px; color: #a1a1a6; margin-bottom: 40px; max-width: 500px; }
    .stButton>button { 
        background-color: #0071e3; 
        color: white; 
        border-radius: 30px; 
        padding: 15px 40px; 
        font-weight: bold; 
        border: none;
        font-size: 18px;
    }
    [data-testid="stHeader"] { background: rgba(0,0,0,0); }
    </style>
    """, unsafe_allow_html=True)

# Layout
col1, space, col2 = st.columns([1, 0.1, 1.2])

with col1:
    st.markdown("<br><br>", unsafe_allow_html=True) # Add top spacing
    st.markdown("<div class='hero-title'>Stop<br>Aging.<br>Start<br>Living.</div>", unsafe_allow_html=True)
    st.markdown("<div class='hero-sub'>Experience the ultimate biohack with Molecular Hydrogen inhalation. Science-backed wellness for longevity.</div>", unsafe_allow_html=True)
    if st.button("START YOUR JOURNEY"):
        st.balloons()

with col2:
    st.markdown("<br>", unsafe_allow_html=True)
    # Using a slightly different placeholder that looks more like a "Biohack" environment
    st.image("https://images.unsplash.com/photo-1576091160550-2173bdd99802?auto=format&fit=crop&q=80&w=1200", use_container_width=True)
