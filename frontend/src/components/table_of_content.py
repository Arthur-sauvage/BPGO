""" Table of Content generator for Streamlit """

import streamlit as st
import re


class ToC:
    def __init__(self, numero_client):
        self._items = [
            "### DéménageFacile Express",
            "### Secteur : Déménagement",
            "#### Dernier RDV : 28/11/23",
            "#### Prochain RDV : 18/05/24",
            "---",
        ]
        self._placeholder = None

    def title(self, text):
        self._markdown(text, "h1")

    def header(self, text):
        self._markdown(text, "h2", " " * 2)

    def subheader(self, text):
        self._markdown(text, "h3", " " * 4)

    def generate(self):
        st.sidebar.markdown("\n".join(self._items), unsafe_allow_html=True)

    def _markdown(self, text, level, space=""):
        key = re.sub(
            "[^0-9a-zA-Z]+",
            "-",
            text.replace("é", "e").replace("è", "e").replace(" et Questions", ""),
        ).lower()

        if level == "h1":
            st.markdown(
                f"""<div style ="background-color:white"> <h3 id='{key}' style ="color:white;text-align:center;">{key}</h3>""",
                unsafe_allow_html=True,
            )
            st.markdown(
                f"""<div style ="background-color:#1E70AA"> <{level} style ="color:white;text-align:center;">{text}</{level}>""",
                unsafe_allow_html=True,
            )
        else:
            st.markdown(f"<{level} id='{key}'>{text}</{level}>", unsafe_allow_html=True)

        if text == "Dashboard":
            self._items.append("### ")
            self._items.append(f"<a href='#{key}'>{text}</a>")
        else:
            self._items.append(f"{space}* <a href='#{key}'>{text}</a>")
