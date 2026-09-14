import streamlit as st


def style_background_home():
    st.markdown("""
        <style>
            .stApp {
                background: linear-gradient(135deg, #0F172A 0%, #1E1B4B 50%, #0F172A 100%) !important;
                color: #F8FAFC !important;
            }

            /* Portal Selection Cards on Landing Page */
            .stApp div[data-testid="stColumn"] {
                background: rgba(255, 255, 255, 0.05) !important;
                backdrop-filter: blur(16px) !important;
                -webkit-backdrop-filter: blur(16px) !important;
                border: 1px solid rgba(255, 255, 255, 0.12) !important;
                padding: 2.2rem 2rem !important;
                border-radius: 1.5rem !important;
                box-shadow: 0 20px 40px -15px rgba(0, 0, 0, 0.4) !important;
                transition: transform 0.3s ease, border-color 0.3s ease, box-shadow 0.3s ease !important;
                display: flex !important;
                flex-direction: column !important;
                justify-content: space-between !important;
            }

            .stApp div[data-testid="stColumn"]:hover {
                transform: translateY(-4px) !important;
                border-color: rgba(99, 102, 241, 0.5) !important;
                box-shadow: 0 25px 50px -12px rgba(79, 70, 229, 0.25) !important;
            }

            /* Responsive tweaks for mobile */
            @media (max-width: 768px) {
                .stApp div[data-testid="stColumn"] {
                    padding: 1.5rem 1.25rem !important;
                    margin-bottom: 1.25rem !important;
                    border-radius: 1.25rem !important;
                }
            }
        </style>
    """, unsafe_allow_html=True)


def style_background_dashboard():
    st.markdown("""
        <style>
            .stApp {
                background: #F8FAFC !important;
                color: #0F172A !important;
            }

            .stApp div[data-testid="stColumn"] {
                background: #FFFFFF !important;
                border: 1px solid #E2E8F0 !important;
                border-radius: 1.25rem !important;
                padding: 1.75rem !important;
                box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.04), 0 2px 4px -2px rgba(0, 0, 0, 0.04) !important;
            }

            @media (max-width: 768px) {
                .stApp div[data-testid="stColumn"] {
                    padding: 1.25rem !important;
                    margin-bottom: 1rem !important;
                }
            }
        </style>
    """, unsafe_allow_html=True)


def style_base_layout():
    st.markdown("""
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=Space+Grotesk:wght@600;700&display=swap');

            /* Global Typography */
            html, body, [class*="css"] {
                font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif !important;
                letter-spacing: -0.01em;
            }

            /* Hide top bar & Streamlit branding */
            #MainMenu, footer, header {
                visibility: hidden !important;
                height: 0 !important;
            }

            /* Hide image fullscreen & element toolbar hover buttons */
            [data-testid="stElementToolbar"],
            button[title="View fullscreen"],
            [data-testid="StyledFullScreenButton"] {
                display: none !important;
                visibility: hidden !important;
                opacity: 0 !important;
                pointer-events: none !important;
            }

            /* Main Container Padding */
            .block-container {
                max-width: 1120px !important;
                padding-top: 2rem !important;
                padding-bottom: 3rem !important;
                padding-left: 1.5rem !important;
                padding-right: 1.5rem !important;
            }

            /* Headings */
            h1 {
                font-family: 'Space Grotesk', 'Plus Jakarta Sans', sans-serif !important;
                font-weight: 700 !important;
                letter-spacing: -0.03em !important;
                line-height: 1.15 !important;
            }

            h2, h3 {
                font-family: 'Space Grotesk', 'Plus Jakarta Sans', sans-serif !important;
                font-weight: 600 !important;
                letter-spacing: -0.02em !important;
            }

            p, label, span {
                font-family: 'Plus Jakarta Sans', sans-serif !important;
            }

            /* Modern Button Design System */
            button {
                font-family: 'Plus Jakarta Sans', sans-serif !important;
                font-weight: 600 !important;
                font-size: 0.95rem !important;
                border-radius: 0.85rem !important;
                padding: 0.7rem 1.4rem !important;
                border: 1px solid transparent !important;
                transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1) !important;
                cursor: pointer !important;
                box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05) !important;
            }

            button[kind="primary"] {
                background: linear-gradient(135deg, #4F46E5 0%, #6366F1 100%) !important;
                color: #FFFFFF !important;
                border: 1px solid rgba(255, 255, 255, 0.15) !important;
                box-shadow: 0 4px 14px rgba(79, 70, 229, 0.35) !important;
            }

            button[kind="primary"]:hover {
                transform: translateY(-2px) !important;
                box-shadow: 0 6px 20px rgba(79, 70, 229, 0.45) !important;
                background: linear-gradient(135deg, #4338CA 0%, #4F46E5 100%) !important;
            }

            button[kind="secondary"] {
                background: rgba(241, 245, 249, 0.9) !important;
                color: #334155 !important;
                border: 1px solid #CBD5E1 !important;
            }

            button[kind="secondary"]:hover {
                background: #E2E8F0 !important;
                color: #0F172A !important;
                transform: translateY(-1px) !important;
            }

            button[kind="tertiary"] {
                background: transparent !important;
                color: #64748B !important;
                border: 1px solid #E2E8F0 !important;
            }

            button[kind="tertiary"]:hover {
                background: #F1F5F9 !important;
                color: #0F172A !important;
            }

            /* Responsive adjustments for phones & small tablets */
            @media (max-width: 768px) {
                .block-container {
                    padding-top: 1rem !important;
                    padding-left: 1rem !important;
                    padding-right: 1rem !important;
                }
                h1 {
                    font-size: 2rem !important;
                }
                h2 {
                    font-size: 1.5rem !important;
                }
                button {
                    width: 100% !important;
                }
            }
        </style>
    """, unsafe_allow_html=True)