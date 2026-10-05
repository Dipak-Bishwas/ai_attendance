import streamlit as st
import segno
import io


@st.dialog("Share Class Link")
def share_subject_dialog(subject_name, subject_code):
    # Valid join URL with protocol so it opens correctly
    join_url = f"http://localhost:8501/?join-code={subject_code}"

    qr = segno.make(join_url)
    out = io.BytesIO()
    qr.save(out, kind='png', scale=10, border=1)

    st.markdown(f"### {subject_name}")
    col1, col2 = st.columns([1.2, 1], gap="medium")

    with col1:
        st.markdown('**Direct Join Link**')
        st.code(join_url, language="text")
        
        st.markdown('**Class Code**')
        st.code(subject_code, language="text")
        st.info('Share this link or code with students to auto-enroll them.')

    with col2:
        st.markdown('**Scan to Join**')
        st.image(out.getvalue(), caption=f'QR Code for {subject_code}')

        
