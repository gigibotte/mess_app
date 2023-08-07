import streamlit as st

# Set page configuration and add a title to the app
#st.set_page_config(page_title="MESS Model", layout="wide")



st.set_page_config(page_title='MESS - The Multi Energy System Symulator',  layout='wide', page_icon=':ambulance:')

#this is the header
 

t1, t2, t3 = st.columns((0.2,0.1,1)) 

t1.image('graphics/mess_logo.png', width = 500)
t3.title("The Multi Energy System Symulator")
t3.markdown(" **tel:** 01392 451192 **| website:** https://www.swast.nhs.uk **| email:** mailto:data.science@swast.nhs.uk")


# Display the logo image in the header
#logo_path = "graphics\mess_logo.png"  # Path to your logo image file
#st.image(logo_path, use_column_width=True)

# Continue building the rest of your Streamlit app content below the header
# For example, you can add text, input widgets, charts, etc.
#st.write("Welcome to your Streamlit app!")
