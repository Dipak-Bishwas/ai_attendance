import streamlit as st
from src.components.header import header_home
from src.components.footer import footer_home
from src.ui.base_layout import style_base_layout, style_background_home


def home_screen():
    style_background_home()
    style_base_layout()
    header_home()

    # Portal Selection Cards
    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.markdown("""
            <div style="margin-bottom: 0.75rem;">
                <span style="display: inline-block; background: rgba(59, 130, 246, 0.15); color: #93C5FD; font-size: 0.75rem; font-weight: 700; padding: 4px 10px; border-radius: 6px; letter-spacing: 0.05em; text-transform: uppercase;">
                    Student Access
                </span>
                <h2 style="color: #FFFFFF; font-size: 1.65rem; margin: 0.5rem 0 0.25rem 0; font-weight: 700;">
                    Student Portal
                </h2>
                <p style="color: #94A3B8; font-size: 0.92rem; line-height: 1.5; margin: 0 0 1rem 0;">
                    Check in with Face ID, track attendance percentages, and enroll in your courses.
                </p>
            </div>
        """, unsafe_allow_html=True)

        center_col1, center_col2, center_col3 = st.columns([1, 2, 1])
        with center_col2:
            st.image("https://i.ibb.co/844D9Lrt/mascot-student.png", width=120)

        st.markdown("<div style='margin-top: 1rem;'></div>", unsafe_allow_html=True)
        if st.button('Enter Student Portal', type='primary', icon=':material/arrow_outward:', key='btn_student_portal'):
            st.session_state['login_type'] = 'student'
            st.rerun()

    with col2:
        st.markdown("""
            <div style="margin-bottom: 0.75rem;">
                <span style="display: inline-block; background: rgba(168, 85, 247, 0.15); color: #D8B4FE; font-size: 0.75rem; font-weight: 700; padding: 4px 10px; border-radius: 6px; letter-spacing: 0.05em; text-transform: uppercase;">
                    Educator Suite
                </span>
                <h2 style="color: #FFFFFF; font-size: 1.65rem; margin: 0.5rem 0 0.25rem 0; font-weight: 700;">
                    Teacher Portal
                </h2>
                <p style="color: #94A3B8; font-size: 0.92rem; line-height: 1.5; margin: 0 0 1rem 0;">
                    Conduct multi-face classroom scans, run voice attendance, and manage subject records.
                </p>
            </div>
        """, unsafe_allow_html=True)

        center_col1, center_col2, center_col3 = st.columns([1, 2, 1])
        with center_col2:
            st.image("https://i.ibb.co/CsmQQV6X/mascot-prof.png", width=135)

        st.markdown("<div style='margin-top: 1rem;'></div>", unsafe_allow_html=True)
        if st.button('Enter Teacher Portal', type='primary', icon=':material/arrow_outward:', key='btn_teacher_portal'):
            st.session_state['login_type'] = 'teacher'
            st.rerun()

    # Feature Highlights Grid
    st.markdown("""
        <div style="margin-top: 3.5rem; padding-top: 2rem; border-top: 1px solid rgba(255, 255, 255, 0.08);">
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 1.5rem; text-align: left;">
                <div style="background: rgba(255, 255, 255, 0.02); border: 1px solid rgba(255, 255, 255, 0.06); padding: 1.25rem; border-radius: 1rem;">
                    <div style="font-size: 1.5rem; margin-bottom: 0.5rem;">⚡</div>
                    <div style="color: #FFFFFF; font-weight: 600; font-size: 0.95rem; margin-bottom: 0.25rem;">Multi-Face Vision</div>
                    <div style="color: #64748B; font-size: 0.85rem; line-height: 1.4;">Scans entire classroom photos simultaneously with sub-second biometric verification.</div>
                </div>
                <div style="background: rgba(255, 255, 255, 0.02); border: 1px solid rgba(255, 255, 255, 0.06); padding: 1.25rem; border-radius: 1rem;">
                    <div style="font-size: 1.5rem; margin-bottom: 0.5rem;">🎙️</div>
                    <div style="color: #FFFFFF; font-weight: 600; font-size: 0.95rem; margin-bottom: 0.25rem;">Voice Recognition</div>
                    <div style="color: #64748B; font-size: 0.85rem; line-height: 1.4;">Deep speaker embeddings isolate and identify students by natural voice recordings.</div>
                </div>
                <div style="background: rgba(255, 255, 255, 0.02); border: 1px solid rgba(255, 255, 255, 0.06); padding: 1.25rem; border-radius: 1rem;">
                    <div style="font-size: 1.5rem; margin-bottom: 0.5rem;">☁️</div>
                    <div style="color: #FFFFFF; font-weight: 600; font-size: 0.95rem; margin-bottom: 0.25rem;">Cloud Database</div>
                    <div style="color: #64748B; font-size: 0.85rem; line-height: 1.4;">Synchronized in real time with enterprise PostgreSQL and encrypted access tokens.</div>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    footer_home()