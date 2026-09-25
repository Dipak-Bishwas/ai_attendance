import streamlit as st


def subject_card(name, code, section, stats=None, footer_callback=None):
    html = f"""
        <div style="background: #FFFFFF; border-left: 4px solid #2563EB; padding: 1.25rem 1.5rem; border-radius: 0.75rem; border-top: 1px solid #E4E4E7; border-right: 1px solid #E4E4E7; border-bottom: 1px solid #E4E4E7; box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.04), 0 1px 2px -1px rgba(0, 0, 0, 0.03); margin-bottom: 1rem;">
            <div style="display: flex; justify-content: space-between; align-items: flex-start; gap: 10px;">
                <h3 style="margin: 0; color: #09090B; font-size: 1.15rem; font-weight: 700; line-height: 1.3;">{name}</h3>
                <span style="background: #EFF6FF; color: #1D4ED8; border: 1px solid #DBEAFE; font-weight: 600; font-size: 0.75rem; padding: 2px 8px; border-radius: 6px; letter-spacing: 0.03em;">{code}</span>
            </div>
            <p style="color: #71717A; font-size: 0.85rem; margin: 0.35rem 0 0.85rem 0;">Section: <strong style="color: #27272A;">{section}</strong></p>
    """

    if stats:
        html += '<div style="display: flex; gap: 8px; flex-wrap: wrap; margin-bottom: 0.5rem;">'
        for icon, label, value in stats:
            html += f"""
                <div style="background: #FAFAFA; border: 1px solid #E4E4E7; padding: 4px 10px; border-radius: 6px; font-size: 0.8rem; color: #3F3F46; display: inline-flex; align-items: center; gap: 5px;">
                    <span>{icon}</span>
                    <strong style="color: #09090B;">{value}</strong>
                    <span style="color: #71717A;">{label}</span>
                </div>
            """
        html += "</div>"

    html += "</div>"

    st.markdown(html, unsafe_allow_html=True)

    if footer_callback:
        footer_callback()
