import streamlit as st
import pandas as pd
import json

st.title('Parse Bank Transaction Data')

import json

uploaded_file = st.file_uploader(...) 

if uploaded_file:

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

  print(f"Collateral rows: {len(collateral)}") 
  print(f"Spend rows: {len(spend)}")

  collateral_df = pd.DataFrame(collateral)
  spend_df = pd.DataFrame(spend)
