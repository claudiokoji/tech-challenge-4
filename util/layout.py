import streamlit as st
from st_pages import show_pages, Page
import locale

from util.constantes import TITULO_ANALISE_EXPLORATORIA, TITULO_HISTORIA, TITULO_MODELO

def format_number(number, format='%0.0f'):
    return locale.format(format, number, grouping=True)

def output_layout():
    show_pages(
        [
            Page("./main.py", "Tech Challenge 4", ":house:", use_relative_hash=True),
            Page("./pages/historia.py", TITULO_HISTORIA, ":open_book:", use_relative_hash=True),
            Page(
                "./pages/analise.py",
                TITULO_ANALISE_EXPLORATORIA,
                ":memo:",
                use_relative_hash=True,
            ),
            Page("./pages/modelo.py", TITULO_MODELO, ":robot_face:", use_relative_hash=True),
            
        ]
    )

    with st.sidebar:
        st.subheader("Alunos do Grupo")
        st.text("Bruno Siqueira | RM 351907")
        st.text("Claudio Koji   | RM 352492")
        st.text("Matheus Lima   | RM 430056")
        st.text("Luana Luz      | RM 353101")
        st.text("Nelson Walcow  | RM 352984")

        st.divider()

        st.subheader("Repositórios do projeto")
        st.link_button(
            "Repositório Streamlit",
            "https://github.com/claudiokoji/tech-challenge-4",
            help=None,
            type="secondary",
            disabled=False,
            use_container_width=False,
        )