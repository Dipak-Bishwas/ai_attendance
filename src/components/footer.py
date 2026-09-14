import streamlit as st


def footer_home():
    st.markdown("""
        <div style="margin-top: 3.5rem; padding: 1.5rem 0 1rem 0; display: flex; flex-direction: column; align-items: center; justify-content: center;">
            <div style="font-size: 0.8rem; color: #64748B; letter-spacing: 0.02em;">
                SnapClass AI &copy; 2026 &bull; Intelligent Attendance Platform
            </div>
        </div>
    """, unsafe_allow_html=True)


def footer_dashboard():
    st.markdown("""
        <div style="margin-top: 3rem; padding: 1.5rem 0 1rem 0; border-top: 1px solid #E2E8F0; display: flex; flex-direction: column; align-items: center; justify-content: center;">
            <div style="font-size: 0.8rem; color: #94A3B8; letter-spacing: 0.02em;">
                SnapClass AI &copy; 2026 &bull; Encrypted Educational Record System
            </div>
        </div>
    """, unsafe_allow_html=True)
