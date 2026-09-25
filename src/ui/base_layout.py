import streamlit as st


def style_background_home():
    st.markdown("""
        <style>
            /* Landing Page Background: 21st.dev Modern Minimal Light Aesthetic */
            .stApp {
                background: #FAFAFA !important;
                background-image: radial-gradient(at 50% 0%, rgba(37, 99, 235, 0.05) 0px, transparent 60%) !important;
                color: #09090B !important;
                min-height: 100vh !important;
            }

            /* Portal Selection Columns / Cards */
            .stApp div[data-testid="stColumn"] {
                background: #FFFFFF !important;
                border: 1px solid #E4E4E7 !important;
                padding: 2rem 1.75rem !important;
                border-radius: 0.875rem !important;
                box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.04), 0 1px 2px -1px rgba(0, 0, 0, 0.03) !important;
                transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1) !important;
                display: flex !important;
                flex-direction: column !important;
                justify-content: space-between !important;
            }

            .stApp div[data-testid="stColumn"]:hover {
                transform: translateY(-3px) !important;
                border-color: #93C5FD !important;
                box-shadow: 0 10px 25px -5px rgba(37, 99, 235, 0.12), 0 8px 10px -6px rgba(37, 99, 235, 0.06) !important;
            }

            /* Responsive Adjustments for Mobile & Tablets */
            @media (max-width: 768px) {
                .stApp div[data-testid="stColumn"] {
                    padding: 1.5rem 1.25rem !important;
                    margin-bottom: 1.25rem !important;
                    border-radius: 0.75rem !important;
                }
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
            @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Plus+Jakarta+Sans:wght@500;600;700;800&display=swap');

            /* Global Modern Minimal Typography */
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

            /* Max Width Container */
            .block-container {
                max-width: 1120px !important;
                padding-top: 1.5rem !important;
                padding-bottom: 3.5rem !important;
                padding-left: 1.5rem !important;
                padding-right: 1.5rem !important;
            }

            /* Typography Hierarchy */
            h1 {
                font-family: 'Plus Jakarta Sans', 'Inter', sans-serif !important;
                font-weight: 700 !important;
                letter-spacing: -0.025em !important;
                line-height: 1.15 !important;
                color: #09090B !important;
            }

            h2, h3 {
                font-family: 'Plus Jakarta Sans', 'Inter', sans-serif !important;
                font-weight: 600 !important;
                letter-spacing: -0.02em !important;
                color: #09090B !important;
            }

            /* Button Design System: 21st.dev Modern Minimal */
            button {
                font-family: 'Inter', sans-serif !important;
                font-weight: 500 !important;
                font-size: 0.9rem !important;
                border-radius: 0.5rem !important;
                padding: 0.6rem 1.25rem !important;
                min-height: 42px !important;
                transition: all 0.15s ease-in-out !important;
                cursor: pointer !important;
            }

            button[kind="primary"] {
                background: #2563EB !important;
                color: #FFFFFF !important;
                border: 1px solid #1D4ED8 !important;
                box-shadow: 0 1px 2px 0 rgba(0, 0, 0, 0.05) !important;
            }

            button[kind="primary"]:hover {
                background: #1D4ED8 !important;
                border-color: #1E40AF !important;
                transform: translateY(-1px) !important;
                box-shadow: 0 4px 12px rgba(37, 99, 235, 0.25) !important;
            }

            button[kind="primary"]:active {
                background: #1E40AF !important;
                transform: translateY(0px) !important;
            }

            button[kind="secondary"] {
                background: #FFFFFF !important;
                color: #18181B !important;
                border: 1px solid #E4E4E7 !important;
                box-shadow: 0 1px 2px 0 rgba(0, 0, 0, 0.05) !important;
            }

            button[kind="secondary"]:hover {
                background: #F4F4F5 !important;
                color: #09090B !important;
                border-color: #D4D4D8 !important;
            }

            button[kind="tertiary"] {
                background: transparent !important;
                color: #52525B !important;
                border: 1px solid #E4E4E7 !important;
            }

            button[kind="tertiary"]:hover {
                background: #F4F4F5 !important;
                color: #09090B !important;
                border-color: #D4D4D8 !important;
            }

            /* Streamlit Inputs & Selectboxes */
            div[data-baseweb="input"], div[data-baseweb="select"] {
                border-radius: 0.5rem !important;
            }

            input, select, textarea {
                border-radius: 0.5rem !important;
                font-family: 'Inter', sans-serif !important;
            }

            /* Streamlit Dialog / Modals */
            div[data-testid="stDialog"] div[role="dialog"] {
                border-radius: 0.875rem !important;
                border: 1px solid #E4E4E7 !important;
                box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04) !important;
            }

            /* Dividers */
            hr {
                border-color: #E4E4E7 !important;
                opacity: 0.8 !important;
                margin: 1.5rem 0 !important;
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
                    font-size: 1.4rem !important;
                }
                button {
                    width: 100% !important;
                }
            }
        </style>
    """, unsafe_allow_html=True)