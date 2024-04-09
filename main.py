import requests
import streamlit as st

api_key = "kO5DBJBV7BQfF6kAnxiY0GAwPqCg7u0xFgvjQRxH"
url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"

# Request NASA for picture of the day, and title and save in image.jpg
request = requests.get(url)
content = request.json()
title_of_the_day = content["title"]
explanation = content["explanation"]
pic_url = content["url"]
pic_bytes = requests.get(pic_url)
with open("image.jpg", "wb") as file:
    file.write(pic_bytes.content)

# Start rendering webpage
# Display Title
st.header(title_of_the_day)

# Display Picture
st.image("image.jpg")

# Display Description
st.write(explanation)