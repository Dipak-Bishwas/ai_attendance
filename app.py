import sys
from pathlib import Path

# Ensure local project modules are prioritized
PROJECT_ROOT = Path(__file__).resolve().parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

import streamlit as st

from src.screens.home_screen import home_screen
from src.screens.teacher_screen import teacher_screen
from src.screens.student_screen import student_screen

from src.components.dialog_auto_enroll import auto_enroll_dialog


def main():
    st.set_page_config(
        page_title='SnapClass - Making Attendance faster using AI',
        page_icon="https://i.ibb.co/YTYGn5qV/logo.png"
    )

    # Sync browser URL query params with login_type for browser back/forward support
    url_role = st.query_params.get('role')
    if url_role in ['teacher', 'student']:
        st.session_state['login_type'] = url_role
    elif url_role is None:
        st.session_state['login_type'] = None

    match st.session_state.get('login_type'):
        case 'teacher':
            teacher_screen()

        case 'student':
            student_screen()

        case _:
            home_screen()

    join_code = st.query_params.get('join-code')
    if join_code:
        if st.session_state.get('login_type') != 'student':
            st.session_state['login_type'] = 'student'
            st.query_params['role'] = 'student'
            st.rerun()
        if st.session_state.get('is_logged_in') and st.session_state.get('user_role') == 'student':
            auto_enroll_dialog(join_code)


if __name__ == '__main__':
    main()