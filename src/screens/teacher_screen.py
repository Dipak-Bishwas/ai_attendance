import streamlit as st

from src.ui.base_layout import style_background_dashboard, style_base_layout

from src.components.header import header_dashboard
from src.components.footer import footer_dashboard
from src.components.subject_card import subject_card
from src.database.db import check_teacher_exists, create_teacher, teacher_login, get_teacher_subjects, get_attendance_for_teacher
from src.components.dialog_create_subject import create_subject_dialog
from src.components.dialog_share_subject import share_subject_dialog
from src.components.dialog_add_photo import add_photos_dialog

from src.pipelines.face_pipeline import predict_attendance
from src.components.dialog_attendance_results import attendance_result_dialog
import numpy as np

from datetime import datetime

import pandas as pd

from src.database.config import supabase


from src.components.dialog_voice_attendance import voice_attendance_dialog
def teacher_screen():

    style_background_dashboard()
    style_base_layout()

    if "teacher_data" in st.session_state:
        teacher_dashboard()
    elif 'teacher_login_type' not in st.session_state or st.session_state.teacher_login_type=="login":
        teacher_screen_login()
    elif st.session_state.teacher_login_type == "register":
        teacher_screen_register()





def teacher_dashboard():
    teacher_data = st.session_state.teacher_data
    c1, c2 = st.columns([1.2, 1.8], vertical_alignment='center')
    with c1:
        header_dashboard()
    with c2:
        st.markdown(f"""
            <div style="display: flex; flex-direction: column; align-items: flex-end; justify-content: center; gap: 8px;">
                <div style="font-family: 'Inter', -apple-system, sans-serif; font-size: 1.45rem; font-weight: 800; color: #09090B; letter-spacing: -0.02em;">
                    Welcome, {teacher_data.get('name', 'Teacher')}!
                </div>
            </div>
        """, unsafe_allow_html=True)
        col_dummy, col_logout = st.columns([1.5, 1])
        with col_logout:
            if st.button("Logout ⌘+L", type='primary', key='loginbackbtn', shortcut="control+shift+l", width='stretch'):
                st.session_state['is_logged_in'] = False
                del st.session_state.teacher_data 
                st.rerun()

    st.markdown('<div style="height: 1.25rem;"></div>', unsafe_allow_html=True)

    if "current_teacher_tab" not in st.session_state:
        st.session_state.current_teacher_tab = 'take_attendance'

    st.markdown('<div class="snap-nav-tabs">', unsafe_allow_html=True)
    tab1, tab2, tab3 = st.columns(3, gap="medium")

    with tab1:
        type1 = "primary" if st.session_state.current_teacher_tab == 'take_attendance' else "tertiary"
        if st.button('Take Attendance', type=type1, width='stretch', icon=':material/ar_on_you:', key='tab_btn_take_attendance'):
            st.session_state.current_teacher_tab = 'take_attendance'
            st.rerun()

    with tab2:
        type2 = "primary" if st.session_state.current_teacher_tab == 'manage_subjects' else "tertiary"
        if st.button('Manage Subjects', type=type2, width='stretch', icon=':material/book_ribbon:', key='tab_btn_manage_subjects'):
            st.session_state.current_teacher_tab = 'manage_subjects'
            st.rerun()

    with tab3:
        type3 = "primary" if st.session_state.current_teacher_tab == 'attendance_records' else "tertiary"
        if st.button('Attendance Records', type=type3, width='stretch', icon=':material/cards_stack:', key='tab_btn_attendance_records'):
            st.session_state.current_teacher_tab = 'attendance_records'
            st.rerun()

    st.divider()

    if st.session_state.current_teacher_tab == "take_attendance":
        teacher_tab_take_attendance()
    elif st.session_state.current_teacher_tab == "manage_subjects":
        teacher_tab_manage_subjects()
    elif st.session_state.current_teacher_tab == "attendance_records":
        teacher_tab_attendance_records()

    footer_dashboard()


def teacher_tab_take_attendance():
    teacher_id = st.session_state.teacher_data['teacher_id']
    st.markdown("""
        <h1 class="snap-retro-title" style="font-size: 2.2rem; margin: 0.25rem 0 1.25rem 0;">
            Take AI Attendance
        </h1>
    """, unsafe_allow_html=True)

    if 'attendance_images' not in st.session_state:
        st.session_state.attendance_images = []

    subjects = get_teacher_subjects(teacher_id)

    if not subjects:
        st.info('You haven\'t created any subjects yet! Click the "Manage Subjects" tab above to create your first subject.')
        return
    
    subject_options = {f"{s['name']} - {s['subject_code']}": s['subject_id'] for s in subjects}
    subject_map = {f"{s['name']} - {s['subject_code']}": s for s in subjects}

    col1, col2, col3 = st.columns([2.5, 1, 1], vertical_alignment='bottom', gap='medium')

    with col1:
        selected_subject_label = st.selectbox('Select Subject', options=list(subject_options.keys()))

    with col2:
        if st.button('Add Photos', type='tertiary', icon=':material/photo_prints:', width='stretch'):
            add_photos_dialog()

    with col3:
        current_sub_data = subject_map[selected_subject_label]
        if st.button('Share Code', type='primary', icon=':material/share:', width='stretch', key='share_from_take_att'):
            share_subject_dialog(current_sub_data['name'], current_sub_data['subject_code'])

    selected_subject_id = subject_options[selected_subject_label]

    if st.session_state.attendance_images:
        st.markdown('<h3 style="font-size: 1.3rem; font-weight: 700; margin: 1.5rem 0 1rem 0;">Added Photos</h3>', unsafe_allow_html=True)
        gallery_cols = st.columns(4, gap="medium")

        for idx, img in enumerate(st.session_state.attendance_images):
            with gallery_cols[idx % 4]:
                st.image(img, width='stretch', caption=f'Photo {idx+1}')

    has_photos = bool(st.session_state.attendance_images)
    
    if not has_photos:
        st.info("📷 Please click **Add Photos** above to upload classroom photos first. Once photos are added, **Run Face Analysis** and **Clear all photos** will become active.")

    c1, c2, c3 = st.columns(3, gap="medium")

    with c1:
        if st.button('Clear all photos', width='stretch', type='secondary', icon=':material/delete:', disabled=not has_photos):
            st.session_state.attendance_images = []
            st.rerun()

    with c2:
        if st.button('Run Face Analysis', width='stretch', type='secondary', icon=':material/analytics:', disabled=not has_photos):
            with st.spinner('Deep scanning classroom photos...'):
                all_detected_ids = {}

                for idx, img in enumerate(st.session_state.attendance_images):
                    img_np = np.array(img.convert('RGB'))
                    detected, _, _ = predict_attendance(img_np)

                    if detected:
                        for sid in detected.keys():
                            student_id = int(sid)
                            all_detected_ids.setdefault(student_id, []).append(f"Photo {idx+1}")

                enrolled_res = supabase.table('subject_students').select("*, students(*)").eq('subject_id', selected_subject_id).execute()
                enrolled_students = enrolled_res.data

                if not enrolled_students:
                    st.warning('No students enrolled in this course')
                else:
                    results, attendance_to_log = [], []
                    current_timestamp = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")

                    for node in enrolled_students:
                        student = node['students']
                        sources = all_detected_ids.get(int(student['student_id']), [])
                        is_present = len(sources) > 0

                        results.append({
                            "Name": student['name'],
                            "ID": student['student_id'],
                            "Source": ", ".join(sources) if is_present else "-",
                            "Status": "✅ Present" if is_present else "❌ Absent"
                        })

                        attendance_to_log.append({
                            'student_id': student['student_id'],
                            'subject_id': selected_subject_id,
                            'timestamp': current_timestamp,
                            'is_present': bool(is_present)
                        })

                    attendance_result_dialog(pd.DataFrame(results), attendance_to_log)

    with c3:
        if st.button('Use Voice Attendance', type='tertiary', width='stretch', icon=':material/mic:'):
            voice_attendance_dialog(selected_subject_id)


def teacher_tab_manage_subjects():
    teacher_id = st.session_state.teacher_data['teacher_id']
    col1, col2 = st.columns([1.2, 1], vertical_alignment='center')
    with col1:
        st.markdown("""
            <h1 class="snap-retro-title" style="font-size: 2.2rem; margin: 0.25rem 0 1rem 0;">
                Manage<br/>subjects
            </h1>
        """, unsafe_allow_html=True)

    with col2:
        if st.button('Create New Subject', type='primary', width='stretch', key='btn_create_subject'):
            create_subject_dialog(teacher_id)

    # LIST all SUBJECTS
    subjects = get_teacher_subjects(teacher_id)
    if subjects:
        for sub in subjects:
            stats = [
                ("👥", "Students", sub.get('total_students', 0)),
                ("📅", "Classes Held", sub.get('total_classes', 0)),
            ]
            def make_share_callback(current_sub):
                def share_btn():
                    if st.button(f"Share Code: {current_sub['name']}", key=f"share_{current_sub['subject_code']}", icon=":material/share:", type='primary'):
                        share_subject_dialog(current_sub['name'], current_sub['subject_code'])
                return share_btn

            subject_card(
                name=sub['name'],
                code=sub['subject_code'],
                section=sub['section'],
                stats=stats,
                footer_callback=make_share_callback(sub)
            )
    else:
        st.info("No subjects found. Click 'Create New Subject' above to add your first course.")


def teacher_tab_attendance_records():
    st.markdown("""
        <h1 class="snap-retro-title" style="font-size: 2.2rem; margin: 0.25rem 0 1.25rem 0;">
            Attendance Records
        </h1>
    """, unsafe_allow_html=True)

    teacher_id = st.session_state.teacher_data['teacher_id']
    records = get_attendance_for_teacher(teacher_id)

    if not records:
        st.info("No attendance records found yet.")
        return
    
    data = []
    for r in records:
        ts = r.get('timestamp')
        data.append({
            "ts_group": ts.split(".")[0] if ts else None,
            "Time": datetime.fromisoformat(ts).strftime("%Y-%m-%d %I:%M %p") if ts else "N/A",
            "Subject": r['subjects']['name'],
            "Subject Code": r['subjects']['subject_code'],
            "is_present": bool(r.get('is_present', False))
        })

    df = pd.DataFrame(data)

    summary = (
        df.groupby(['ts_group', 'Time', 'Subject', 'Subject Code'])
        .agg(
            Present_Count=('is_present', 'sum'),
            Total_Count=('is_present', 'count')
        ).reset_index()
    )

    summary['Attendance Stats'] = (
        "✅ " + summary['Present_Count'].astype(str) + " / "
        + summary['Total_Count'].astype(str) + ' Students'
    )

    display_df = (
        summary.sort_values(by='ts_group', ascending=False)
        [['Time', 'Subject', 'Subject Code', 'Attendance Stats']]
    )
    
    st.markdown('<div class="white-card">', unsafe_allow_html=True)
    st.dataframe(display_df, width='stretch', hide_index=True)
    st.markdown('</div>', unsafe_allow_html=True)


def login_teacher(username, password):
    if not username or not password:
        return False, "Username and password cannot be empty."
    
    try:
        teacher = teacher_login(username, password)
        if teacher:
            st.session_state.user_role = 'teacher'
            st.session_state.teacher_data = teacher
            st.session_state.is_logged_in = True
            return True, "Success"
        return False, "Invalid username or password."
    except Exception as e:
        return False, f"Could not connect to Supabase database. Please check your internet connection or .streamlit/secrets.toml settings. ({str(e)})"


def teacher_screen_login():
    c1, c2 = st.columns([1.5, 1], vertical_alignment='center')
    with c1:
        header_dashboard()
    
    st.markdown('<div style="height: 1.5rem;"></div>', unsafe_allow_html=True)
    
    st.markdown("""
        <div class="white-card" style="max-width: 500px; margin: 0 auto; padding: 2.25rem 2.5rem;">
            <h2 style="font-family: 'Inter', sans-serif; font-weight: 800; font-size: 1.6rem; color: #09090B; margin: 0 0 1.5rem 0; text-align: center; letter-spacing: -0.02em;">
                Teacher Login
            </h2>
    """, unsafe_allow_html=True)

    teacher_username = st.text_input("Username", placeholder='e.g. ananyaroy')
    teacher_pass = st.text_input("Password", type='password', placeholder="Enter password")

    st.markdown('<div style="height: 1rem;"></div>', unsafe_allow_html=True)

    btnc1, btnc2 = st.columns(2, gap="small")

    with btnc1:
        st.markdown('<div class="pink-pill-btn">', unsafe_allow_html=True)
        if st.button('Login', icon=':material/passkey:', shortcut='control+enter', width='stretch'):
            success, message = login_teacher(teacher_username, teacher_pass)
            if success:
                st.toast("Welcome back!", icon="👋")
                import time
                time.sleep(0.5)
                st.rerun()
            else:
                st.error(message)
        st.markdown('</div>', unsafe_allow_html=True)

    with btnc2:
        if st.button('Register Instead', type="secondary", icon=':material/person_add:', width='stretch'):
            st.session_state.teacher_login_type = 'register'
            st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)

    footer_dashboard()


def register_teacher(teacher_username, teacher_name, teacher_pass, teacher_pass_confirm):
    if not teacher_username or not teacher_name or not teacher_pass:
        return False, "All Fields are required!"
    if teacher_pass != teacher_pass_confirm:
        return False, "Passwords do not match!"
    
    try:
        if check_teacher_exists(teacher_username):
            return False, "Username already taken!"
        create_teacher(teacher_username, teacher_pass, teacher_name)
        return True, "Successfully Created! Login Now"
    except Exception as e:
        return False, f"Database connection error: {str(e)}"
    

def teacher_screen_register():
    c1, c2 = st.columns([1.5, 1], vertical_alignment='center')
    with c1:
        header_dashboard()

    st.markdown('<div style="height: 1.5rem;"></div>', unsafe_allow_html=True)

    st.markdown("""
        <div class="white-card" style="max-width: 500px; margin: 0 auto; padding: 2.25rem 2.5rem;">
            <h2 style="font-family: 'Inter', sans-serif; font-weight: 800; font-size: 1.6rem; color: #09090B; margin: 0 0 1.5rem 0; text-align: center; letter-spacing: -0.02em;">
                Create Teacher Account
            </h2>
    """, unsafe_allow_html=True)
    
    teacher_username = st.text_input("Username (Used for logging in)", placeholder='e.g. ananyaroy')
    teacher_name = st.text_input("Full Name (Display name)", placeholder='e.g. Prof. Ananya Roy')
    teacher_pass = st.text_input("Password", type='password', placeholder="Enter password")
    teacher_pass_confirm = st.text_input("Confirm password", type='password', placeholder="Re-enter password")

    st.markdown('<div style="height: 1rem;"></div>', unsafe_allow_html=True)

    btnc1, btnc2 = st.columns(2, gap="small")

    with btnc1:
        st.markdown('<div class="pink-pill-btn">', unsafe_allow_html=True)
        if st.button('Register Now', icon=':material/passkey:', shortcut='control+enter', width='stretch'):
            success, message = register_teacher(teacher_username, teacher_name, teacher_pass, teacher_pass_confirm)
            if success:
                st.success(message)
                import time
                time.sleep(1)
                st.session_state.teacher_login_type = "login"
                st.rerun()
            else:
                st.error(message)
        st.markdown('</div>', unsafe_allow_html=True)

    with btnc2:
        if st.button('Login Instead', type="secondary", icon=':material/login:', width='stretch'):
            st.session_state.teacher_login_type = 'login'
            st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)

    footer_dashboard()