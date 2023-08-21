import streamlit as st
import pandas as pd
import json

st.title('Parse Bank Transaction Data')

if uploaded_file is not None:

  data = json.loads(uploaded_file.getvalue())
  
  if type(data) == dict:
    data = [data]

  collateral = []
  spend = []

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
