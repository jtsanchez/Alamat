import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="ALAMAT"
)

#### you may edit here onwards ###

st.title("Comparison vs. Leading Artists")

st.write("The thing with Alamat is that their branding is unique and true to the Filipino heritage, but even with this, it still would not hurt if they follow the path taken by other competitors in the scene.")

st.write("In the P-Pop Scene, we have taken data though Spotify Web API showing that SB19 is their number one competitor and a close second is BGYO.")

image = Image.open("8.png")
st.image(image, caption="P-pop scene based on followers and popularity.", use_column_width=True)

st.write("But since we also wanted to capture audiences from around the world, we wanted to compare also with the K-Pop Scene where BTS and Stray kids top the charts.")

image2 = Image.open("7.png")
st.image(image2, caption="K-pop scene based on followers and popularity.", use_column_width=True)

st.write("Interestingly enough, the distinguishable audio features for both kpop and ppop are the same, namely: Danceability, Energy, Key, Loudness, Speechiness. Other audio features have little to no difference or might not even matter in the production of the song. *Still, it is provided here for reference of the client.*")

image3 = Image.open("ppopfeat.png")
image4 = Image.open("kpopfeat.png")

col1, col2 = st.columns(2)

with col1:
    st.subheader("P-POP")
    st.image(image3, caption='SB19 vs BGYO vs Alamat', use_column_width=True)

with col2:
    st.header("K-POP")
    st.image(image4, caption='BTS vs Stray Kids vs Alamat', use_column_width=True)

st.subheader('Recommendation 1')    
st.write("With these findings for the audio features, we collated these recommendations:")

st.write("""
1. Increase suitability for dancing - a possibility to be translated to gain popularity through TikTok (social media app for people dancing to songs)
2. Increase Energy of songs - more intensity and activity to their songs
3. Decrease the Key (from G to E) - this can also help when performing live 
4. Increase Loudness (from -7 db to -4 db) 
5. Increase speechiness - integrate more lyrics or words into the song
""")

st.write("Another way of extending their reach is tapping into the global market. According to the International Federation of the Phonographic Industry(IFPI), the USA and Canada Region has the world’s largest music revenue amounting to about $10 B.")

image5 = Image.open("bazinga.png")
st.image(image5, caption="SB19 Tracks and their no. of streams in Spotify.", use_column_width=True)         
         
st.write("SB19 managed to get into this market by releasing songs with English lyrics. In fact, if we removed their top song *MAPA*, we can see that Bazinga and WYAT are next in the charts. For Bazinga, 92% of the total duration of the song is in English and the remaining 8% or roughly only 17 seconds is in Filipino. For WYAT, the whole song is in English.")
         
st.subheader('Recommendation 2')           
st.write("In the case of Alamat, we recommend to still stick to their branding as this is what separates them from the competition and continue to release songs in Filipino and other language and dialects. To compensate though, we recommend that Alamat still release Filipino songs, but have another version in complete English lyrics to capture the Western Audience.")
         
st.subheader('Recommendation 3') 
image6 = Image.open("12.png")
st.image(image6, caption="Tracks Released in a Year vs No. of Followers.", use_column_width=True) 
         
st.write("Lastly, we recommend Alamat to release more songs in a year. It is clearly shown in this graph that boy groups who tend to release more songs in a year have larger number of followers. Take BTS for example which releases an average of 6 tracks a year. ")
         
image7 = Image.open("14.png")
st.image(image7, caption="BTS Tracks Data vs No. of Streams (Time - Series)", use_column_width=True)          
         
st.write("In this graph, you will see many spikes in the streams throughout the years on when they  release their singles. So the more tracks you release in a year, the more chances you have of going viral and thus increasing your followers and streams.")
