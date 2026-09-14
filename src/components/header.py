import streamlit as st


def header_home():
    logo_url = "https://i.ibb.co/YTYGn5qV/logo.png"

    st.markdown(f"""
        <div style="display: flex; flex-direction: column; align-items: center; justify-content: center; text-align: center; margin-top: 1.5rem; margin-bottom: 2rem;">
            <div style="display: inline-flex; align-items: center; gap: 8px; background: rgba(99, 102, 241, 0.15); border: 1px solid rgba(129, 140, 248, 0.3); padding: 6px 16px; border-radius: 9999px; margin-bottom: 1.25rem;">
                <span style="display: inline-block; width: 8px; height: 8px; background: #34D399; border-radius: 50%; box-shadow: 0 0 10px #34D399;"></span>
                <span style="font-size: 0.82rem; font-weight: 600; color: #C7D2FE; letter-spacing: 0.05em; text-transform: uppercase;">Next-Gen Smart Attendance</span>
            </div>
            <div style="display: flex; align-items: center; justify-content: center; gap: 14px; margin-bottom: 0.75rem;">
                <img src='{logo_url}' style='height: 64px; width: 64px; object-fit: contain; filter: drop-shadow(0 8px 16px rgba(99, 102, 241, 0.3));' />
                <h1 style='margin: 0; font-size: 2.8rem; font-weight: 800; background: linear-gradient(135deg, #FFFFFF 0%, #C7D2FE 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; letter-spacing: -0.03em;'>
                    SnapClass
                </h1>
            </div>
            <p style='max-width: 580px; font-size: 1.1rem; color: #94A3B8; line-height: 1.6; margin: 0 auto 0.5rem auto;'>
                Automated classroom attendance powered by multi-face computer vision and speaker biometrics.
            </p>
        </div>
    """, unsafe_allow_html=True)


def header_dashboard():
    logo_url = "https://i.ibb.co/YTYGn5qV/logo.png"

    st.markdown(f"""
        <div style="display: flex; align-items: center; gap: 12px; padding: 0.5rem 0;">
            <img src='{logo_url}' style='height: 44px; width: 44px; object-fit: contain; filter: drop-shadow(0 4px 10px rgba(79, 70, 229, 0.2));' />
            <div>
                <h2 style='margin: 0; font-size: 1.6rem; font-weight: 700; color: #0F172A; letter-spacing: -0.02em;'>
                    SnapClass
                </h2>
                <div style="display: flex; align-items: center; gap: 6px;">
                    <span style="display: inline-block; width: 6px; height: 6px; background: #10B981; border-radius: 50%;"></span>
                    <span style="font-size: 0.75rem; font-weight: 500; color: #64748B;">AI Engine Active</span>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)
