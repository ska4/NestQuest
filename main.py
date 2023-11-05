import streamlit as st 
import pandas as pd
from PIL import Image

st.title(':blue[Nest]:red[Quest]')
st.title('Journey to :green[Home Ownership]')

df = pd.read_csv("/Users/frootyloops/Desktop/data/HomeBuyerInfo.csv", index_col=None)  # read a CSV file inside the 'data" folder next to 'app.py'
# df = pd.read_excel(...)  # will work for Excel files
if 'button' not in st.session_state:
    st.session_state.button = False
    
# df = df.reset_index(drop=True)

def click_button():
    st.session_state.button = not st.session_state.button

st.button('Show Data', on_click=click_button)

if st.session_state.button:
    st.dataframe(df, use_container_width=True, hide_index=True)
    image1 = Image.open("/Users/frootyloops/Downloads/Appraised Value.png")
    image2 = Image.open("/Users/frootyloops/Downloads/Gross Monthly Income.png")
    image3 = Image.open("/Users/frootyloops/Downloads/Loan Amount.png")
    image4 = Image.open("/Users/frootyloops/Downloads/Student Loan.png")
    image5 = Image.open("/Users/frootyloops/Downloads/Credit Card Payment.png")
    image6 = Image.open("/Users/frootyloops/Downloads/Down Payment.png")
    image7 = Image.open("/Users/frootyloops/Downloads/Monthly Mortgage.png")
    # Display the image in your Streamlit app
    st.image(image1, caption="Appraised Value")
    st.image(image2, caption="Gross Monthly Income")
    st.image(image3, caption="Loan Amount")
    st.image(image4, caption="Student Loan")
    st.image(image5, caption="Credit Card Payment")
    st.image(image6, caption="Down Payment")
    st.image(image7, caption="Monthly Mortgage")
