import streamlit as st
import pandas as pd
import altair as alt
import plotly.express as px

st.set_page_config(
    page_title='BR Population Dashboard',
    page_icon='',
    layout='wide',
    initial_sidebar_state='collapsed')

alt.themes.enable('dark')

