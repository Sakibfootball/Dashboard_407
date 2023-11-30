import streamlit as st # web development
import numpy as np # np mean, np random 
import pandas as pd # read csv, df manipulation
import time # to simulate a real time data, time loop 
import plotly.express as px # interactive charts
from PIL import Image


# read csv from a github repo
df = pd.read_csv("407 Mid assesment Dataset - Sheet1.csv")


st.set_page_config(
    page_title = 'Power Consumption Dashboard',
    page_icon = '⚡',
    layout = 'wide'
)

# dashboard title

st.title("Power Consumption Dashboard")

# top-level filters 

# job_filter = st.selectbox("Select the Job", pd.unique(df['job']))


# creating a single-element container.
placeholder = st.empty()

# dataframe filter 

# df = df[df['job']==job_filter]

# near real-time / live feed simulation 

# for seconds in range(200):
# #while True:
#
#     df['age_new'] = df['age'] * np.random.choice(range(1,5))
#     df['balance_new'] = df['balance'] * np.random.choice(range(1,5))
#
#     # creating KPIs
#     avg_age = np.mean(df['age_new'])
#
#     count_married = int(df[(df["marital"]=='married')]['marital'].count() + np.random.choice(range(1,30)))
#
#     balance = np.mean(df['balance_new'])
#
#     with placeholder.container():
#         # create three columns
#         kpi1, kpi2, kpi3 = st.columns(3)
#
#         # fill in those three columns with respective metrics or KPIs
#         kpi1.metric(label="Age ⏳", value=round(avg_age), delta= round(avg_age) - 10)
#         kpi2.metric(label="Married Count 💍", value= int(count_married), delta= - 10 + count_married)
#         kpi3.metric(label="A/C Balance ＄", value= f"$ {round(balance,2)} ", delta= - round(balance/count_married) * 100)

        # create two columns for charts 

# col1 = st.columns(1)
# with col1:
st.header("Personal PC Analysis")
# st.markdown("###")
img1 = Image.open("img1.png")
st.image(img1, caption="Power consumption of Sakib’s PC")

st.header("Comparisons between members PC")
col1, col2 = st.columns(2)

with col1:
    img2 = Image.open("img2.png")

    st.image(img2, caption="Power consumption of All members heavy PC usage")

    # st.image(img4, caption="")
with col2:
    img3 = Image.open("img3.png")
    st.image(img3, caption="Power consumption of All members light PC usage")

st.header("Comparisons between Lab PC")
col3, col4 = st.columns(2)
with col3:
    img4 = Image.open("img4.png")
    st.image(img4, caption="")

st.header("Household Power Consumption")
col5, col6 = st.columns(2)
with col5:
    img6 = Image.open("img6.png")
    st.image(img6, caption="Household Power Consumption of Sakib's House")
with col6:
    img5 = Image.open("img5.png")
    st.image(img5, caption="Household Power Consumption Comparison Of All Members")


st.markdown("### Detailed Data View")
st.dataframe(df)
time.sleep(1)
    #placeholder.empty()


