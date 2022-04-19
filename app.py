import time
import requests
import streamlit as st
import webbrowser

st.header("What to.. Where to .. What type of ... ? ")

insight = 'https://share.streamlit.io/pgstorm148/tac-traffic-v1/main/tac_app.py'
poc = 'https://github.com/pgstorm148/eda-traffic/tree/main/eda-traffic'

if st.button('Insights'):
    webbrowser.open_new_tab(insight)

if st.button('EDA - traffic'):
    webbrowser.open_new_tab(poc)
