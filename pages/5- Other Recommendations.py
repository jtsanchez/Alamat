import streamlit as st

st.set_page_config(
    page_title="ALAMAT"
)

#### you may edit here onwards ###

st.title("Other Recommendations")
st.subheader('What other strategies could Alamat implement?')

#1. Playlist
st.subheader('1. Publish songs in playlists')
st.markdown('Output attests that "When an unknown artist is featured even on a modestly followed playlist, it can bring significant exposure measured in more listeners" (2018).')

st.markdown('The sample playlists below were generated using recommender engine & selected Alamat songs as seed tracks, with pool from PH daily top 200  to attract more audience.')

#embed playlist--------------
#workout-------------------------------

# Set the text to be centered
text = "Jog to 'Hala' by Alamat in 'Your next WORKOUT playlist"

# Use st.write() and set the style parameter to center the text
st.write(f'<div style="text-align:center">{text}</div>', unsafe_allow_html=True)


# Define the Spotify playlist URI
#spotify_uri = "spotify:playlist:37i9dQZF1DWYp5yzYMBr2d"
spotify_uri="spotify:playlist:0e9WlZUwaVuFi0VcbWY1th"

# Define the HTML code to embed the Spotify player
html_code = f'<iframe style="border-radius:12px" src="https://open.spotify.com/embed/playlist/0e9WlZUwaVuFi0VcbWY1th?utm_source=generator&theme=0" width="100%" height="152" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>'

# Use the Streamlit HTML component to display the code
st.components.v1.html(html_code)


#------------------------------------------

#embed playlist--------------
#sad-------------------------------

# Set the text to be centered
text = "cry for the 'what ifs' to 'Sa Panaginip Na Lang' by Alamat in the 'sad pop songs' playlist"

# Use st.write() and set the style parameter to center the text
st.write(f'<div style="text-align:center">{text}</div>', unsafe_allow_html=True)


# Define the Spotify playlist URI
#spotify_uri = "spotify:playlist:37i9dQZF1DWYp5yzYMBr2d"
spotify_uri="spotify:playlist:7xLzIwjGaBNxwg5DQu4DBB"

# Define the HTML code to embed the Spotify player
html_code = f'<iframe style="border-radius:12px" src="https://open.spotify.com/embed/playlist/7xLzIwjGaBNxwg5DQu4DBB?utm_source=generator" width="100%" height="152" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>'

# Use the Streamlit HTML component to display the code
st.components.v1.html(html_code)


#------------------------------------------


#embed playlist--------------
#sad-------------------------------

# Set the text to be centered
text = "cheep up to 'ABKD' by Alamat in the 'motivation & good vibes' playlist"

# Use st.write() and set the style parameter to center the text
st.write(f'<div style="text-align:center">{text}</div>', unsafe_allow_html=True)


# Define the Spotify playlist URI
#spotify_uri = "spotify:playlist:37i9dQZF1DWYp5yzYMBr2d"
spotify_uri="spotify:playlist:3t3A8abTTxLVQ1fGF2AH8G"

# Define the HTML code to embed the Spotify player
html_code = f'<iframe style="border-radius:12px" src="https://open.spotify.com/embed/playlist/3t3A8abTTxLVQ1fGF2AH8G?utm_source=generator&theme=0" width="100%" height="152" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>'

# Use the Streamlit HTML component to display the code
st.components.v1.html(html_code)


#------------------------------------------


#2. OST
st.subheader('2. Tap OST Market')
st.markdown("Being OST of a Show/Movie will give more exposure to songs. Listeners will not only be limited to the artist's fans but as well as fans/viewers of the show as well.")

st.image('ost.JPG')
st.markdown('_*versus average streams of current most popular non-OST track of artist in Spotify_')

#3. Diff versions of songs
st.subheader('3. Release different versions of songs')
st.markdown('Creating different versions of songs is a proven way to boost engagement over streaming platforms. This is a good strategy for engaging with fans and building on prior successes (Mcguire, 2021)')
st.markdown("Avid fans can confirm that they will listen and delve in any version their beloved idol will release (Hi ARMYs, A'tins, and Swifties!)")


#embed playlist--------------

#BTS-------------------------------

spotify_uri="spotify:album:0PBQ3Cp6NG8WX0G9KQVNMP"

# Define the HTML code to embed the Spotify player
html_code = f'<iframe style="border-radius:12px" src="https://open.spotify.com/embed/album/0PBQ3Cp6NG8WX0G9KQVNMP?utm_source=generator" width="100%" height="152" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>'

# Use the Streamlit HTML component to display the code
st.components.v1.html(html_code)


#SB19-------------------------------

spotify_uri="spotify:album:18g914rk7rcJP0o4uhz8uE"

# Define the HTML code to embed the Spotify player
html_code = f'<iframe style="border-radius:12px" src="https://open.spotify.com/embed/album/18g914rk7rcJP0o4uhz8uE?utm_source=generator" width="100%" height="152" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>'

# Use the Streamlit HTML component to display the code
st.components.v1.html(html_code)


#Taytay-------------------------------

spotify_uri="spotify:album:6WzAiEDGTU7KmEyGwLpBXB"

# Define the HTML code to embed the Spotify player
html_code = f'<iframe style="border-radius:12px" src="https://open.spotify.com/embed/album/6WzAiEDGTU7KmEyGwLpBXB?utm_source=generator" width="100%" height="152" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>'

# Use the Streamlit HTML component to display the code
st.components.v1.html(html_code)

#------------------------------------------



#4. Influencer

st.subheader('4. Collaboration with influencers')
st.markdown("Increasing an artist's reach in Spotify extends to multi-platform marketing. Although influencers would not be the first in mind when it comes to music, one can't deny their benefit in terms of exposure.")
st.markdown('The following are some top influencers Alamat can collaborate with')

st.image('influencer.JPG')

st.markdown("Good vibes are guaranteed with their influence plus Alamat's talent.")

#influencer-------------------------------

spotify_uri="spotify:playlist:3Y9iKIwe9uPEUUIDNLzqZi"

# Define the HTML code to embed the Spotify player
html_code = f'<iframe style="border-radius:12px" src="https://open.spotify.com/embed/playlist/3Y9iKIwe9uPEUUIDNLzqZi?utm_source=generator&theme=0" width="100%" height="152" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>'

# Use the Streamlit HTML component to display the code
st.components.v1.html(html_code)


