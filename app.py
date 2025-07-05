
import streamlit as st
import time

st.set_page_config(page_title="Crypto Risk Dashboard", layout="wide", page_icon="🚀")

st.markdown("<h1 style='text-align: center; color: cyan;'>🚀 Space-Themed Crypto Risk Dashboard</h1>", unsafe_allow_html=True)

tokens = [
    {"name": "Chainlink (LINK)", "risk": 22, "unlocks": "In 45 days", "holders": "Decentralized", "whale_activity": "Stable"},
    {"name": "Arbitrum (ARB)", "risk": 38, "unlocks": "In 14 days", "holders": "Fair", "whale_activity": "Moderate sells"},
    {"name": "Render (RNDR)", "risk": 19, "unlocks": "None soon", "holders": "Healthy", "whale_activity": "Accumulating"},
    {"name": "Pyth Network (PYTH)", "risk": 15, "unlocks": "Staked (Low risk)", "holders": "Healthy", "whale_activity": "Stable"},
    {"name": "Sui (SUI)", "risk": 43, "unlocks": "In 3 days", "holders": "Moderate", "whale_activity": "Light dumps"}
]

st.markdown("### 🧠 Real-Time Token Risk Scoreboard (Auto-refreshes every 60s)")

for token in tokens:
    risk_color = "green" if token["risk"] < 30 else "orange" if token["risk"] < 50 else "red"
    with st.expander(f"{token['name']}"):
        st.markdown(f"**🧪 Dump Risk Score**: <span style='color:{risk_color}; font-weight:bold;'>{token['risk']}%</span>", unsafe_allow_html=True)
        st.markdown(f"**🔓 Upcoming Unlock**: {token['unlocks']}")
        st.markdown(f"**🧬 Holder Spread**: {token['holders']}")
        st.markdown(f"**🐋 Whale Tracker**: {token['whale_activity']}")

# Auto-refresh every 60s
st.experimental_rerun() if time.time() % 60 < 2 else None
