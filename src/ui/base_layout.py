import streamlit as st


def style_background_home():
    st.markdown("""
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@500;600;700;800;900&family=Syne:wght@700;800&family=Inter:wght@400;500;600;700&display=swap');

            /* Landing Page Background: Clean Crisp White with Soft Ambient Tint */
            .stApp {
                background: #FFFFFF !important;
                background-image: radial-gradient(at 50% -5%, rgba(79, 70, 229, 0.06) 0px, transparent 65%) !important;
                color: #09090B !important;
                min-height: 100vh !important;
            }

            /* Block container padding */
            .block-container {
                max-width: 1200px !important;
                padding-top: 1rem !important;
                padding-bottom: 2rem !important;
                padding-left: 1.5rem !important;
                padding-right: 1.5rem !important;
            }

            /* Typography */
            .snap-display-title {
                font-family: 'Syne', 'Plus Jakarta Sans', sans-serif !important;
                font-weight: 800 !important;
                letter-spacing: -0.04em !important;
                line-height: 1.05 !important;
            }

            /* Reset column styling on home screen to avoid clipping */
            .stApp div[data-testid="stColumn"] {
                background: transparent !important;
                border: none !important;
                box-shadow: none !important;
                padding: 0 !important;
            }
        </style>
    """, unsafe_allow_html=True)


def style_background_dashboard():
    st.markdown("""
        <style>
            .stApp {
                background: #FAFAFA !important;
                color: #09090B !important;
            }

            .stApp div[data-testid="stColumn"] {
                background: #FFFFFF !important;
                border: 1px solid #E4E4E7 !important;
                border-radius: 0.875rem !important;
                padding: 1.5rem !important;
                box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.04), 0 1px 2px -1px rgba(0, 0, 0, 0.03) !important;
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
            @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Plus+Jakarta+Sans:wght@500;600;700;800;900&family=Syne:wght@700;800&display=swap');

            /* Global Typography */
            html, body, [class*="css"] {
                font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif !important;
                letter-spacing: -0.011em;
                color: #09090B !important;
            }

            /* Hide Top Bar & Streamlit Header */
            #MainMenu, footer, header {
                visibility: hidden !important;
                height: 0 !important;
            }

            /* Hide Image Fullscreen & Element Toolbars */
            [data-testid="stElementToolbar"],
            button[title="View fullscreen"],
            [data-testid="StyledFullScreenButton"] {
                display: none !important;
                visibility: hidden !important;
                opacity: 0 !important;
                pointer-events: none !important;
            }

            /* Primary Button: Black Pill or Electric Blue */
            button[kind="primary"] {
                background: #09090B !important;
                color: #FFFFFF !important;
                border: 1px solid #09090B !important;
                border-radius: 9999px !important;
                font-family: 'Inter', sans-serif !important;
                font-weight: 600 !important;
                font-size: 0.92rem !important;
                padding: 0.65rem 1.6rem !important;
                box-shadow: 0 4px 14px rgba(0, 0, 0, 0.15) !important;
                transition: all 0.2s ease !important;
            }

            button[kind="primary"]:hover {
                background: #18181B !important;
                transform: translateY(-1px) !important;
                box-shadow: 0 8px 20px rgba(0, 0, 0, 0.2) !important;
            }

            button[kind="secondary"] {
                background: #FFFFFF !important;
                color: #18181B !important;
                border: 1px solid #E4E4E7 !important;
                border-radius: 9999px !important;
                font-family: 'Inter', sans-serif !important;
                font-weight: 600 !important;
                padding: 0.65rem 1.5rem !important;
                box-shadow: 0 1px 2px 0 rgba(0, 0, 0, 0.05) !important;
            }

            button[kind="secondary"]:hover {
                background: #F4F4F5 !important;
                border-color: #D4D4D8 !important;
            }

            button[kind="tertiary"] {
                background: transparent !important;
                color: #52525B !important;
                border: 1px solid #E4E4E7 !important;
                border-radius: 0.5rem !important;
            }

            button[kind="tertiary"]:hover {
                background: #F4F4F5 !important;
                color: #09090B !important;
            }
        </style>
    """, unsafe_allow_html=True)