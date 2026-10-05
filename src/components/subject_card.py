import textwrap
import streamlit as st


def subject_card(name, code, section, stats=None, footer_callback=None):
    stats_html = ""
    if stats:
        items_html = ""
        for icon, label, value in stats:
            bg_color = "#EEF2FF" if "Student" in label else "#FEE2E2"
            text_color = "#3730A3" if "Student" in label else "#991B1B"
            items_html += f"""<div style="background: {bg_color}; padding: 5px 12px; border-radius: 8px; font-size: 0.82rem; font-weight: 600; color: {text_color}; display: inline-flex; align-items: center; gap: 6px;"><span>{icon}</span><span>{value}</span><span>{label}</span></div>"""
        stats_html = f"""<div style="display: flex; gap: 10px; flex-wrap: wrap; margin-top: 1rem;">{items_html}</div>"""

    card_html = textwrap.dedent(f"""
        <div style="background: #FFFFFF; border-radius: 1.5rem; padding: 1.6rem 1.85rem; box-shadow: 0 4px 20px rgba(0, 0, 0, 0.03); margin-bottom: 0.85rem;">
            <h3 style="margin: 0 0 0.5rem 0; color: #09090B; font-size: 1.3rem; font-weight: 700; letter-spacing: -0.01em;">{name}</h3>
            <div style="display: flex; align-items: center; gap: 8px; font-size: 0.88rem; color: #64748B;">
                <span>Code:</span>
                <span style="background: #E0E7FF; color: #4338CA; font-weight: 700; font-size: 0.82rem; padding: 2px 8px; border-radius: 6px; letter-spacing: 0.02em;">{code}</span>
                <span style="color: #94A3B8;">|</span>
                <span>Section: <strong style="color: #0F172A;">{section}</strong></span>
            </div>
            {stats_html}
        </div>
    """).strip()

    st.markdown(card_html, unsafe_allow_html=True)

    if footer_callback:
        st.markdown('<div class="pink-pill-btn" style="max-width: 360px; margin-bottom: 1.5rem;">', unsafe_allow_html=True)
        footer_callback()
        st.markdown('</div>', unsafe_allow_html=True)

