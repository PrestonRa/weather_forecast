import streamlit as st
import plotly.express as px
from backn import get_data

st.title("Weather Forecast")
place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5, help="Select how many days of forecast you need.")
option = st.selectbox("Select data to view", ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place.title()}")

try:
    if place:

        filtered_data = get_data(place, days)

        if option == "Temperature":
            temperatures = [float(dict["main"]["temp"]) / 10 for dict in filtered_data]
            print(temperatures)
            dates = [dict["dt_txt"] for dict in filtered_data]
            figure = px.line(x=dates, y=temperatures, labels={"x": "Date", "y": "Temperatures (C)"})
            st.plotly_chart(figure)

        if option == "Sky":
            images = {"Clear": "images/clear.png", "Clouds": "images/cloud.png",
                      "Rain": "images/rain.png", "Snow": "images/snow.png"}
            sky_conditions = [dict["weather"][0]["main"] for dict in filtered_data]
            image_paths = [images[condition] for condition in sky_conditions]
            st.image(image_paths, width=115)

except KeyError:
        st.subheader(f'...Sorry, it seems that "{place}" is not a city or country, please double check.')
