import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="ALAMAT"
)

#### you may edit here onwards ###

st.title("Alamat")

image = Image.open("logo.webp")
st.image(image, caption="Alamat, Handa 'Rap.",width=None)

st.write("**Alamat** is a multi-ethnic and multilingual Filipino boy group that was formed in 2020 under the management of Viva Records. The group consists of six members, namely: Taneo, Mo, Tomas, Jao, R-Ji, and Alas.")

image1 = Image.open("members.jpeg")
st.image(image1, caption="Members in Costume with Filipino Flair.", use_column_width=True)

st.write("Their name *Alamat* is the Tagalog word for legend, and their mission is to become a legendary group that showcase their unique style and talent, as well as their pride in their Filipino heritage. They made their debut with the single 'kbye' last February 14, 2021. ")

image2 = Image.open("discog.png")
st.image(image2, caption="Top 5 Tracks in Spotify based on streams.", use_column_width=True)

image3 = Image.open("awards.png")
st.image(image3, caption="Awards and Recognitions of Alamat.", use_column_width=True)

st.write("Since then, they have garnered many awards and recognitions from different competitions. But still, it doesn’t translate to their number of followers and listeners.")

# Display a video with a caption using Streamlit
video_file = open('stats.mp4', 'rb')
video_bytes = video_file.read()
st.video(video_bytes)

st.write("With this slight problem at hand, we want to make Alamat belong in the Top 200 Daily Spotify Charts for PH by:")

st.write("""
1. Extend their audience reach 
2. Specify best months to release new single 
3. Recommend best future collaborations
""")

