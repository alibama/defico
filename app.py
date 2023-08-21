import streamlit as st
import pandas as pd
import json

st.title('Parse Bank Transaction Data')

uploaded_file = st.file_uploader('Upload JSON file', type=['json'])
if uploaded_file is not None:
    data = json.loads(uploaded_file.getvalue())
  
collateral = []
spend = []

if type(data) == dict:
    data = [data]
  
for row in data:
    if 'collateral_add' in row['type']: 
        collateral.append(row)
    elif 'spend' in row['type']:
        spend.append(row)

collateral_df = pd.DataFrame(collateral) 
spend_df = pd.DataFrame(spend)

st.write('Collateral Transactions')
st.write(collateral_df.head())

st.write('Spend Transactions')
st.write(spend_df.head())
