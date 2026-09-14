import streamlit as st


def subject_card(name, code, section, stats=None, footer_callback=None):
    html = f"""
        <div style="background: #FFFFFF; border-left: 5px solid #4F46E5; padding: 1.5rem; border-radius: 1rem; border-top: 1px solid #E2E8F0; border-right: 1px solid #E2E8F0; border-bottom: 1px solid #E2E8F0; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.04), 0 2px 4px -2px rgba(0, 0, 0, 0.02); margin-bottom: 1.25rem;">
            <div style="display: flex; justify-content: space-between; align-items: flex-start; gap: 10px;">
                <h3 style="margin: 0; color: #0F172A; font-size: 1.25rem; font-weight: 700; line-height: 1.3;">{name}</h3>
                <span style="background: #EEF2FF; color: #4338CA; font-weight: 700; font-size: 0.75rem; padding: 3px 8px; border-radius: 6px; letter-spacing: 0.04em;">{code}</span>
            </div>
            <p style="color: #64748B; font-size: 0.88rem; margin: 0.4rem 0 1rem 0;">Section: <strong style="color: #334155;">{section}</strong></p>
    """

    if stats:
        html += '<div style="display: flex; gap: 8px; flex-wrap: wrap; margin-bottom: 0.5rem;">'
        for icon, label, value in stats:
            html += f"""
                <div style="background: #F8FAFC; border: 1px solid #E2E8F0; padding: 6px 12px; border-radius: 8px; font-size: 0.82rem; color: #334155; display: inline-flex; align-items: center; gap: 5px;">
                    <span>{icon}</span>
                    <strong style="color: #0F172A;">{value}</strong>
                    <span style="color: #64748B;">{label}</span>
                </div>
            """
        html += "</div>"

    html += "</div>"

    st.markdown(html, unsafe_allow_html=True)

    if footer_callback:
        footer_callback()
