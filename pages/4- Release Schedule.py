import streamlit as st

st.set_page_config(
    page_title="ALAMAT"
)


st.title("Release Schedule")


st.write("In boosting streams, another thing we can look at is date of release of new songs and as well as its timing as well.")

st.write("We plotted streams of charting songs from P-pop (SB19) and K-pop (BTS and Stray Kids) artists fron 2017 until 2022. Here we can notice that the spikes are after release of albums/singles of the mentioned artist. This is apparent on both BTS's and SB19's streams in mid 2021 which is the release of BTS's Butter and SB19's Pagsibol")
image = Image.open("p4-1.png")
st.image(image, caption="Monthly Streams for Charting Songs (2017-2022).", use_column_width=True)

st.write("To further assess the relationship of the release between K-pop and P-pop we checked the correlation of streams of the 3 artist. Based on the this, we can see that there is a positive correlation between release of K-pop(BTS and Straykids) vs. P-pop(SB 19). What this suggests is that as streams of BTS and/or Stray Kids increase SB19 are charting as well.")
image2 = Image.open("p4-2.png")
st.image(image2, caption="Correlation of Streams.", use_column_width=True)

st.write("Aside from the timing of song release, we also checked on which month charting songs are releasing and/or high charting. The graph below shows the average stream per month from 2017 to 2022. From this we can see a spike on the midyear (June-July/ Beginning of Q3)")
image3 = Image.open("p4-3.png")
st.image(image, caption="Average Streams for 2017-2022 Charting Songs per Month.", use_column_width=True)


st.subheader('Recommendations') 
st.write("With these findings for timing of releases and analysis on charting songs; the following are recommended:")

st.write("""
1. When releasing songs, ALAMAT can consider riding the waves of releases of Famous K-pop artists (BTS and Stray Kids) as this may lead to higher exposure for P-pop songs as well.
2. When releasing songs, ALAMAT can consider releasing in the beginning of Q3 (June and July) as these are the months recorded to have higher streams for both K-pop and P-pop top artists.
""")