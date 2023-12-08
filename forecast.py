import streamlit as st
import plotly.express as px
from backn import get_data
st.title("Weather Forecast for the Next Days")
place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5, help="Select how many days of forecast you need.")
option = st.selectbox("Select data to view", ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place.title()}")

data = get_data(place, days, option)


figure = px.line(x=d, y=t, labels={"x": "Date", "y": "Temperatures (C)"})
st.plotly_chart(figure)