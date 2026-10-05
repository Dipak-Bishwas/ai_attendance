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
            @import url('https://fonts.googleapis.com/css2?family=Titan+One&family=Fredoka:wght@600;700;800;900&family=Syne:wght@700;800;900&family=Inter:wght@400;500;600;700;800&family=Plus+Jakarta+Sans:wght@600;700;800;900&display=swap');

            /* Dashboard Lavender Background */
            .stApp {
                background: #ECE8FD !important;
                color: #09090B !important;
                min-height: 100vh !important;
            }

            /* Clear Streamlit column boxes on dashboard */
            .stApp div[data-testid="stColumn"] {
                background: transparent !important;
                border: none !important;
                box-shadow: none !important;
                padding: 0 !important;
            }

            /* Chunky Retro Titles */
            .snap-retro-title {
                font-family: 'Titan One', 'Fredoka', 'Syne', sans-serif !important;
                font-weight: 900 !important;
                letter-spacing: -0.03em !important;
                line-height: 0.95 !important;
                color: #09090B !important;
            }

            /* Top Welcome Text */
            .snap-welcome-text {
                font-family: 'Inter', -apple-system, sans-serif !important;
                font-size: 1.45rem !important;
                font-weight: 800 !important;
                color: #09090B !important;
                letter-spacing: -0.02em !important;
                line-height: 1.2 !important;
                text-align: right !important;
            }

            /* PRIMARY BUTTON: HOT PINK PILL (Logout, Create New Subject, Share Code, Enroll) */
            button[kind="primary"],
            button[data-testid="stBaseButton-primary"] {
                background: #EC4899 !important;
                background-color: #EC4899 !important;
                color: #FFFFFF !important;
                border: none !important;
                border-radius: 9999px !important;
                font-family: 'Inter', sans-serif !important;
                font-weight: 600 !important;
                font-size: 0.92rem !important;
                padding: 0.65rem 1.6rem !important;
                box-shadow: 0 4px 14px rgba(236, 72, 153, 0.3) !important;
                transition: all 0.2s ease !important;
            }

            button[kind="primary"]:hover,
            button[data-testid="stBaseButton-primary"]:hover {
                background: #DB2777 !important;
                background-color: #DB2777 !important;
                color: #FFFFFF !important;
                transform: translateY(-1px) !important;
                box-shadow: 0 6px 18px rgba(236, 72, 153, 0.4) !important;
            }

            button[kind="primary"]:active,
            button[data-testid="stBaseButton-primary"]:active {
                transform: translateY(1px) !important;
            }

            /* SECONDARY BUTTON: CRISP WHITE PILL WITH BORDER (Clear photos, Run Face Analysis) */
            button[kind="secondary"],
            button[data-testid="stBaseButton-secondary"] {
                background: #FFFFFF !important;
                background-color: #FFFFFF !important;
                color: #09090B !important;
                border: 1px solid #E2E8F0 !important;
                border-radius: 9999px !important;
                font-family: 'Inter', sans-serif !important;
                font-weight: 600 !important;
                font-size: 0.92rem !important;
                padding: 0.65rem 1.5rem !important;
                box-shadow: 0 1px 3px rgba(0, 0, 0, 0.04) !important;
                transition: all 0.2s ease !important;
            }

            button[kind="secondary"]:hover,
            button[data-testid="stBaseButton-secondary"]:hover {
                background: #F8FAFC !important;
                background-color: #F8FAFC !important;
                border-color: #CBD5E1 !important;
                color: #09090B !important;
                transform: translateY(-1px) !important;
            }

            /* TERTIARY BUTTON: SOLID BLACK PILL (Add Photos, Voice Attendance, Inactive Tabs) */
            button[kind="tertiary"],
            button[data-testid="stBaseButton-tertiary"] {
                background: #09090B !important;
                background-color: #09090B !important;
                color: #FFFFFF !important;
                border: none !important;
                border-radius: 9999px !important;
                font-family: 'Inter', sans-serif !important;
                font-weight: 600 !important;
                font-size: 0.92rem !important;
                padding: 0.65rem 1.5rem !important;
                box-shadow: 0 2px 8px rgba(0, 0, 0, 0.15) !important;
                transition: all 0.2s ease !important;
            }

            button[kind="tertiary"]:hover,
            button[data-testid="stBaseButton-tertiary"]:hover {
                background: #18181B !important;
                background-color: #18181B !important;
                color: #FFFFFF !important;
                transform: translateY(-1px) !important;
            }

            /* NAVIGATION TABS: ACTIVE TAB (Royal Blue Pill) */
            .snap-nav-tabs button[kind="primary"],
            .snap-nav-tabs [data-testid="stBaseButton-primary"] {
                background: #4F46E5 !important;
                background-color: #4F46E5 !important;
                color: #FFFFFF !important;
                border: none !important;
                border-radius: 9999px !important;
                font-family: 'Inter', sans-serif !important;
                font-weight: 700 !important;
                font-size: 0.92rem !important;
                padding: 0.65rem 1.5rem !important;
                box-shadow: 0 4px 14px rgba(79, 70, 229, 0.35) !important;
                transition: all 0.2s ease !important;
            }

            .snap-nav-tabs button[kind="primary"]:hover,
            .snap-nav-tabs [data-testid="stBaseButton-primary"]:hover {
                background: #4338CA !important;
                background-color: #4338CA !important;
                color: #FFFFFF !important;
                transform: translateY(-1px) !important;
            }

            /* NAVIGATION TABS: INACTIVE TAB (Solid Black Pill) */
            .snap-nav-tabs button[kind="tertiary"],
            .snap-nav-tabs button[kind="secondary"],
            .snap-nav-tabs [data-testid="stBaseButton-tertiary"],
            .snap-nav-tabs [data-testid="stBaseButton-secondary"] {
                background: #09090B !important;
                background-color: #09090B !important;
                color: #FFFFFF !important;
                border: none !important;
                border-radius: 9999px !important;
                font-family: 'Inter', sans-serif !important;
                font-weight: 600 !important;
                font-size: 0.92rem !important;
                padding: 0.65rem 1.5rem !important;
                box-shadow: 0 2px 8px rgba(0, 0, 0, 0.15) !important;
                transition: all 0.2s ease !important;
            }

            .snap-nav-tabs button[kind="tertiary"]:hover,
            .snap-nav-tabs button[kind="secondary"]:hover,
            .snap-nav-tabs [data-testid="stBaseButton-tertiary"]:hover,
            .snap-nav-tabs [data-testid="stBaseButton-secondary"]:hover {
                background: #18181B !important;
                background-color: #18181B !important;
                color: #FFFFFF !important;
                transform: translateY(-1px) !important;
            }

            /* Streamlit Inputs & Selectboxes */
            div[data-baseweb="select"] > div {
                background: #FFFFFF !important;
                border-radius: 0.75rem !important;
                border: 1px solid #E2E8F0 !important;
            }

            div[data-baseweb="input"] > div {
                background: #FFFFFF !important;
                border-radius: 0.75rem !important;
                border: 1px solid #E2E8F0 !important;
            }

            /* Divider styling */
            hr {
                border-color: rgba(147, 51, 234, 0.12) !important;
                margin: 1.5rem 0 !important;
            }

            /* Dialog styling */
            div[role="dialog"] {
                border-radius: 1.5rem !important;
                background: #FFFFFF !important;
                box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.25) !important;
            }
        </style>
    """, unsafe_allow_html=True)


def style_base_layout():
    st.markdown("""
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Titan+One&family=Fredoka:wght@600;700;800;900&family=Inter:wght@300;400;500;600;700;800&family=Plus+Jakarta+Sans:wght@500;600;700;800;900&family=Syne:wght@700;800;900&display=swap');

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
                border-radius: 9999px !important;
            }

            button[kind="tertiary"]:hover {
                background: #F4F4F5 !important;
                color: #09090B !important;
            }
        </style>
    """, unsafe_allow_html=True)