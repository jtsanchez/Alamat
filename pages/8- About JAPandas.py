import streamlit as st

st.set_page_config(
    page_title="ALAMAT"
)

#### you may edit here onwards ###

st.title("About JAPandas")

st.image("1.png")

st.markdown("JAPandas is a group of Data Science Fellows under Eskwelabs' Data Science Fellowship- Cohort 11. Dedicated to helping the Philippine music scene grow, the group is honored to recommend strategies for the rising P-pop boy group 'Alamat' through Music Streaming Analytics concepts")


#----try embed

st.markdown('Members')

# url_austin = "https://www.linkedin.com/in/austincarvajal/"
# st.write("Carvajal, Austin [LinkedIn](%s)" % url_austin)

# url_pau = "https://www.linkedin.com/in/jann-pauline-sanchez/"
# st.write("Sanchez, Pau [LinkedIn](%s)" % url_pau)

# url_jed = "https://www.linkedin.com/in/jeremiah-dominic-soliman-59a708155/"
# st.write("Soliman, Jed [LinkedIn](%s)" % url_jed)


# st.markdown('Mentor')
# url_AJ = "https://www.linkedin.com/in/ajloconer/"
# st.write("Oconer, AJ [LinkedIn](%s)" % url_jed)


#---try 3 cols

url_austin = "https://www.linkedin.com/in/austincarvajal/"
url_pau = "https://www.linkedin.com/in/jann-pauline-sanchez/"
url_jed = "https://www.linkedin.com/in/jeremiah-dominic-soliman-59a708155/"
url_AJ = "https://www.linkedin.com/in/ajloconer/"

col1, col2, col3 = st.columns(3)

with col2:
   st.subheader('Austin')
   st.write("Carvajal, Austin Loi [LinkedIn](%s)" % url_austin)

with col3:
   st.subheader('Pau')
   st.write("Sanchez, Jann Pauline [LinkedIn](%s)" % url_pau)

with col1:
   st.subheader('Jed')
   st.write("Soliman, Jeremiah Dominic [LinkedIn](%s)" % url_jed)


st.markdown('Mentor')
st.subheader('AJ')
url_AJ = "https://www.linkedin.com/in/ajloconer/"
st.write("Oconer, Andrew Justin [LinkedIn](%s)" % url_AJ)