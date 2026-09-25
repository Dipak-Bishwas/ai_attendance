import streamlit as st
from src.ui.base_layout import style_base_layout, style_background_home


def render_html(html_str):
    """
    Renders HTML in Streamlit with all leading indentation and empty lines stripped.
    This prevents CommonMark markdown parsers from treating 4-space indented HTML as code blocks.
    """
    cleaned = "\n".join(line.strip() for line in html_str.strip().splitlines() if line.strip())
    st.markdown(cleaned, unsafe_allow_html=True)


def home_screen():
    style_background_home()
    style_base_layout()

    logo_url = "https://i.ibb.co/YTYGn5qV/logo.png"

    # ==========================================
    # 1. TOP NAVBAR (Reference Image 1)
    # ==========================================
    render_html(f"""
<div style="background: #09090B; padding: 0.85rem 2rem; border-radius: 9999px; margin-bottom: 2.5rem; display: flex; align-items: center; justify-content: space-between; box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.25);">
<div style="display: flex; align-items: center; gap: 10px;">
<img src="{logo_url}" style="height: 34px; width: 34px; object-fit: contain;" />
<span style="font-family: 'Syne', 'Plus Jakarta Sans', sans-serif; font-weight: 800; font-size: 1.45rem; color: #FFFFFF; letter-spacing: -0.03em;">SnapClass</span>
</div>
<div style="display: flex; align-items: center; gap: 2.25rem;">
<a href="#hero" style="color: #FAFAFA; text-decoration: none; font-size: 0.9rem; font-weight: 600;">Home</a>
<a href="#features" style="color: #A1A1AA; text-decoration: none; font-size: 0.9rem; font-weight: 500;">Features</a>
<a href="#journey" style="color: #A1A1AA; text-decoration: none; font-size: 0.9rem; font-weight: 500;">Journey</a>
<a href="#tech" style="color: #A1A1AA; text-decoration: none; font-size: 0.9rem; font-weight: 500;">Tech Stack</a>
</div>
<div>
<a href="#get-started" style="background: #FFFFFF; color: #09090B; font-weight: 700; font-size: 0.86rem; padding: 9px 20px; border-radius: 9999px; text-decoration: none; display: inline-flex; align-items: center; gap: 6px; box-shadow: 0 2px 10px rgba(255, 255, 255, 0.25);">
Start AI Attendance &rsaquo;
</a>
</div>
</div>
""")

    # ==========================================
    # 2. HERO SECTION (Reference Image 1)
    # ==========================================
    h_col1, h_col2, h_col3 = st.columns([1.1, 2.6, 1.1], gap="medium")

    with h_col1:
        # Left Floating Preview Card (Tilted Attendance Report Preview)
        render_html("""
<div style="margin-top: 3.5rem; transform: rotate(-3deg); transition: transform 0.3s ease;">
<div style="background: #F8FAFC; border: 1px solid #E2E8F0; padding: 1.25rem; border-radius: 1.25rem; box-shadow: 0 20px 35px -10px rgba(0, 0, 0, 0.08);">
<div style="background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 0.875rem; padding: 1rem; box-shadow: 0 4px 12px rgba(0,0,0,0.03);">
<div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 8px;">
<div style="font-family: 'Syne', sans-serif; font-size: 0.85rem; font-weight: 800; color: #09090B;">📋 Attendance Report</div>
<span style="background: #4F46E5; width: 10px; height: 10px; border-radius: 50%;"></span>
</div>
<div style="display: flex; flex-direction: column; gap: 6px; font-size: 0.74rem;">
<div style="display: flex; justify-content: space-between; align-items: center; background: #F8FAFC; padding: 5px 8px; border-radius: 6px;">
<span style="font-weight: 600; color: #1E293B;">Hamza R.</span>
<span style="background: #ECFDF5; color: #047857; font-weight: 700; font-size: 0.68rem; padding: 2px 6px; border-radius: 4px;">✅ Present</span>
</div>
<div style="display: flex; justify-content: space-between; align-items: center; background: #F8FAFC; padding: 5px 8px; border-radius: 6px;">
<span style="font-weight: 600; color: #1E293B;">Ananya R.</span>
<span style="background: #ECFDF5; color: #047857; font-weight: 700; font-size: 0.68rem; padding: 2px 6px; border-radius: 4px;">✅ Present</span>
</div>
<div style="display: flex; justify-content: space-between; align-items: center; background: #F8FAFC; padding: 5px 8px; border-radius: 6px;">
<span style="font-weight: 600; color: #1E293B;">Akash S.</span>
<span style="background: #FEF2F2; color: #B91C1C; font-weight: 700; font-size: 0.68rem; padding: 2px 6px; border-radius: 4px;">❌ Absent</span>
</div>
</div>
</div>
</div>
</div>
""")

    with h_col2:
        # Center Hero Content
        render_html("""
<div id="hero" style="text-align: center;">
<div style="display: inline-flex; align-items: center; gap: 6px; background: #FFFFFF; border: 1px solid #E4E4E7; padding: 6px 18px; border-radius: 9999px; margin-bottom: 1.25rem; box-shadow: 0 1px 3px 0 rgba(0,0,0,0.04);">
<span style="width: 7px; height: 7px; background: #2563EB; border-radius: 50%;"></span>
<span style="font-size: 0.84rem; font-weight: 600; color: #18181B;">Welcome to SnapClass</span>
</div>
<h1 style="font-family: 'Syne', 'Plus Jakarta Sans', sans-serif; font-size: 4rem; font-weight: 800; line-height: 1.05; letter-spacing: -0.04em; margin: 0 0 1.25rem 0; color: #09090B;">
AI Powered<br/>
Attendance<br/>
<span style="color: #3B82F6;">System</span>
</h1>
<p style="max-width: 580px; font-size: 1.08rem; color: #52525B; line-height: 1.6; margin: 0 auto 1.75rem auto;">
Revolutionizing the classroom with next-gen computer vision and voice biometrics. Trusted by educators for speed, accuracy, and security.
</p>
</div>
""")

        # CTA Buttons Centered
        st.markdown("<div id='get-started' style='display: flex; justify-content: center;'></div>", unsafe_allow_html=True)
        btn_c1, btn_c2 = st.columns([1.1, 1], gap="small")
        with btn_c1:
            if st.button("Start as Teacher ›", type="primary", use_container_width=True, key="hero_start_teacher"):
                st.session_state['login_type'] = 'teacher'
                st.query_params['role'] = 'teacher'
                st.rerun()
        with btn_c2:
            if st.button("Enter as Student ›", type="secondary", use_container_width=True, key="hero_start_student"):
                st.session_state['login_type'] = 'student'
                st.query_params['role'] = 'student'
                st.rerun()

        # Hero Stat Pills Strip
        render_html("""
<div style="display: flex; justify-content: center; gap: 8px; flex-wrap: wrap; margin-top: 1.75rem;">
<span style="background: #F8FAFC; border: 1px solid #E2E8F0; padding: 4px 10px; border-radius: 9999px; font-size: 0.76rem; color: #334155;">⚡ <strong>&lt; 1s</strong> Multi-Face Scan</span>
<span style="background: #F8FAFC; border: 1px solid #E2E8F0; padding: 4px 10px; border-radius: 9999px; font-size: 0.76rem; color: #334155;">🎯 <strong>99.8%</strong> Precision</span>
<span style="background: #F8FAFC; border: 1px solid #E2E8F0; padding: 4px 10px; border-radius: 9999px; font-size: 0.76rem; color: #334155;">🎙️ <strong>256-d</strong> Voice AI</span>
</div>
""")

    with h_col3:
        # Right Floating Preview Card (Tilted Snap ID Camera Card)
        render_html("""
<div style="margin-top: 3.5rem; transform: rotate(3deg); transition: transform 0.3s ease;">
<div style="background: linear-gradient(135deg, #4F46E5 0%, #3B82F6 100%); border: 1px solid #4338CA; padding: 1.5rem 1.25rem; border-radius: 1.25rem; box-shadow: 0 20px 35px -10px rgba(79, 70, 229, 0.35); text-align: center; color: #FFFFFF;">
<div style="font-size: 2.2rem; margin-bottom: 6px;">📸</div>
<div style="font-family: 'Syne', sans-serif; font-weight: 800; font-size: 1.25rem; letter-spacing: -0.02em;">SNAP ID</div>
<div style="font-size: 0.75rem; color: #E0E7FF; margin-top: 4px;">1-Click Face Recognition</div>
<div style="background: rgba(255, 255, 255, 0.15); border: 1px dashed rgba(255, 255, 255, 0.3); border-radius: 8px; padding: 6px; margin-top: 10px; font-size: 0.7rem; color: #FFFFFF;">
🎯 Confidence: 99.8%
</div>
</div>
</div>
""")

    # ==========================================
    # 3. INNOVATIVE FEATURES SECTION (Reference Image 3)
    # ==========================================
    render_html("""
<div id="features" style="margin-top: 6.5rem; text-align: center;">
<h2 style="font-family: 'Syne', 'Plus Jakarta Sans', sans-serif; font-size: 2.8rem; font-weight: 800; letter-spacing: -0.04em; color: #09090B; margin-bottom: 2.5rem;">
Innovative Features
</h2>
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 1.75rem; text-align: center;">
<div style="background: #FFFFFF; border: 1px solid #E4E4E7; padding: 2.5rem 2rem; border-radius: 1.25rem; box-shadow: 0 4px 20px -4px rgba(0, 0, 0, 0.04);">
<div style="background: #F8FAFC; border: 1px solid #E2E8F0; width: 68px; height: 68px; border-radius: 1.25rem; display: flex; align-items: center; justify-content: center; font-size: 2.2rem; margin: 0 auto 1.25rem auto;">
📸
</div>
<h3 style="font-family: 'Syne', 'Plus Jakarta Sans', sans-serif; font-size: 1.35rem; font-weight: 800; letter-spacing: -0.02em; color: #09090B; margin: 0 0 0.75rem 0;">
AI Face Analysis
</h3>
<p style="color: #52525B; font-size: 0.92rem; line-height: 1.6; margin: 0;">
Advanced neural networks recognize every student's face from a single class photo, making attendance instant and accurate.
</p>
</div>
<div style="background: #FFFFFF; border: 1px solid #E4E4E7; padding: 2.5rem 2rem; border-radius: 1.25rem; box-shadow: 0 4px 20px -4px rgba(0, 0, 0, 0.04);">
<div style="background: #F8FAFC; border: 1px solid #E2E8F0; width: 68px; height: 68px; border-radius: 1.25rem; display: flex; align-items: center; justify-content: center; font-size: 2.2rem; margin: 0 auto 1.25rem auto;">
🎙️
</div>
<h3 style="font-family: 'Syne', 'Plus Jakarta Sans', sans-serif; font-size: 1.35rem; font-weight: 800; letter-spacing: -0.02em; color: #09090B; margin: 0 0 0.75rem 0;">
Sequential Voice ID
</h3>
<p style="color: #52525B; font-size: 0.92rem; line-height: 1.6; margin: 0;">
Students say "Present" one-by-one, and our audio-AI matches their voice biometrics against stored embeddings in real-time.
</p>
</div>
<div style="background: #FFFFFF; border: 1px solid #E4E4E7; padding: 2.5rem 2rem; border-radius: 1.25rem; box-shadow: 0 4px 20px -4px rgba(0, 0, 0, 0.04);">
<div style="background: #F8FAFC; border: 1px solid #E2E8F0; width: 68px; height: 68px; border-radius: 1.25rem; display: flex; align-items: center; justify-content: center; font-size: 2.2rem; margin: 0 auto 1.25rem auto;">
📱
</div>
<h3 style="font-family: 'Syne', 'Plus Jakarta Sans', sans-serif; font-size: 1.35rem; font-weight: 800; letter-spacing: -0.02em; color: #09090B; margin: 0 0 0.75rem 0;">
QR-Driven Rosters
</h3>
<p style="color: #52525B; font-size: 0.92rem; line-height: 1.6; margin: 0;">
Course codes generate unique links for instant student enrollment without manual entry or data mismatch headaches.
</p>
</div>
</div>
</div>
""")

    # ==========================================
    # 4. STEP-BY-STEP USER JOURNEY (All 6 Steps from Reference Images)
    # ==========================================
    render_html("""
<div id="journey" style="margin-top: 7rem;">
<div style="text-align: center; margin-bottom: 4rem;">
<span style="font-size: 0.8rem; font-weight: 700; color: #4F46E5; letter-spacing: 0.08em; text-transform: uppercase;">User Journey</span>
<h2 style="font-family: 'Syne', 'Plus Jakarta Sans', sans-serif; font-size: 2.8rem; font-weight: 800; letter-spacing: -0.04em; color: #09090B; margin: 0.25rem 0 0 0;">
How It Works
</h2>
</div>
</div>
""")

    # STEP 01: Secure Login (Image 4)
    s1_col1, s1_col2 = st.columns([1, 1.2], gap="large")
    with s1_col1:
        render_html("""
<div style="padding: 1.5rem 0;">
<span style="font-size: 0.85rem; font-weight: 700; color: #4F46E5; letter-spacing: 0.06em; text-transform: uppercase;">
STEP 01
</span>
<h2 style="font-family: 'Syne', 'Plus Jakarta Sans', sans-serif; font-size: 2.6rem; font-weight: 800; letter-spacing: -0.03em; color: #09090B; margin: 0.5rem 0 1rem 0;">
Secure<br/>Login
</h2>
<p style="color: #52525B; font-size: 1rem; line-height: 1.6; max-width: 440px;">
Start your session with our high-security authentication portal. Your data is encrypted and synced across all your devices.
</p>
</div>
""")

    with s1_col2:
        render_html(f"""
<div style="background: #EEF2FF; border: 1px solid #E0E7FF; padding: 2rem; border-radius: 1.5rem; box-shadow: 0 10px 30px -10px rgba(79, 70, 229, 0.15);">
<div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1.25rem;">
<div style="display: flex; align-items: center; gap: 8px;">
<img src="{logo_url}" style="height: 28px; width: 28px; object-fit: contain;" />
<span style="font-family: 'Syne', sans-serif; font-weight: 800; font-size: 1.1rem; color: #1E1B4B;">SNAP CLASS</span>
</div>
<span style="background: #F43F5E; color: #FFFFFF; font-size: 0.72rem; font-weight: 600; padding: 3px 8px; border-radius: 9999px;">Go back to Home</span>
</div>
<div style="background: #FFFFFF; border-radius: 1rem; padding: 1.5rem; box-shadow: 0 4px 12px rgba(0,0,0,0.03);">
<div style="font-family: 'Syne', sans-serif; font-weight: 800; font-size: 1.15rem; color: #09090B; margin-bottom: 1rem; text-align: center;">Login using password</div>
<div style="background: #F8FAFC; border: 1px solid #E2E8F0; padding: 8px 12px; border-radius: 6px; font-size: 0.8rem; color: #64748B; margin-bottom: 8px;">@teacher_username</div>
<div style="background: #F8FAFC; border: 1px solid #E2E8F0; padding: 8px 12px; border-radius: 6px; font-size: 0.8rem; color: #64748B; margin-bottom: 12px;">••••••••••••</div>
<div style="display: flex; gap: 8px;">
<div style="background: #F43F5E; color: #FFFFFF; font-weight: 700; font-size: 0.78rem; padding: 8px 14px; border-radius: 6px; text-align: center; flex: 1;">👤 Login</div>
<div style="background: #4F46E5; color: #FFFFFF; font-weight: 700; font-size: 0.78rem; padding: 8px 14px; border-radius: 6px; text-align: center; flex: 1;">👥 Register instead</div>
</div>
</div>
</div>
""")

    render_html("<div style='margin-top: 4.5rem;'></div>")

    # STEP 02: Interactive Dashboard (Image 5)
    s2_col1, s2_col2 = st.columns([1, 1.2], gap="large")
    with s2_col1:
        render_html("""
<div style="padding: 1.5rem 0;">
<span style="font-size: 0.85rem; font-weight: 700; color: #4F46E5; letter-spacing: 0.06em; text-transform: uppercase;">
STEP 02
</span>
<h2 style="font-family: 'Syne', 'Plus Jakarta Sans', sans-serif; font-size: 2.6rem; font-weight: 800; letter-spacing: -0.03em; color: #09090B; margin: 0.5rem 0 1rem 0;">
Interactive<br/>Dashboard
</h2>
<p style="color: #52525B; font-size: 1rem; line-height: 1.6; max-width: 440px;">
Manage all your subjects, attendance logs, and student rosters from a single, beautiful unified stream.
</p>
</div>
""")

    with s2_col2:
        render_html(f"""
<div style="background: #EEF2FF; border: 1px solid #E0E7FF; padding: 2rem; border-radius: 1.5rem; box-shadow: 0 10px 30px -10px rgba(79, 70, 229, 0.15);">
<div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1.25rem;">
<div style="display: flex; align-items: center; gap: 8px;">
<img src="{logo_url}" style="height: 28px; width: 28px; object-fit: contain;" />
<span style="font-family: 'Syne', sans-serif; font-weight: 800; font-size: 1.1rem; color: #1E1B4B;">SNAP CLASS</span>
</div>
<div style="text-align: right;">
<div style="font-size: 0.8rem; font-weight: 700; color: #09090B;">Welcome, Educator!</div>
<span style="background: #F43F5E; color: #FFFFFF; font-size: 0.68rem; font-weight: 600; padding: 2px 6px; border-radius: 4px;">Logout</span>
</div>
</div>
<div style="background: #FFFFFF; border-radius: 1rem; padding: 1.25rem; box-shadow: 0 4px 12px rgba(0,0,0,0.03);">
<div style="display: flex; gap: 6px; margin-bottom: 1rem;">
<span style="background: #4F46E5; color: #FFFFFF; font-weight: 700; font-size: 0.75rem; padding: 5px 10px; border-radius: 6px;">📷 Take Attendance</span>
<span style="background: #09090B; color: #FFFFFF; font-weight: 700; font-size: 0.75rem; padding: 5px 10px; border-radius: 6px;">📚 Manage</span>
<span style="background: #09090B; color: #FFFFFF; font-weight: 700; font-size: 0.75rem; padding: 5px 10px; border-radius: 6px;">📊 Records</span>
</div>
<div style="font-family: 'Syne', sans-serif; font-weight: 800; font-size: 1rem; color: #09090B; margin-bottom: 8px;">Take AI Attendance</div>
<div style="background: #F8FAFC; border: 1px solid #E2E8F0; padding: 8px 10px; border-radius: 6px; font-size: 0.78rem; color: #64748B; margin-bottom: 10px;">Intro to Machine Learning (CS111)</div>
<div style="display: flex; gap: 6px; flex-wrap: wrap;">
<span style="background: #09090B; color: #FFFFFF; font-size: 0.72rem; font-weight: 600; padding: 4px 8px; border-radius: 4px;">Clear All</span>
<span style="background: #F43F5E; color: #FFFFFF; font-size: 0.72rem; font-weight: 600; padding: 4px 8px; border-radius: 4px;">Run Face Analysis</span>
<span style="background: #4F46E5; color: #FFFFFF; font-size: 0.72rem; font-weight: 600; padding: 4px 8px; border-radius: 4px;">Use Voice</span>
</div>
</div>
</div>
""")

    render_html("<div style='margin-top: 4.5rem;'></div>")

    # STEP 03: Course Management (New Image 1)
    s3_col1, s3_col2 = st.columns([1, 1.2], gap="large")
    with s3_col1:
        render_html("""
<div style="padding: 1.5rem 0;">
<span style="font-size: 0.85rem; font-weight: 700; color: #4F46E5; letter-spacing: 0.06em; text-transform: uppercase;">
STEP 03
</span>
<h2 style="font-family: 'Syne', 'Plus Jakarta Sans', sans-serif; font-size: 2.6rem; font-weight: 800; letter-spacing: -0.03em; color: #09090B; margin: 0.5rem 0 1rem 0;">
Course<br/>Management
</h2>
<p style="color: #52525B; font-size: 1rem; line-height: 1.6; max-width: 440px;">
Creating a new subject is a breeze. Just name it, and SnapClass generates everything you need to start tracking.
</p>
</div>
""")

    with s3_col2:
        render_html("""
<div style="background: #64748B; padding: 2rem; border-radius: 1.5rem; box-shadow: 0 10px 30px -10px rgba(100, 116, 139, 0.25);">
<div style="background: #FFFFFF; border-radius: 1.25rem; padding: 1.75rem; box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.2);">
<div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
<h4 style="font-family: 'Syne', sans-serif; font-weight: 800; font-size: 1.2rem; color: #09090B; margin: 0;">Create New Subject</h4>
<span style="background: #4F46E5; width: 16px; height: 16px; border-radius: 50%;"></span>
</div>
<p style="color: #71717A; font-size: 0.8rem; margin: 0 0 1rem 0;">Enter the details of the new subject batch.</p>
<div style="margin-bottom: 10px;">
<label style="font-size: 0.75rem; font-weight: 600; color: #334155; display: block; margin-bottom: 3px;">Subject Code</label>
<div style="background: #FFFFFF; border: 1px solid #CBD5E1; padding: 8px 12px; border-radius: 6px; font-size: 0.85rem; color: #09090B;">CS101</div>
</div>
<div style="margin-bottom: 10px;">
<label style="font-size: 0.75rem; font-weight: 600; color: #334155; display: block; margin-bottom: 3px;">Subject Name</label>
<div style="background: #F8FAFC; border: 1px solid #E2E8F0; padding: 8px 12px; border-radius: 6px; font-size: 0.85rem; color: #94A3B8;">Intro to AI</div>
</div>
<div style="margin-bottom: 1.25rem;">
<label style="font-size: 0.75rem; font-weight: 600; color: #334155; display: block; margin-bottom: 3px;">Section</label>
<div style="background: #F8FAFC; border: 1px solid #E2E8F0; padding: 8px 12px; border-radius: 6px; font-size: 0.85rem; color: #94A3B8;">A</div>
</div>
<div style="background: #4F46E5; color: #FFFFFF; font-weight: 700; font-size: 0.88rem; padding: 10px; border-radius: 8px; text-align: center;">
Create Subject Now
</div>
</div>
</div>
""")

    render_html("<div style='margin-top: 4.5rem;'></div>")

    # STEP 04: FaceID Attendance (New Image 2)
    s4_col1, s4_col2 = st.columns([1, 1.2], gap="large")
    with s4_col1:
        render_html("""
<div style="padding: 1.5rem 0;">
<span style="font-size: 0.85rem; font-weight: 700; color: #4F46E5; letter-spacing: 0.06em; text-transform: uppercase;">
STEP 04
</span>
<h2 style="font-family: 'Syne', 'Plus Jakarta Sans', sans-serif; font-size: 2.6rem; font-weight: 800; letter-spacing: -0.03em; color: #09090B; margin: 0.5rem 0 1rem 0;">
FaceID<br/>Attendance
</h2>
<p style="color: #52525B; font-size: 1rem; line-height: 1.6; max-width: 440px;">
Use high-speed computer vision to scan the entire room. Our AI identifies every student from a single class photo in milliseconds.
</p>
</div>
""")

    with s4_col2:
        render_html("""
<div style="background: #475569; padding: 2rem; border-radius: 1.5rem; box-shadow: 0 10px 30px -10px rgba(71, 85, 105, 0.3);">
<div style="background: #FFFFFF; border-radius: 1.25rem; padding: 1.5rem; box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.25);">
<div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.75rem;">
<div style="font-family: 'Syne', sans-serif; font-weight: 800; font-size: 1.1rem; color: #09090B;">📋 Attendance Report</div>
<span style="background: #4F46E5; width: 14px; height: 14px; border-radius: 50%;"></span>
</div>
<p style="color: #71717A; font-size: 0.75rem; margin: 0 0 10px 0;">Please review the detected attendance before confirming.</p>
<div style="overflow-x: auto; margin-bottom: 1rem;">
<table style="width: 100%; border-collapse: collapse; font-size: 0.78rem;">
<tr style="border-bottom: 1px solid #E2E8F0; color: #64748B;">
<th style="padding: 4px; text-align: left;">Name</th>
<th style="padding: 4px; text-align: left;">ID</th>
<th style="padding: 4px; text-align: left;">Source</th>
<th style="padding: 4px; text-align: left;">Status</th>
</tr>
<tr style="border-bottom: 1px solid #F1F5F9;">
<td style="padding: 5px 4px; font-weight: 600;">Mihika</td>
<td style="padding: 5px 4px;">5</td>
<td style="padding: 5px 4px; color: #64748B;">Photo 1, Photo 2</td>
<td style="padding: 5px 4px; color: #047857; font-weight: 700;">✅ Present</td>
</tr>
<tr style="border-bottom: 1px solid #F1F5F9;">
<td style="padding: 5px 4px; font-weight: 600;">Ayan Dey</td>
<td style="padding: 5px 4px;">8</td>
<td style="padding: 5px 4px; color: #64748B;">Photo 1, Photo 2</td>
<td style="padding: 5px 4px; color: #047857; font-weight: 700;">✅ Present</td>
</tr>
<tr>
<td style="padding: 5px 4px; font-weight: 600;">Hamza Rizvi</td>
<td style="padding: 5px 4px;">14</td>
<td style="padding: 5px 4px; color: #64748B;">Photo 1</td>
<td style="padding: 5px 4px; color: #047857; font-weight: 700;">✅ Present</td>
</tr>
</table>
</div>
<div style="display: flex; gap: 8px;">
<div style="background: #F43F5E; color: #FFFFFF; font-weight: 700; font-size: 0.78rem; padding: 8px; border-radius: 6px; text-align: center; flex: 1;">Discard</div>
<div style="background: #4F46E5; color: #FFFFFF; font-weight: 700; font-size: 0.78rem; padding: 8px; border-radius: 6px; text-align: center; flex: 1;">Confirm & Save</div>
</div>
</div>
</div>
""")

    render_html("<div style='margin-top: 4.5rem;'></div>")

    # STEP 05: Voice ID Attendance (New Image 3)
    s5_col1, s5_col2 = st.columns([1, 1.2], gap="large")
    with s5_col1:
        render_html("""
<div style="padding: 1.5rem 0;">
<span style="font-size: 0.85rem; font-weight: 700; color: #4F46E5; letter-spacing: 0.06em; text-transform: uppercase;">
STEP 05
</span>
<h2 style="font-family: 'Syne', 'Plus Jakarta Sans', sans-serif; font-size: 2.6rem; font-weight: 800; letter-spacing: -0.03em; color: #09090B; margin: 0.5rem 0 1rem 0;">
Voice ID<br/>Attendance
</h2>
<p style="color: #52525B; font-size: 1rem; line-height: 1.6; max-width: 440px;">
Switch to voice mode for a futuristic roll-call. Students speak sequentially, and our AI matches their unique voice signatures.
</p>
</div>
""")

    with s5_col2:
        render_html("""
<div style="background: #475569; padding: 2rem; border-radius: 1.5rem; box-shadow: 0 10px 30px -10px rgba(71, 85, 105, 0.3);">
<div style="background: #FFFFFF; border-radius: 1.25rem; padding: 1.5rem; box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.25);">
<div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
<div style="font-family: 'Syne', sans-serif; font-weight: 800; font-size: 1.1rem; color: #09090B;">🎙️ Voice Attendance</div>
<span style="background: #4F46E5; width: 14px; height: 14px; border-radius: 50%;"></span>
</div>
<p style="color: #71717A; font-size: 0.75rem; margin: 0 0 10px 0;">Record audio of students saying "I am present". AI recognizes enrolled voices.</p>
<div style="background: #F8FAFC; border: 1px solid #E2E8F0; padding: 8px 12px; border-radius: 8px; display: flex; align-items: center; justify-content: space-between; margin-bottom: 12px;">
<div style="display: flex; align-items: center; gap: 6px;">
<span style="background: #4F46E5; color: #FFFFFF; width: 22px; height: 22px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 0.7rem;">▶</span>
<span style="color: #94A3B8; font-size: 0.75rem;">||| | ||||| | ||| ||</span>
</div>
<span style="color: #64748B; font-size: 0.72rem;">00:04</span>
</div>
<div style="background: #4F46E5; color: #FFFFFF; font-weight: 700; font-size: 0.8rem; padding: 8px; border-radius: 6px; text-align: center; margin-bottom: 12px;">
Analyze Voice Attendance
</div>
<div style="display: flex; justify-content: space-between; font-size: 0.75rem; background: #F8FAFC; padding: 6px 8px; border-radius: 4px;">
<span>Hamza Rizvi (Match: 0.77)</span>
<span style="color: #047857; font-weight: 700;">✅ Present</span>
</div>
</div>
</div>
""")

    render_html("<div style='margin-top: 4.5rem;'></div>")

    # STEP 06: Actionable Records (New Image 4)
    s6_col1, s6_col2 = st.columns([1, 1.2], gap="large")
    with s6_col1:
        render_html("""
<div style="padding: 1.5rem 0;">
<span style="font-size: 0.85rem; font-weight: 700; color: #4F46E5; letter-spacing: 0.06em; text-transform: uppercase;">
STEP 06
</span>
<h2 style="font-family: 'Syne', 'Plus Jakarta Sans', sans-serif; font-size: 2.6rem; font-weight: 800; letter-spacing: -0.03em; color: #09090B; margin: 0.5rem 0 1rem 0;">
Actionable<br/>Records
</h2>
<p style="color: #52525B; font-size: 1rem; line-height: 1.6; max-width: 440px;">
Review and manage historical logs. View confidence scores, download CSV reports, and track long-term attendance trends.
</p>
</div>
""")

    with s6_col2:
        render_html(f"""
<div style="background: #EEF2FF; border: 1px solid #E0E7FF; padding: 2rem; border-radius: 1.5rem; box-shadow: 0 10px 30px -10px rgba(79, 70, 229, 0.15);">
<div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1.25rem;">
<div style="display: flex; align-items: center; gap: 8px;">
<img src="{logo_url}" style="height: 28px; width: 28px; object-fit: contain;" />
<span style="font-family: 'Syne', sans-serif; font-weight: 800; font-size: 1.1rem; color: #1E1B4B;">SNAP CLASS</span>
</div>
<div style="text-align: right;">
<div style="font-size: 0.8rem; font-weight: 700; color: #09090B;">Welcome, Educator!</div>
<span style="background: #F43F5E; color: #FFFFFF; font-size: 0.68rem; font-weight: 600; padding: 2px 6px; border-radius: 4px;">Logout</span>
</div>
</div>
<div style="background: #FFFFFF; border-radius: 1rem; padding: 1.25rem; box-shadow: 0 4px 12px rgba(0,0,0,0.03);">
<div style="font-family: 'Syne', sans-serif; font-weight: 800; font-size: 1.1rem; color: #09090B; margin-bottom: 10px;">Attendance Records</div>
<table style="width: 100%; border-collapse: collapse; font-size: 0.74rem;">
<tr style="border-bottom: 1px solid #E2E8F0; color: #64748B;">
<th style="padding: 4px; text-align: left;">Time</th>
<th style="padding: 4px; text-align: left;">Subject</th>
<th style="padding: 4px; text-align: left;">Code</th>
<th style="padding: 4px; text-align: left;">Stats</th>
</tr>
<tr style="border-bottom: 1px solid #F1F5F9;">
<td style="padding: 5px 4px; color: #64748B;">2026-03-19 09:50 PM</td>
<td style="padding: 5px 4px; font-weight: 600;">Intro to ML</td>
<td style="padding: 5px 4px;">CS111</td>
<td style="padding: 5px 4px; color: #047857; font-weight: 700;">✅ 4/4 Students</td>
</tr>
<tr>
<td style="padding: 5px 4px; color: #64748B;">2026-03-19 09:48 PM</td>
<td style="padding: 5px 4px; font-weight: 600;">Intro to ML</td>
<td style="padding: 5px 4px;">CS111</td>
<td style="padding: 5px 4px; color: #047857; font-weight: 700;">✅ 1/4 Students</td>
</tr>
</table>
</div>
</div>
""")

    # ==========================================
    # 5. TECH STACK / ARCHITECTURE SECTION
    # ==========================================
    render_html("""
<div id="tech" style="margin-top: 6rem; text-align: center;">
<span style="font-size: 0.8rem; font-weight: 700; color: #4F46E5; letter-spacing: 0.08em; text-transform: uppercase;">Infrastructure</span>
<h2 style="font-family: 'Syne', 'Plus Jakarta Sans', sans-serif; font-size: 2.8rem; font-weight: 800; letter-spacing: -0.04em; color: #09090B; margin: 0.25rem 0 2.5rem 0;">
Built with Modern AI Stack
</h2>
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 1.25rem; text-align: left;">
<div style="background: #FFFFFF; border: 1px solid #E4E4E7; padding: 1.5rem; border-radius: 1rem; box-shadow: 0 4px 12px rgba(0,0,0,0.03);">
<div style="font-size: 1.75rem; margin-bottom: 0.5rem;">🧠</div>
<h4 style="font-family: 'Syne', sans-serif; font-weight: 800; font-size: 1.1rem; color: #09090B; margin: 0 0 0.35rem 0;">dlib & 128-d Embeddings</h4>
<p style="color: #64748B; font-size: 0.84rem; line-height: 1.5; margin: 0;">Multi-face pose detection and Euclidean distance metric verification.</p>
</div>
<div style="background: #FFFFFF; border: 1px solid #E4E4E7; padding: 1.5rem; border-radius: 1rem; box-shadow: 0 4px 12px rgba(0,0,0,0.03);">
<div style="font-size: 1.75rem; margin-bottom: 0.5rem;">🎙️</div>
<h4 style="font-family: 'Syne', sans-serif; font-weight: 800; font-size: 1.1rem; color: #09090B; margin: 0 0 0.35rem 0;">Resemblyzer & Librosa</h4>
<p style="color: #64748B; font-size: 0.84rem; line-height: 1.5; margin: 0;">256-d voice embeddings with spectral silence splitting for group audio.</p>
</div>
<div style="background: #FFFFFF; border: 1px solid #E4E4E7; padding: 1.5rem; border-radius: 1rem; box-shadow: 0 4px 12px rgba(0,0,0,0.03);">
<div style="font-size: 1.75rem; margin-bottom: 0.5rem;">⚡</div>
<h4 style="font-family: 'Syne', sans-serif; font-weight: 800; font-size: 1.1rem; color: #09090B; margin: 0 0 0.35rem 0;">Supabase PostgreSQL</h4>
<p style="color: #64748B; font-size: 0.84rem; line-height: 1.5; margin: 0;">Real-time cloud synchronization, relational joins, and secure bcrypt storage.</p>
</div>
<div style="background: #FFFFFF; border: 1px solid #E4E4E7; padding: 1.5rem; border-radius: 1rem; box-shadow: 0 4px 12px rgba(0,0,0,0.03);">
<div style="font-size: 1.75rem; margin-bottom: 0.5rem;">💻</div>
<h4 style="font-family: 'Syne', sans-serif; font-weight: 800; font-size: 1.1rem; color: #09090B; margin: 0 0 0.35rem 0;">Streamlit Enterprise UI</h4>
<p style="color: #64748B; font-size: 0.84rem; line-height: 1.5; margin: 0;">Responsive mobile and desktop layout with seamless component reactivity.</p>
</div>
</div>
</div>
""")

    # ==========================================
    # 6. DARK FOOTER (Reference Image 2)
    # ==========================================
    render_html(f"""
<div style="margin-top: 6rem; background: #000000; color: #FFFFFF; padding: 4rem 2.5rem 2rem 2.5rem; border-radius: 1.5rem 1.5rem 0 0; margin-left: -1.5rem; margin-right: -1.5rem; margin-bottom: -2rem;">
<div style="display: grid; grid-template-columns: 2fr 1fr 1fr 1fr; gap: 2.5rem; margin-bottom: 3rem;">
<div>
<div style="display: flex; align-items: center; gap: 10px; margin-bottom: 1.25rem;">
<img src="{logo_url}" style="height: 36px; width: 36px; object-fit: contain;" />
<span style="font-family: 'Syne', 'Plus Jakarta Sans', sans-serif; font-weight: 800; font-size: 1.5rem; color: #FFFFFF; letter-spacing: -0.03em;">SnapClass</span>
</div>
<p style="color: #A1A1AA; font-size: 0.88rem; line-height: 1.6; max-width: 300px; margin: 0;">
The next generation of classroom management, powered by advanced AI biometrics. Join the future of education today.
</p>
</div>
<div>
<h4 style="font-family: 'Syne', sans-serif; font-size: 1rem; font-weight: 800; color: #FFFFFF; margin: 0 0 1rem 0;">Product</h4>
<div style="display: flex; flex-direction: column; gap: 0.6rem; font-size: 0.84rem; color: #A1A1AA;">
<span>AI Attendance</span>
<span>Smart Roster</span>
<span>Tech Stack</span>
<span>Student Portal</span>
</div>
</div>
<div>
<h4 style="font-family: 'Syne', sans-serif; font-size: 1rem; font-weight: 800; color: #FFFFFF; margin: 0 0 1rem 0;">Experience</h4>
<div style="display: flex; flex-direction: column; gap: 0.6rem; font-size: 0.84rem; color: #A1A1AA;">
<span>Teacher Journey</span>
<span>Student Journey</span>
<span>Voice ID Roll-call</span>
<span>FaceID Scan</span>
</div>
</div>
<div>
<h4 style="font-family: 'Syne', sans-serif; font-size: 1rem; font-weight: 800; color: #FFFFFF; margin: 0 0 1rem 0;">Company</h4>
<div style="display: flex; flex-direction: column; gap: 0.6rem; font-size: 0.84rem; color: #A1A1AA;">
<span>About Us</span>
<span>How it Works</span>
<span>Privacy Policy</span>
<span>Terms of Service</span>
</div>
</div>
</div>
<div style="border-top: 1px solid rgba(255, 255, 255, 0.1); padding-top: 1.5rem; text-align: center; font-size: 0.8rem; color: #71717A;">
&copy; 2026 SnapClass AI. Built with ❤️ for educators everywhere.
</div>
</div>
""")