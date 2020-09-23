import streamlit as st
import numpy as np
import pandas as pd

st.title('My First Application in Streamlit')

x=4

st.write(x, 'square is', x*x)

x=4

x, 'square is', x*x

st.write("Here's our first attempt at using data to create a table:")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))

df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

df



chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)

map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)

if st.checkbox('Show dataframe'):
    x = st.slider('x')
    st.writer(x, 'square', x*x)

option = st.selectbox(
    'Which number do you like best?',
     df['first column'])

'You selected: ', option

option_side = st.sidebar.selectbox(
    'Which number do you like best?',
     ["hello", "world", "!"])

'You selected:', option_side

import time
'Starting a long computation...'

# Initializing the variables
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  # Update the progress bar with each iteration.
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i + 1)
  time.sleep(0.1)

'...and now we\'re done!'

add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)

add_slider = st.sidebar.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0)
)

    