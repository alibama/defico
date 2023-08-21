import streamlit as st
import pandas as pd
import json

st.title('Parse Bank Transaction Data')

uploaded_file = st.file_uploader('Upload JSON file', type=['json'])
if uploaded_file is not None:
    data = json.loads(uploaded_file.getvalue())

    collateral = []
    spend = []
    for row in data:
        if row['type'] == 'collateral_add':
            collateral.append(row) 
        elif row['type'] == 'spend':
            spend.append(row)

    collateral_df = pd.DataFrame(collateral) 
    spend_df = pd.DataFrame(spend)

    st.write('Collateral Transactions')
    st.write(collateral_df.head())

    st.write('Spend Transactions') 
    st.write(spend_df.head())
