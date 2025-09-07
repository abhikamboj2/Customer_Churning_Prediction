import streamlit as st
import pandas as pd
import numpy as np
st.title("hello,streamlit")
st.write("This is write function")
df=pd.DataFrame({
    'first-col':[1,2,3,4,5],
    'second-col':[10,20,30,40,50]})
st.write(df)

# Create line chart
chart_data=pd.DataFrame(np.random.randint(20,3),columns=['a','b','c'])
st.line_chart(chart_data)