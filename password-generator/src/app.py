import streamlit as st
from utils.password_utils import generate_password, check_password_strength
from config.constants import DEFAULT_LENGTH, SPECIAL_CHARS

# Session state initialization
if 'generated_pwd' not in st.session_state:
    st.session_state.generated_pwd = None

# Sidebar controls
with st.sidebar:
    st.title("Password Configuration")
    length = st.slider("Length", 8, 64, DEFAULT_LENGTH)
    col1, col2 = st.columns(2)
    with col1:
        include_upper = st.checkbox("Uppercase (A-Z)", True)
        include_lower = st.checkbox("Lowercase (a-z)", True)
    with col2:
        include_digits = st.checkbox("Digits (0-9)", True)
        include_special = st.checkbox(f"Special ({SPECIAL_CHARS})", True)
    
    if st.button("Generate Password", key="generate_btn"):
        try:
            pwd = generate_password(
                length=length,
                include_upper=include_upper,
                include_lower=include_lower,
                include_digits=include_digits,
                include_special=include_special
            )
            st.session_state.generated_pwd = pwd
            st.session_state.score, (st.session_state.strength, color) = check_password_strength(pwd)
        except ValueError as e:
            st.error(str(e))

# Main display
st.title("Password Generator")
if st.session_state.generated_pwd:
    st.code(st.session_state.generated_pwd, language="text")
    
    # Strength indicator
    progress = st.session_state.score / 5.0 if st.session_state.score > 0 else 0.0
    st.markdown(f"""
    <style>
        .stProgress > div > div > div {{
            background-color: {color};
        }}
    </style>
    """, unsafe_allow_html=True)
    st.progress(progress)
    st.subheader(f"Security Rating: {st.session_state.strength}")