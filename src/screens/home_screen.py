import os
import base64
import streamlit as st
from src.ui.base_layout import style_base_layout, style_background_home


def get_image_base64(file_path):
    if os.path.exists(file_path):
        with open(file_path, "rb") as f:
            encoded = base64.b64encode(f.read()).decode("utf-8")
        return f"data:image/png;base64,{encoded}"
    return ""


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

    photos_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "photos"))
    jiraya_path = os.path.join(photos_dir, "jiraya.png")
    naruto_path = os.path.join(photos_dir, "naruto.png")

    jiraya_img = get_image_base64(jiraya_path)
    naruto_img = get_image_base64(naruto_path)

    teacher_icon_html = f'<img src="{jiraya_img}" style="width: 44px; height: 44px; border-radius: 10px; object-fit: cover; border: 1px solid #E4E4E7;" />' if jiraya_img else '<div style="background: #EC4899; color: #FFFFFF; width: 40px; height: 40px; border-radius: 10px; display: flex; align-items: center; justify-content: center; font-size: 1.3rem;">👨‍🏫</div>'
    student_icon_html = f'<img src="{naruto_img}" style="width: 44px; height: 44px; border-radius: 10px; object-fit: cover; border: 1px solid #E4E4E7;" />' if naruto_img else '<div style="background: #4F46E5; color: #FFFFFF; width: 40px; height: 40px; border-radius: 10px; display: flex; align-items: center; justify-content: center; font-size: 1.3rem;">🎓</div>'

    # ==========================================
    # 1. TOP NAVBAR (Reference Image 1)
    # ==========================================
    render_html(f"""
<div id="snap-nav-wrapper" class="sticky-nav-container">
<div class="top-navbar-box">
<div style="display: flex; align-items: center; gap: 10px;">
<img src="{logo_url}" class="nav-brand-logo" />
<span class="nav-brand-title">SnapClass</span>
</div>
<div class="nav-link-group">
<a href="#hero" class="nav-link-item">Home</a>
<a href="#features" class="nav-link-item">Features</a>
<a href="#journey" class="nav-link-item">Journey</a>
<a href="#tech" class="nav-link-item">Tech Stack</a>
</div>
<div>
<a href="#get-started" class="nav-cta-btn">
Start AI Attendance &rsaquo;
</a>
</div>
</div>
</div>

<style>
.sticky-nav-container {{
    position: fixed !important;
    top: 1rem !important;
    left: 50% !important;
    transform: translateX(-50%) !important;
    width: min(1180px, calc(100vw - 2.5rem)) !important;
    z-index: 999999 !important;
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
}}

.sticky-nav-container.scrolled {{
    top: 0.5rem !important;
    width: min(1080px, calc(100vw - 1.5rem)) !important;
}}

.top-navbar-box {{
    background: rgba(9, 9, 11, 0.94);
    backdrop-filter: blur(14px);
    -webkit-backdrop-filter: blur(14px);
    padding: 0.85rem 2rem;
    border-radius: 9999px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    box-shadow: 0 10px 30px -5px rgba(0, 0, 0, 0.35);
    border: 1px solid rgba(255, 255, 255, 0.12);
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}}

.top-navbar-box a,
.top-navbar-box a:link,
.top-navbar-box a:visited,
.top-navbar-box a:hover,
.top-navbar-box a:active {{
    text-decoration: none !important;
}}

.sticky-nav-container.scrolled .top-navbar-box {{
    padding: 0.45rem 1.35rem;
    background: rgba(9, 9, 11, 0.96);
    box-shadow: 0 15px 35px -5px rgba(0, 0, 0, 0.5);
    border-color: rgba(255, 255, 255, 0.22);
}}

.nav-brand-logo {{
    height: 34px;
    width: 34px;
    object-fit: contain;
    transition: all 0.3s ease;
}}

.sticky-nav-container.scrolled .nav-brand-logo {{
    height: 25px;
    width: 25px;
}}

.nav-brand-title {{
    font-family: 'Syne', 'Plus Jakarta Sans', sans-serif;
    font-weight: 800;
    font-size: 1.45rem;
    color: #FFFFFF !important;
    letter-spacing: -0.03em;
    transition: all 0.3s ease;
}}

.sticky-nav-container.scrolled .nav-brand-title {{
    font-size: 1.1rem;
}}

.nav-link-group {{
    display: flex;
    align-items: center;
    gap: 2.25rem;
    transition: all 0.3s ease;
}}

.sticky-nav-container.scrolled .nav-link-group {{
    gap: 1.25rem;
}}

.nav-link-item,
.nav-link-item:link,
.nav-link-item:visited,
.nav-link-item:hover,
.nav-link-item:active,
.nav-link-item:focus {{
    color: #FFFFFF !important;
    text-decoration: none !important;
    font-size: 0.9rem !important;
    font-weight: 600 !important;
    transition: all 0.2s ease !important;
}}

.nav-link-item:hover {{
    opacity: 0.8 !important;
}}

.sticky-nav-container.scrolled .nav-link-item,
.sticky-nav-container.scrolled .nav-link-item:link,
.sticky-nav-container.scrolled .nav-link-item:visited {{
    font-size: 0.82rem !important;
}}

.nav-cta-btn {{
    background: #FFFFFF;
    color: #09090B;
    font-weight: 700;
    font-size: 0.86rem;
    padding: 9px 20px;
    border-radius: 9999px;
    text-decoration: none;
    display: inline-flex;
    align-items: center;
    gap: 6px;
    box-shadow: 0 2px 10px rgba(255, 255, 255, 0.25);
    transition: all 0.3s ease;
}}

.sticky-nav-container.scrolled .nav-cta-btn {{
    padding: 5px 14px;
    font-size: 0.76rem;
}}
</style>

<script>
(function() {{
    function mountNavToApp() {{
        const navContainer = document.getElementById('snap-nav-wrapper');
        if (!navContainer) return;
        
        // Move nav container directly under .stApp or body so position: fixed works relative to screen
        const target = document.querySelector('.stApp') || document.body;
        if (navContainer.parentElement !== target) {{
            target.appendChild(navContainer);
        }}
        
        const mainSec = document.querySelector('section.main') || document.querySelector('.stApp') || window;
        const scrollY = mainSec.scrollTop || window.scrollY || document.documentElement.scrollTop || 0;
        
        if (scrollY > 20) {{
            navContainer.classList.add('scrolled');
        }} else {{
            navContainer.classList.remove('scrolled');
        }}
    }}

    mountNavToApp();
    setInterval(mountNavToApp, 150);

    function onScrollHandler() {{
        const navContainer = document.getElementById('snap-nav-wrapper');
        if (!navContainer) return;
        const mainSec = document.querySelector('section.main') || document.querySelector('.stApp');
        const scrollY = (mainSec ? mainSec.scrollTop : 0) || window.scrollY || document.documentElement.scrollTop || 0;
        if (scrollY > 20) {{
            navContainer.classList.add('scrolled');
        }} else {{
            navContainer.classList.remove('scrolled');
        }}
    }}

    window.addEventListener('scroll', onScrollHandler, {{ passive: true }});
    document.addEventListener('scroll', onScrollHandler, {{ passive: true }});
    setTimeout(function() {{
        const mainSec = document.querySelector('section.main') || document.querySelector('.stApp');
        if (mainSec) mainSec.addEventListener('scroll', onScrollHandler, {{ passive: true }});
    }}, 500);
}})();
</script>
""")

    # ==========================================
    # 2. HERO SECTION (Reference Image 1)
    # ==========================================
    hero_container = st.container()
    with hero_container:
        # Center Hero Content
        render_html("""
<div id="hero" style="text-align: center; margin-top: 4.5rem;">
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

        # Two Portal Cards (Teacher & Student)
        st.markdown("<div id='get-started' style='margin-top: 1.25rem;'></div>", unsafe_allow_html=True)
        btn_c1, btn_c2 = st.columns(2, gap="medium")
        
        teacher_banner_html = f'<img src="{jiraya_img}" style="width: 100%; height: 300px; object-fit: cover; object-position: center top;" />' if jiraya_img else '<div style="background: #EC4899; color: #FFFFFF; width: 100%; height: 300px; display: flex; align-items: center; justify-content: center; font-size: 4rem;">👨‍🏫</div>'
        student_banner_html = f'<img src="{naruto_img}" style="width: 100%; height: 300px; object-fit: cover; object-position: center top;" />' if naruto_img else '<div style="background: #4F46E5; color: #FFFFFF; width: 100%; height: 300px; display: flex; align-items: center; justify-content: center; font-size: 4rem;">🎓</div>'

        with btn_c1:
            render_html(f"""
<div style="background: #FFFFFF; border: 1px solid #E4E4E7; border-radius: 1.25rem; overflow: hidden; box-shadow: 0 10px 25px -5px rgba(0,0,0,0.04); text-align: center; height: 100%; display: flex; flex-direction: column; justify-content: space-between;">
<div style="width: 100%; height: 300px; background: #F4F4F5; overflow: hidden;">
{teacher_banner_html}
</div>
<div style="padding: 1.25rem; display: flex; flex-direction: column; justify-content: space-between; flex-grow: 1;">
<div>
<div style="font-family: 'Syne', sans-serif; font-weight: 800; font-size: 1.25rem; color: #09090B; margin-bottom: 0.2rem;">Teacher Portal</div>
<div style="font-size: 0.78rem; color: #71717A; margin-bottom: 0.6rem;">Manage subjects & AI rosters</div>
<p style="font-size: 0.84rem; color: #52525B; line-height: 1.5; margin: 0;">
Create courses, run multi-face AI analysis, and share class codes.
</p>
</div>
<a href="?role=teacher" target="_self" style="display: block; width: 100%; padding: 0.75rem 1rem; background: #09090B; color: #FFFFFF; font-weight: 700; font-size: 0.88rem; text-align: center; border-radius: 9999px; text-decoration: none; margin-top: 1.25rem; box-shadow: 0 4px 12px rgba(0,0,0,0.12);">
Start as Teacher &rsaquo;
</a>
</div>
</div>
""")

        with btn_c2:
            render_html(f"""
<div style="background: #FFFFFF; border: 1px solid #E4E4E7; border-radius: 1.25rem; overflow: hidden; box-shadow: 0 10px 25px -5px rgba(0,0,0,0.04); text-align: center; height: 100%; display: flex; flex-direction: column; justify-content: space-between;">
<div style="width: 100%; height: 300px; background: #F4F4F5; overflow: hidden;">
{student_banner_html}
</div>
<div style="padding: 1.25rem; display: flex; flex-direction: column; justify-content: space-between; flex-grow: 1;">
<div>
<div style="font-family: 'Syne', sans-serif; font-weight: 800; font-size: 1.25rem; color: #09090B; margin-bottom: 0.2rem;">Student Portal</div>
<div style="font-size: 0.78rem; color: #71717A; margin-bottom: 0.6rem;">FaceID login & attendance stats</div>
<p style="font-size: 0.84rem; color: #52525B; line-height: 1.5; margin: 0;">
Login with 1-click FaceID scan, enroll via QR, and track records.
</p>
</div>
<a href="?role=student" target="_self" style="display: block; width: 100%; padding: 0.75rem 1rem; background: #09090B; color: #FFFFFF; font-weight: 700; font-size: 0.88rem; text-align: center; border-radius: 9999px; text-decoration: none; margin-top: 1.25rem; box-shadow: 0 4px 12px rgba(0,0,0,0.12);">
Enter as Student &rsaquo;
</a>
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