import streamlit as st


def footer_home():
    logo_url = "https://i.ibb.co/4r5X1FY/apnacollege.png"

    st.markdown(f"""
        <div style="margin-top: 3.5rem; padding: 1.5rem 0 1rem 0; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 8px;">
            <div style="display: flex; align-items: center; gap: 8px;">
                <span style="font-size: 0.85rem; font-weight: 500; color: #64748B;">Created with ❤️ by</span>
                <img src='{logo_url}' style='height: 20px; object-fit: contain;' />
            </div>
            <div style="font-size: 0.75rem; color: #475569;">
                SnapClass AI &copy; 2026 • Intelligent Attendance Platform
            </div>
        </div>
    """, unsafe_allow_html=True)


def footer_dashboard():
    logo_url = "https://i.ibb.co/4r5X1FY/apnacollege.png"

    st.markdown(f"""
        <div style="margin-top: 3rem; padding: 1.5rem 0 1rem 0; border-top: 1px solid #E2E8F0; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 6px;">
            <div style="display: flex; align-items: center; gap: 8px;">
                <span style="font-size: 0.85rem; font-weight: 500; color: #64748B;">Created with ❤️ by</span>
                <img src='{logo_url}' style='height: 20px; object-fit: contain;' />
            </div>
            <div style="font-size: 0.75rem; color: #94A3B8;">
                SnapClass AI &copy; 2026 • Encrypted Educational Record System
            </div>
        </div>
    """, unsafe_allow_html=True)
