import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import date, datetime
from PIL import Image
from pathlib import Path
import base64
today = date.today()

# st.write('Upload file')
# uploaded_file = st.file_uploader("Choose a file")

st.title('Outcome Measures Report')
cols_used = [3,6,34,35, 59, 60, 61, 62, 63, 73, 79, 87, 95, 113]
# data = pd.read_csv(uploaded_file, usecols=cols_used, names=['URN', 'Date', 'Anxiety', 'Depression', 'PTSD', 'Intrusions', 'Avoidance', 'PTSD cognitions','Arousal', 'Insomnia', 'Alcohol', 'Anger', 'Function', 'Physical'], skiprows=0)
data = pd.read_csv("data.csv", usecols=cols_used, names=['URN', 'Date', 'Anxiety', 'Depression', 'PTSD', 'Intrusions', 'Avoidance', 'PTSD cognitions','Arousal', 'Insomnia', 'Alcohol', 'Anger', 'Function', 'Physical'], skiprows=0)
# st.write(data)

# Patient Selector
option = st.sidebar.selectbox(
    'For patient URN:',
    data['URN'].unique()
)
ptdata = data[data['URN'] == option]
# # Convert dates into strings for use in charts
# dates = ptdata['Date']
# li = dates.Date.tolist()
# s = []
# for i in li:
#     x = i.strftime("%d %b %y")
#     s.append(x)

st.write('### Report generated on: ' + str(today) + ' for URN: ' + str(option))

st.write(ptdata)

st.write(ptdata['Date'])

pclfig = px.bar(
    ptdata,
    x=ptdata['Date'],
    y='PTSD',
    range_y=[0,80]
)
hadsfig = px.scatter_matrix(
    ptdata,
    dimensions=['Anxiety','Depression'],
    color=['Date']
)


# scfig.update_layout(
#     title=({
#         'text': 'PCL',
#         'xanchor': 'center',
#         'yanchor': 'top',}),
#     xaxis_title="Date",
#     plot_bgcolor="#eceff1"
# )

# hadsfig = px.line(
#     ptdata,
#     x=ptdata['Date'],
#     y=['Anxiety', 'Depression'],
#     range_y=[0,21]
# )
# hadsfig.update_layout(
#     title=({
#         'text': 'HADS',
#         'xanchor': 'center',
#         'yanchor': 'top',}),
#     xaxis_title="Date",
#     plot_bgcolor="#eceff1"
# )

st.plotly_chart(pclfig)
st.plotly_chart(hadsfig)

# pclfig = px.imshow(
#     ptdata['Intrusions','Avoidance','PTSD Cognitions','Arousal'],
#     y=ptdata['Date'], x=['Intrusions','Avoidance','PTSD Cognitions','Arousal'],
#     title='PTSD Symptoms'
# )

