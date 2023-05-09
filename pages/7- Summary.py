import streamlit as st

st.set_page_config(
    page_title="ALAMAT"
)

#### you may edit here onwards ###

st.title("Summary of Recommendations")
st.subheader("Alamat can rise locally and internationally while trusting their proud Filipino brand by applying these strategies:")
st.image('alamat2.jpg')

#1.
st.subheader("1. Adopt track features and practices of Leading K-Pop and P-pop groups")

st.markdown(":arrow_up: increase danceability")
st.markdown(":arrow_up: increase energy")
st.markdown(":arrow_down: decrease key")
st.markdown(":arrow_up: increase speechiness")

st.markdown(":arrow_up: increase number of tracks released per year")

st.markdown(":earth_americas: release English version of original songs to tap global market")

#2.
st.subheader("2. Timeline of releases")
st.markdown("Data of leading artists show that K-Pop and P-pop streams rise at the 3rd Quarter of the year. Alamat can optimize this timeline and join the hype")

#3.
st.subheader("3. Collaborate with artists of both similar and opposite genre")
st.image('collab.JPG')

#4.
st.subheader("4. Other Strategies")
st.markdown(":headphones: maximize benefits of playlists")
st.markdown(":movie_camera: tap OST market")
st.markdown(":notes: upload different versions of songs")
st.markdown(":raised_hands: collaborate music with influencers")

#playlists
st.subheader("Enjoy Alamat and other tracks below. Happy Listening!")

#embed playlist--------------
#PPop-------------------------------

# Define the Spotify playlist URI
spotify_uri="spotify:playlist:4aDh9tss9O5ITj3PEHi6sE"

# Define the HTML code to embed the Spotify player
html_code = f'<iframe style="border-radius:12px" src="https://open.spotify.com/embed/playlist/4aDh9tss9O5ITj3PEHi6sE?utm_source=generator" width="100%" height="152" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>'

# Use the Streamlit HTML component to display the code
st.components.v1.html(html_code)

#embed playlist--------------
#INternational-------------------------------

# Define the Spotify playlist URI
spotify_uri="spotify:playlist:7stWyrrvYadpioDYjDNTi6"

# Define the HTML code to embed the Spotify player
html_code = f'<iframe style="border-radius:12px" src="https://open.spotify.com/embed/playlist/7stWyrrvYadpioDYjDNTi6?utm_source=generator" width="100%" height="152" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>'

# Use the Streamlit HTML component to display the code
st.components.v1.html(html_code)




st.subheader("_Sa pamamagitan ng musika, layunin ng ALAMAT ang ipagdiwang ang ating pagka-Pilipino at maitanim sa puso't isipan ng mga kabataang Pinoy na hindi kailangan hubarin ang ating kultura't pagkakakilanlan para lamang umangat at makilala sa pandaigdigang entablado._")
st.markdown("-Alamat's Mission Statement")