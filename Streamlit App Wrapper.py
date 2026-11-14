import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="California Trip Planner & Checklist",
    page_icon="☀️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Remove default Streamlit padding/header so the planner fills the screen cleanly
st.markdown(
    """
    <style>
        .block-container { padding: 0 !important; max-width: 100% !important; }
        header[data-testid="stHeader"] { display: none; }
        footer { display: none; }
    </style>
    """,
    unsafe_allow_html=True
)

with open("california-trip-planner.html", "r", encoding="utf-8") as f:
    html_content = f.read()

components.html(html_content, height=2200, scrolling=True)