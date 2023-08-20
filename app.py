import streamlit as st
import pandas as pd 
import json
import plotly.express as px

st.title('JSON Transaction Explorer')

uploaded_file = st.file_uploader('Choose a JSON file', type='json')

if uploaded_file is not None:
    data = json.load(uploaded_file)
    
    df = pd.json_normalize(data)

    # Display full table
    st.dataframe(df)  

    # Analysis
    totals = df['amount'].describe()
    st.write("Total Transactions:", len(df))

    st.write("Total Amount:")
    st.metric(label="Sum", value=totals['sum'])
    st.metric(label="Average", value=totals['mean'])
    st.metric(label="Min", value=totals['min'])
    st.metric(label="Max", value=totals['max'])

    # Visualizations 
    fig = px.histogram(df, x="amount")
    st.plotly_chart(fig)

    fig = px.pie(df, values='amount', names='merchantName')
    st.plotly_chart(fig)
