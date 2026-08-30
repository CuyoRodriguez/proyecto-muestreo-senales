from pathlib import Path

import streamlit as st


def cargar_css() -> None:
    css_path = Path(__file__).resolve().parent / "assets" / "styles" / "style.css"
    if css_path.exists():
        css = css_path.read_text(encoding="utf-8")
        st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)


cargar_css()

st.set_page_config(
    page_title="Proyecto base",
    page_icon="📘",
    layout="wide",
)

st.title("Proyecto base")
st.caption("Aplicación educativa en desarrollo.")

st.markdown(
    """
    <div class="card">
        <h3>Base visual preparada</h3>
        <p>La estructura está lista para continuar con la lógica del ejercicio y la interfaz final.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

with st.container():
    st.markdown(
        """
        <div class="section-box">
            <h4>Estado actual</h4>
            <p>Esta versión solo prepara la base visual del proyecto y mantiene la lógica matemática separada en <strong>src</strong>.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
