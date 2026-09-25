import streamlit as st
from src.components.header import header_home
from src.components.footer import footer_home
from src.ui.base_layout import style_base_layout, style_background_home


def home_screen():
    style_background_home()
    style_base_layout()
    header_home()

    # Quick Metric Pill Strip (Modern Minimal Light)
    st.markdown("""
        <div style="display: flex; justify-content: center; gap: 10px; flex-wrap: wrap; margin-bottom: 2.25rem;">
            <div style="background: #FFFFFF; border: 1px solid #E4E4E7; padding: 5px 14px; border-radius: 9999px; font-size: 0.8rem; color: #18181B; display: inline-flex; align-items: center; gap: 6px; box-shadow: 0 1px 2px 0 rgba(0, 0, 0, 0.03);">
                <span style="color: #2563EB;">⚡</span> <strong>&lt; 1s</strong> Scan Speed
            </div>
            <div style="background: #FFFFFF; border: 1px solid #E4E4E7; padding: 5px 14px; border-radius: 9999px; font-size: 0.8rem; color: #18181B; display: inline-flex; align-items: center; gap: 6px; box-shadow: 0 1px 2px 0 rgba(0, 0, 0, 0.03);">
                <span style="color: #10B981;">🎯</span> <strong>99.8%</strong> Precision
            </div>
            <div style="background: #FFFFFF; border: 1px solid #E4E4E7; padding: 5px 14px; border-radius: 9999px; font-size: 0.8rem; color: #18181B; display: inline-flex; align-items: center; gap: 6px; box-shadow: 0 1px 2px 0 rgba(0, 0, 0, 0.03);">
                <span style="color: #8B5CF6;">🎙️</span> <strong>256-d</strong> Voice Embeddings
            </div>
            <div style="background: #FFFFFF; border: 1px solid #E4E4E7; padding: 5px 14px; border-radius: 9999px; font-size: 0.8rem; color: #18181B; display: inline-flex; align-items: center; gap: 6px; box-shadow: 0 1px 2px 0 rgba(0, 0, 0, 0.03);">
                <span style="color: #0EA5E9;">☁️</span> <strong>Real-time</strong> Cloud Sync
            </div>
        </div>
    """, unsafe_allow_html=True)

    # Portal Selection Cards
    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.markdown("""
            <div>
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.75rem;">
                    <span style="background: #EFF6FF; color: #1D4ED8; border: 1px solid #DBEAFE; font-size: 0.72rem; font-weight: 600; padding: 3px 9px; border-radius: 6px; letter-spacing: 0.04em; text-transform: uppercase;">
                        Student Access
                    </span>
                    <span style="color: #71717A; font-size: 0.78rem; font-weight: 500;">Face ID &bull; Rosters</span>
                </div>
                <h2 style="color: #09090B; font-size: 1.55rem; margin: 0 0 0.4rem 0; font-weight: 700;">
                    Student Portal
                </h2>
                <p style="color: #52525B; font-size: 0.88rem; line-height: 1.5; margin: 0 0 1.25rem 0;">
                    Authenticate with 1-click Face ID, view real-time subject attendance rates, and enroll with join codes.
                </p>
                <div style="background: #F8FAFC; border: 1px solid #E2E8F0; padding: 12px 14px; border-radius: 8px; margin-bottom: 1.25rem;">
                    <div style="font-size: 0.8rem; color: #334155; margin-bottom: 4px;">&bull; <strong>Instant Face Verification</strong></div>
                    <div style="font-size: 0.8rem; color: #334155; margin-bottom: 4px;">&bull; <strong>Live Course Attendance Stats</strong></div>
                    <div style="font-size: 0.8rem; color: #334155;">&bull; <strong>Auto-Enroll Via QR / Codes</strong></div>
                </div>
            </div>
        """, unsafe_allow_html=True)

        center_c1, center_c2, center_c3 = st.columns([1, 2, 1])
        with center_c2:
            st.image("https://i.ibb.co/844D9Lrt/mascot-student.png", width=120)

        st.markdown("<div style='margin-top: 1.25rem;'></div>", unsafe_allow_html=True)
        if st.button('Enter Student Portal', type='primary', icon=':material/arrow_outward:', key='btn_student_portal', use_container_width=True):
            st.session_state['login_type'] = 'student'
            st.rerun()

    with col2:
        st.markdown("""
            <div>
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.75rem;">
                    <span style="background: #F5F3FF; color: #6D28D9; border: 1px solid #DDD6FE; font-size: 0.72rem; font-weight: 600; padding: 3px 9px; border-radius: 6px; letter-spacing: 0.04em; text-transform: uppercase;">
                        Educator Suite
                    </span>
                    <span style="color: #71717A; font-size: 0.78rem; font-weight: 500;">Multi-Face &bull; Voice AI</span>
                </div>
                <h2 style="color: #09090B; font-size: 1.55rem; margin: 0 0 0.4rem 0; font-weight: 700;">
                    Teacher Portal
                </h2>
                <p style="color: #52525B; font-size: 0.88rem; line-height: 1.5; margin: 0 0 1.25rem 0;">
                    Perform simultaneous multi-face classroom recognition, run bulk voice roll calls, and export logs.
                </p>
                <div style="background: #F8FAFC; border: 1px solid #E2E8F0; padding: 12px 14px; border-radius: 8px; margin-bottom: 1.25rem;">
                    <div style="font-size: 0.8rem; color: #334155; margin-bottom: 4px;">&bull; <strong>Simultaneous Multi-Face Scan</strong></div>
                    <div style="font-size: 0.8rem; color: #334155; margin-bottom: 4px;">&bull; <strong>Audio Speaker Biometrics</strong></div>
                    <div style="font-size: 0.8rem; color: #334155;">&bull; <strong>Automated Roster & Export</strong></div>
                </div>
            </div>
        """, unsafe_allow_html=True)

        center_c1, center_c2, center_c3 = st.columns([1, 2, 1])
        with center_c2:
            st.image("https://i.ibb.co/CsmQQV6X/mascot-prof.png", width=135)

        st.markdown("<div style='margin-top: 1.25rem;'></div>", unsafe_allow_html=True)
        if st.button('Enter Teacher Portal', type='primary', icon=':material/arrow_outward:', key='btn_teacher_portal', use_container_width=True):
            st.session_state['login_type'] = 'teacher'
            st.rerun()

    # How It Works (3 Steps)
    st.markdown("""
        <div style="margin-top: 4rem; text-align: center;">
            <span style="font-size: 0.78rem; font-weight: 600; color: #2563EB; letter-spacing: 0.06em; text-transform: uppercase;">
                Effortless Workflow
            </span>
            <h2 style="color: #09090B; font-size: 1.85rem; margin: 0.35rem 0 1.75rem 0; font-weight: 700;">
                How SnapClass Works
            </h2>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 1.25rem; text-align: left;">
                <div style="background: #FFFFFF; border: 1px solid #E4E4E7; padding: 1.35rem; border-radius: 0.75rem; box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.03);">
                    <div style="background: #EFF6FF; width: 32px; height: 32px; border-radius: 6px; display: flex; align-items: center; justify-content: center; font-weight: 700; color: #1D4ED8; margin-bottom: 0.75rem; font-size: 0.9rem;">1</div>
                    <div style="color: #09090B; font-weight: 600; font-size: 1rem; margin-bottom: 0.35rem;">Enroll Face & Voice</div>
                    <p style="color: #52525B; font-size: 0.85rem; line-height: 1.5; margin: 0;">Students take a single selfie and record a short phrase. Neural embeddings are safely stored.</p>
                </div>
                <div style="background: #FFFFFF; border: 1px solid #E4E4E7; padding: 1.35rem; border-radius: 0.75rem; box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.03);">
                    <div style="background: #F5F3FF; width: 32px; height: 32px; border-radius: 6px; display: flex; align-items: center; justify-content: center; font-weight: 700; color: #6D28D9; margin-bottom: 0.75rem; font-size: 0.9rem;">2</div>
                    <div style="color: #09090B; font-weight: 600; font-size: 1rem; margin-bottom: 0.35rem;">Snap or Record Class</div>
                    <p style="color: #52525B; font-size: 0.85rem; line-height: 1.5; margin: 0;">The teacher snaps photos of the classroom or records audio of students responding.</p>
                </div>
                <div style="background: #FFFFFF; border: 1px solid #E4E4E7; padding: 1.35rem; border-radius: 0.75rem; box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.03);">
                    <div style="background: #ECFDF5; width: 32px; height: 32px; border-radius: 6px; display: flex; align-items: center; justify-content: center; font-weight: 700; color: #047857; margin-bottom: 0.75rem; font-size: 0.9rem;">3</div>
                    <div style="color: #09090B; font-weight: 600; font-size: 1rem; margin-bottom: 0.35rem;">Instant Verified Logs</div>
                    <p style="color: #52525B; font-size: 0.85rem; line-height: 1.5; margin: 0;">AI simultaneously detects and verifies all attendees, saving logs directly to cloud database.</p>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # Feature Capabilities Bento Grid
    st.markdown("""
        <div style="margin-top: 4rem; padding-top: 2rem; border-top: 1px solid #E4E4E7;">
            <div style="text-align: center; margin-bottom: 1.75rem;">
                <span style="font-size: 0.78rem; font-weight: 600; color: #2563EB; letter-spacing: 0.06em; text-transform: uppercase;">Enterprise Features</span>
                <h2 style="color: #09090B; font-size: 1.85rem; margin: 0.35rem 0 0 0; font-weight: 700;">Cutting-Edge AI Architecture</h2>
            </div>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 1rem;">
                <div style="background: #FFFFFF; border: 1px solid #E4E4E7; padding: 1.35rem; border-radius: 0.75rem; box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.03);">
                    <div style="font-size: 1.5rem; margin-bottom: 0.5rem;">👁️</div>
                    <div style="color: #09090B; font-weight: 600; font-size: 0.95rem; margin-bottom: 0.35rem;">Multi-Face Vision</div>
                    <div style="color: #71717A; font-size: 0.82rem; line-height: 1.5;">68-point facial landmark pose estimation with 128-d deep metric embeddings & SVM classification.</div>
                </div>
                <div style="background: #FFFFFF; border: 1px solid #E4E4E7; padding: 1.35rem; border-radius: 0.75rem; box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.03);">
                    <div style="font-size: 1.5rem; margin-bottom: 0.5rem;">🎙️</div>
                    <div style="color: #09090B; font-weight: 600; font-size: 0.95rem; margin-bottom: 0.35rem;">Speaker Biometrics</div>
                    <div style="color: #71717A; font-size: 0.82rem; line-height: 1.5;">Resemblyzer deep voice encoder with silence splitting to isolate individual student voices.</div>
                </div>
                <div style="background: #FFFFFF; border: 1px solid #E4E4E7; padding: 1.35rem; border-radius: 0.75rem; box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.03);">
                    <div style="font-size: 1.5rem; margin-bottom: 0.5rem;">📱</div>
                    <div style="color: #09090B; font-weight: 600; font-size: 0.95rem; margin-bottom: 0.35rem;">Responsive Everywhere</div>
                    <div style="color: #71717A; font-size: 0.82rem; line-height: 1.5;">Optimized for mobile phones, iPads, laptops, and smart classroom display boards.</div>
                </div>
                <div style="background: #FFFFFF; border: 1px solid #E4E4E7; padding: 1.35rem; border-radius: 0.75rem; box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.03);">
                    <div style="font-size: 1.5rem; margin-bottom: 0.5rem;">🔒</div>
                    <div style="color: #09090B; font-weight: 600; font-size: 0.95rem; margin-bottom: 0.35rem;">Supabase Security</div>
                    <div style="color: #71717A; font-size: 0.82rem; line-height: 1.5;">Encrypted bcrypt passwords, PostgreSQL relational joins, and secure JWT authentication.</div>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    footer_home()