import textwrap
import streamlit as st


def header_home():
    logo_url = "https://i.ibb.co/YTYGn5qV/logo.png"

    st.markdown(textwrap.dedent(f"""
        <div style="display: flex; flex-direction: column; align-items: center; justify-content: center; text-align: center; margin-top: 1rem; margin-bottom: 2rem;">
            <div style="display: inline-flex; align-items: center; gap: 8px; background: #EFF6FF; border: 1px solid #DBEAFE; padding: 5px 14px; border-radius: 9999px; margin-bottom: 1.25rem;">
                <span style="display: inline-block; width: 7px; height: 7px; background: #2563EB; border-radius: 50%;"></span>
                <span style="font-size: 0.78rem; font-weight: 600; color: #1D4ED8; letter-spacing: 0.04em; text-transform: uppercase;">Smart AI Attendance System</span>
            </div>
            <div style="display: flex; align-items: center; justify-content: center; gap: 14px; margin-bottom: 0.75rem;">
                <img src='{logo_url}' style='height: 56px; width: 56px; object-fit: contain; filter: drop-shadow(0 2px 8px rgba(37, 99, 235, 0.15));' />
                <h1 style='margin: 0; font-size: 2.6rem; font-weight: 800; color: #09090B; letter-spacing: -0.03em;'>
                    SnapClass
                </h1>
            </div>
            <p style='max-width: 540px; font-size: 1.05rem; color: #52525B; line-height: 1.55; margin: 0 auto 0.5rem auto;'>
                Automated classroom attendance powered by multi-face computer vision and voice biometrics.
            </p>
        </div>
    """).strip(), unsafe_allow_html=True)


def header_dashboard():
    logo_url = "https://i.ibb.co/YTYGn5qV/logo.png"

    st.markdown(textwrap.dedent(f"""
        <div style="display: flex; align-items: center; gap: 14px; padding: 0.25rem 0;">
            <img src='{logo_url}' style='height: 64px; width: 64px; object-fit: contain; filter: drop-shadow(0 2px 8px rgba(0, 0, 0, 0.08));' />
            <div style="font-family: 'Titan One', 'Fredoka', 'Syne', sans-serif; font-size: 1.85rem; font-weight: 900; line-height: 0.92; color: #5363F3; letter-spacing: -0.02em; text-transform: uppercase;">
                SNAP<br/>CLASS
            </div>
        </div>
    """).strip(), unsafe_allow_html=True)

