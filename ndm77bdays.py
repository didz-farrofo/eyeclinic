import json
import streamlit as st
import pandas as pd
import plotly.express as px
#from matplotlib import pyplot as pt
from streamlit_lottie import st_lottie
#import chart_studio.plotly as py
#t.title(":bar_chart: Dashboard")


st.set_page_config(page_title="NDM77 Birthdays",
                  page_icon=":bar_chart:",
                  layout="wide"
)

df= pd.read_excel(
    io = 'RegisteredB77_Final2.xlsx',
    engine='openpyxl',
    sheet_name='Bday77',
    skiprows=0,
    usecols='A:C',
    nrows=100
)
#st.dataframe(df)
def load_lottiefile(filepath:str):
    with open (filepath, "r") as f:
        return json.load (f)

lottie_coding=load_lottiefile("lottiefiles/happybirthday1.json")
lottie_coding2=load_lottiefile("lottiefiles/happybirthday2.json")
st_lottie(
    lottie_coding,
    height=300,
    width=800
)

st.title(":cake: NDM '77 CELEBRANTS")
st.markdown ("""---""")
rb=st.selectbox("Please select month:", ['January','February','March','April','May','June','July','August','September','October','November','December'])
print(rb)
if rb == 'January':
    newdf=df[df["Birthday"].str[:3] == 'Jan']
elif rb == 'February':
    newdf=df[df["Birthday"].str[:3] == 'Feb']
elif rb== 'March':
    newdf=df[df["Birthday"].str[:3] == 'Mar']
elif rb == 'April':
    newdf=df[df["Birthday"].str[:3] == 'Apr']
elif rb == 'May':
    newdf=df[df["Birthday"].str[:3] == 'May']
elif rb == 'June':
    newdf=df[df["Birthday"].str[:3] == 'Jun']
elif rb == 'July':
    newdf=df[df["Birthday"].str[:3] == 'Jul']
elif rb== 'August':
    newdf=df[df["Birthday"].str[:3] == 'Aug']
elif rb == 'September':
    newdf=df[df["Birthday"].str[:3] == 'Sep']
elif rb == 'October':
        newdf=df[df["Birthday"].str[:3] == 'Oct']
elif rb== 'November':
        newdf=df[df["Birthday"].str[:3] == 'Nov']
else:
        newdf=df[df["Birthday"].str[:3] == 'Dec']

#st.subheader(":cake: HAPPY BIRTHDAY")
st.dataframe(newdf)
st_lottie(
    lottie_coding2,
    height=300,
    width=800
)
