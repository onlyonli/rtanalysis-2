import time
import requests
import streamlit as st
import webbrowser
from bokeh.models.widgets import Div

st.header("What to.. Where to .. What type of ... ? ")

insight = 'https://share.streamlit.io/pgstorm148/tac-traffic-v1/main/tac_app.py'
poc = 'https://github.com/pgstorm148/eda-traffic/tree/main/eda-traffic'

if st.button('Insights'):
    js = "window.open('https://share.streamlit.io/pgstorm148/tac-traffic-v1/main/tac_app.py')"  # New tab or window
    js = "window.location.href = 'https://www.streamlit.io/'"  # Current tab
    html = '<img src onerror="{}">'.format(js)
    div = Div(text=html)
    st.bokeh_chart(div)
    

if st.button('EDA - traffic'):
    webbrowser.open_new_tab(poc)
