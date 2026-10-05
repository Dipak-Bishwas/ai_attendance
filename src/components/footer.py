import textwrap
import streamlit as st


def footer_home():
    st.markdown(textwrap.dedent("""
        <div style="margin-top: 3.5rem; padding: 1.5rem 0 1rem 0; display: flex; flex-direction: column; align-items: center; justify-content: center; border-top: 1px solid #E4E4E7;">
            <div style="font-size: 0.78rem; color: #71717A; letter-spacing: 0.02em;">
                SnapClass AI &copy; 2026 &bull; Intelligent Attendance Platform
            </div>
        </div>
    """).strip(), unsafe_allow_html=True)


def footer_dashboard():
    st.markdown(textwrap.dedent("""
        <div style="margin-top: 3rem; padding: 1.5rem 0 1rem 0; border-top: 1px solid #E4E4E7; display: flex; flex-direction: column; align-items: center; justify-content: center;">
            <div style="font-size: 0.78rem; color: #A1A1AA; letter-spacing: 0.02em;">
                SnapClass AI &copy; 2026 &bull; Encrypted Educational Record System
            </div>
        </div>
    """).strip(), unsafe_allow_html=True)

