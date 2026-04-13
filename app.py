import streamlit as st

# 1. Page Configuration for a Premium Look
st.set_page_config(
    page_title="H2 Vitality | Molecular Hydrogen",
    page_icon="💧",
    layout="wide"
)

# 2. Custom CSS for "Obsidian Grey" & Apple-style aesthetics
# FIXED: Changed unsafe_allow_contents to unsafe_allow_html
st.markdown("""
    <style>
    .main { background-color: #1a1a1a; color: #ffffff; }
    h1 { font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-weight: 700; color: #f5f5f7; }
    .stButton>button { border-radius: 20px; background-color: #0071e3; color: white; border: none; padding: 10px 25px; }
    .hero-text { font-size: 60px; line-height: 1.1; margin-bottom: 20px; font-weight: bold; }
    .stMarkdown { color: #f5f5f7; }
    </style>
    """, unsafe_allow_html=True)

# 3. Navigation Bar (Simple)
st.markdown("### H2 VITALITY | ADVANCED THERAPY | HEALTH BENEFITS")

# 4. Hero Section
col1, col2 = st.columns([1, 1])

with col1:
    st.markdown("<div class='hero-text'>Stop Aging.<br>Start Living.</div>", unsafe_allow_html=True)
    st.write("Experience the ultimate biohack with Molecular Hydrogen inhalation. Science-backed wellness for longevity.")
    if st.button("START YOUR JOURNEY"):
        st.balloons()

with col2:
    # Placeholder image for H2 Technology
    st.image("https://images.unsplash.com/photo-1518152006812-edab29b069ac?auto=format&fit=crop&q=80&w=1000")

# 5. Footer Disclaimer
st.divider()
st.info("Educational Disclaimer: This website is for informational purposes only and not a substitute for professional medical advice.")
