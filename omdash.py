import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import date, datetime
from PIL import Image
from pathlib import Path
import base64
today = date.today()

st.write('Upload file')
# uploaded_file = st.file_uploader("Choose a file")
uploaded_file = 'data.csv'
st.title('Outcome Measures Report')
cols_used = [2,3,32,33,57,58,59,60,61,71,77,86,93,111]
# data = pd.read_csv("data.csv", usecols=cols_used, names=['URN', 'Date', 'Anxiety', 'Depression', 'PTSD', 'Intrusions', 'Avoidance', 'PTSD cognitions','Arousal', 'Insomnia', 'Alcohol', 'Anger', 'Function', 'Physical'], skiprows=1)
# st.write(data)

# Patient Selector
if uploaded_file is not None:
    # load data
    data = pd.read_csv(uploaded_file, usecols=cols_used, names=['URN', 'Date', 'Anxiety', 'Depression', 'PTSD', 'Intrusions', 'Avoidance', 'PTSD cognitions','Arousal', 'Insomnia', 'Alcohol', 'Anger', 'Function', 'Physical'], skiprows=1)
    # change types
    data['Date'] = data['Date'].astype('datetime64')
    
    option = st.sidebar.selectbox(
        'For patient URN:',
        data['URN'].unique()
    )

    ptdata = data[data['URN'] == option]
    # # Convert dates into strings for use in charts
    ptdata['DateStr'] =ptdata['Date'].dt.strftime('%d%m%Y')
    # dates = ptdata['Date']
    # li = dates.Date.tolist()
    # s = []
    # for i in li:
    #     x = i.strftime("%d %b %y")
    #     s.append(x)

    st.write('### Report generated on: ' + str(today) + ' for URN: ' + str(option))

    st.write(ptdata)
    st.write(ptdata.dtypes)

    st.write(ptdata['Date'])

    pclfig = px.bar(
        ptdata,
        # x='Date',
        x='DateStr',
        y=['PTSD','Insomnia'],
        range_y=[0,80]
    )
    hadsfig = px.scatter_matrix(
        ptdata,
        dimensions=['Anxiety','Depression'],
        color=['Date']
    )
    st.plotly_chart(pclfig)
    # st.plotly_chart(hadsfig)
else:
    st.write('Upload data file to continue - export from redcap as CSV and tick "remove all tagged identifier fields"')

