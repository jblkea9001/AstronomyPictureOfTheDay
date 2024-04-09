import requests
import streamlit as st

api_key = "kO5DBJBV7BQfF6kAnxiY0GAwPqCg7u0xFgvjQRxH"
url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"

# Get the request data as a dictionary
request = requests.get(url)
content = request.json()

# Extract the image url, title and explanation
title_of_the_day = content["title"]
explanation = content["explanation"]
pic_url = content["url"]

# Download the image and save in image.jpg
pic_bytes = requests.get(pic_url)
with open("image.png", "wb") as file:
    file.write(pic_bytes.content)

# Start rendering webpage
# Display Title
st.title(title_of_the_day)

# Display Picture
st.image("image.png")

# Display Description
st.write(explanation)