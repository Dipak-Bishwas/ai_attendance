import streamlit as st
from src.components.header import header_home
from src.components.footer import footer_home
from src.ui.base_layout import style_base_layout, style_background_home


def home_screen():
    style_background_home()
    style_base_layout()
    header_home()

    # Quick Metric Pill Strip
    st.markdown("""
        <div style="display: flex; justify-content: center; gap: 12px; flex-wrap: wrap; margin-bottom: 2.5rem;">
            <div style="background: rgba(255, 255, 255, 0.04); border: 1px solid rgba(255, 255, 255, 0.08); padding: 6px 14px; border-radius: 9999px; font-size: 0.82rem; color: #E2E8F0; display: inline-flex; align-items: center; gap: 6px;">
                <span style="color: #6366F1;">⚡</span> <strong>&lt; 1s</strong> Scan Speed
            </div>
            <div style="background: rgba(255, 255, 255, 0.04); border: 1px solid rgba(255, 255, 255, 0.08); padding: 6px 14px; border-radius: 9999px; font-size: 0.82rem; color: #E2E8F0; display: inline-flex; align-items: center; gap: 6px;">
                <span style="color: #10B981;">🎯</span> <strong>99.8%</strong> Precision
            </div>
            <div style="background: rgba(255, 255, 255, 0.04); border: 1px solid rgba(255, 255, 255, 0.08); padding: 6px 14px; border-radius: 9999px; font-size: 0.82rem; color: #E2E8F0; display: inline-flex; align-items: center; gap: 6px;">
                <span style="color: #EC4899;">🎙️</span> <strong>256-d</strong> Voice Embeddings
            </div>
            <div style="background: rgba(255, 255, 255, 0.04); border: 1px solid rgba(255, 255, 255, 0.08); padding: 6px 14px; border-radius: 9999px; font-size: 0.82rem; color: #E2E8F0; display: inline-flex; align-items: center; gap: 6px;">
                <span style="color: #38BDF8;">☁️</span> <strong>Real-time</strong> Cloud Sync
            </div>
        </div>
    """, unsafe_allow_html=True)

    # Portal Selection Cards
    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.markdown("""
            <div>
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.75rem;">
                    <span style="background: rgba(59, 130, 246, 0.15); color: #93C5FD; font-size: 0.75rem; font-weight: 700; padding: 4px 10px; border-radius: 6px; letter-spacing: 0.05em; text-transform: uppercase;">
                        Student Access
                    </span>
                    <span style="color: #64748B; font-size: 0.8rem; font-weight: 500;">Face ID &bull; Rosters</span>
                </div>
                <h2 style="color: #FFFFFF; font-size: 1.65rem; margin: 0 0 0.4rem 0; font-weight: 700;">
                    Student Portal
                </h2>
                <p style="color: #94A3B8; font-size: 0.9rem; line-height: 1.5; margin: 0 0 1.25rem 0;">
                    Authenticate with 1-click Face ID, view real-time subject attendance rates, and enroll with join codes.
                </p>
                <div style="background: rgba(0, 0, 0, 0.2); border: 1px solid rgba(255, 255, 255, 0.05); padding: 12px 14px; border-radius: 10px; margin-bottom: 1.25rem;">
                    <div style="font-size: 0.82rem; color: #CBD5E1; margin-bottom: 4px;">&bull; <strong>Instant Face Verification</strong></div>
                    <div style="font-size: 0.82rem; color: #CBD5E1; margin-bottom: 4px;">&bull; <strong>Live Course Attendance Stats</strong></div>
                    <div style="font-size: 0.82rem; color: #CBD5E1;">&bull; <strong>Auto-Enroll Via QR / Codes</strong></div>
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
                    <span style="background: rgba(168, 85, 247, 0.15); color: #D8B4FE; font-size: 0.75rem; font-weight: 700; padding: 4px 10px; border-radius: 6px; letter-spacing: 0.05em; text-transform: uppercase;">
                        Educator Suite
                    </span>
                    <span style="color: #64748B; font-size: 0.8rem; font-weight: 500;">Multi-Face &bull; Voice AI</span>
                </div>
                <h2 style="color: #FFFFFF; font-size: 1.65rem; margin: 0 0 0.4rem 0; font-weight: 700;">
                    Teacher Portal
                </h2>
                <p style="color: #94A3B8; font-size: 0.9rem; line-height: 1.5; margin: 0 0 1.25rem 0;">
                    Perform simultaneous multi-face classroom recognition, run bulk voice roll calls, and export logs.
                </p>
                <div style="background: rgba(0, 0, 0, 0.2); border: 1px solid rgba(255, 255, 255, 0.05); padding: 12px 14px; border-radius: 10px; margin-bottom: 1.25rem;">
                    <div style="font-size: 0.82rem; color: #CBD5E1; margin-bottom: 4px;">&bull; <strong>Simultaneous Multi-Face Scan</strong></div>
                    <div style="font-size: 0.82rem; color: #CBD5E1; margin-bottom: 4px;">&bull; <strong>Audio Speaker Biometrics</strong></div>
                    <div style="font-size: 0.82rem; color: #CBD5E1;">&bull; <strong>Automated Roster & Export</strong></div>
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
        <div style="margin-top: 4.5rem; text-align: center;">
            <span style="font-size: 0.8rem; font-weight: 700; color: #818CF8; letter-spacing: 0.08em; text-transform: uppercase;">
                Effortless Workflow
            </span>
            <h2 style="color: #FFFFFF; font-size: 2rem; margin: 0.4rem 0 2rem 0; font-weight: 700;">
                How SnapClass Works
            </h2>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 1.5rem; text-align: left;">
                <div style="background: rgba(30, 41, 59, 0.3); border: 1px solid rgba(255, 255, 255, 0.06); padding: 1.5rem; border-radius: 1rem;">
                    <div style="background: rgba(99, 102, 241, 0.2); width: 36px; height: 36px; border-radius: 8px; display: flex; align-items: center; justify-content: center; font-weight: 800; color: #A5B4FC; margin-bottom: 0.75rem;">1</div>
                    <div style="color: #FFFFFF; font-weight: 600; font-size: 1.05rem; margin-bottom: 0.4rem;">Enroll Face & Voice</div>
                    <p style="color: #94A3B8; font-size: 0.88rem; line-height: 1.5; margin: 0;">Students take a single selfie and record a short phrase. Neural embeddings are safely stored.</p>
                </div>
                <div style="background: rgba(30, 41, 59, 0.3); border: 1px solid rgba(255, 255, 255, 0.06); padding: 1.5rem; border-radius: 1rem;">
                    <div style="background: rgba(168, 85, 247, 0.2); width: 36px; height: 36px; border-radius: 8px; display: flex; align-items: center; justify-content: center; font-weight: 800; color: #D8B4FE; margin-bottom: 0.75rem;">2</div>
                    <div style="color: #FFFFFF; font-weight: 600; font-size: 1.05rem; margin-bottom: 0.4rem;">Snap or Record Class</div>
                    <p style="color: #94A3B8; font-size: 0.88rem; line-height: 1.5; margin: 0;">The teacher snaps photos of the classroom or records audio of students responding.</p>
                </div>
                <div style="background: rgba(30, 41, 59, 0.3); border: 1px solid rgba(255, 255, 255, 0.06); padding: 1.5rem; border-radius: 1rem;">
                    <div style="background: rgba(16, 185, 129, 0.2); width: 36px; height: 36px; border-radius: 8px; display: flex; align-items: center; justify-content: center; font-weight: 800; color: #6EE7B7; margin-bottom: 0.75rem;">3</div>
                    <div style="color: #FFFFFF; font-weight: 600; font-size: 1.05rem; margin-bottom: 0.4rem;">Instant Verified Logs</div>
                    <p style="color: #94A3B8; font-size: 0.88rem; line-height: 1.5; margin: 0;">AI simultaneously detects and verifies all attendees, saving logs directly to cloud database.</p>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # Feature Capabilities Bento Grid
    st.markdown("""
        <div style="margin-top: 4.5rem; padding-top: 2.5rem; border-top: 1px solid rgba(255, 255, 255, 0.08);">
            <div style="text-align: center; margin-bottom: 2rem;">
                <span style="font-size: 0.8rem; font-weight: 700; color: #818CF8; letter-spacing: 0.08em; text-transform: uppercase;">Enterprise Features</span>
                <h2 style="color: #FFFFFF; font-size: 2rem; margin: 0.4rem 0 0 0; font-weight: 700;">Cutting-Edge AI Architecture</h2>
            </div>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 1.25rem;">
                <div style="background: rgba(255, 255, 255, 0.02); border: 1px solid rgba(255, 255, 255, 0.06); padding: 1.5rem; border-radius: 1rem;">
                    <div style="font-size: 1.75rem; margin-bottom: 0.5rem;">👁️</div>
                    <div style="color: #FFFFFF; font-weight: 600; font-size: 1rem; margin-bottom: 0.35rem;">Multi-Face Vision</div>
                    <div style="color: #64748B; font-size: 0.85rem; line-height: 1.5;">68-point facial landmark pose estimation with 128-d deep metric embeddings & SVM classification.</div>
                </div>
                <div style="background: rgba(255, 255, 255, 0.02); border: 1px solid rgba(255, 255, 255, 0.06); padding: 1.5rem; border-radius: 1rem;">
                    <div style="font-size: 1.75rem; margin-bottom: 0.5rem;">🎙️</div>
                    <div style="color: #FFFFFF; font-weight: 600; font-size: 1rem; margin-bottom: 0.35rem;">Speaker Biometrics</div>
                    <div style="color: #64748B; font-size: 0.85rem; line-height: 1.5;">Resemblyzer deep voice encoder with silence splitting to isolate individual student voices.</div>
                </div>
                <div style="background: rgba(255, 255, 255, 0.02); border: 1px solid rgba(255, 255, 255, 0.06); padding: 1.5rem; border-radius: 1rem;">
                    <div style="font-size: 1.75rem; margin-bottom: 0.5rem;">📱</div>
                    <div style="color: #FFFFFF; font-weight: 600; font-size: 1rem; margin-bottom: 0.35rem;">Responsive Everywhere</div>
                    <div style="color: #64748B; font-size: 0.85rem; line-height: 1.5;">Optimized for mobile phones, iPads, laptops, and smart classroom display boards.</div>
                </div>
                <div style="background: rgba(255, 255, 255, 0.02); border: 1px solid rgba(255, 255, 255, 0.06); padding: 1.5rem; border-radius: 1rem;">
                    <div style="font-size: 1.75rem; margin-bottom: 0.5rem;">🔒</div>
                    <div style="color: #FFFFFF; font-weight: 600; font-size: 1rem; margin-bottom: 0.35rem;">Supabase Security</div>
                    <div style="color: #64748B; font-size: 0.85rem; line-height: 1.5;">Encrypted bcrypt passwords, PostgreSQL relational joins, and secure JWT authentication.</div>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    footer_home()