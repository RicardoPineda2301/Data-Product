import streamlit as st
import pandas as pd
import numpy as np

### Set Title

st.title('Uber Pickups')


### Importing data

DATE_COLUMN = 'Date/Time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/streamlit-demo-data/uber-raw-data-sep14.csv.gz')

###Create a Function to load data

def load_data(nrows):
    data = pd.read_csv(DATA_URL, parse_dates=[DATE_COLUMN], nrows=nrows).rename(columns={
        "Lat":"latitude",
        "Lon":"longitude"
    })
    return data

### Now we add a text to notify the data is being loaded

# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading data...')
# Load 10,000 rows of data into the dataframe.
data = load_data(10000)
# Notify the reader that the data was successfully loaded.
data_load_state.text("Done!")

st.subheader('Raw data')
st.write(data)


## Remember if you wish to hide the table you can use a checkbox
if st.checkbox('Show raw data'):

    st.subheader('Number of pickups by hour')

    hist_values = np.histogram(
        data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]

    st.bar_chart(hist_values)


## Let's create a map for the data

st.subheader('Map of all pickups')

st.map(data)


## Why not add a filter


hour_to_filter = 17
filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]
st.subheader(f'Map of all pickups at {hour_to_filter}:00')
st.map(filtered_data)


## That's boring, let's create a dynamic filter


hour_to_filter = st.slider('hour', 0, 23, 17)
filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]
st.subheader(f'Map of all pickups at {hour_to_filter}:00')
st.map(filtered_data)



