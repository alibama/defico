import streamlit as st
import pandas as pd
import json

st.title('JSON Transaction Explorer')

uploaded_file = st.file_uploader('Choose a JSON file', type='json')

if uploaded_file is not None:

  data = json.load(uploaded_file)

  # Schema detection
  transactions = data['transactions']
  schemas = {}

  for transaction in transactions:

    t_type = transaction['type']

    if t_type not in schemas:
      schemas[t_type] = {}
    
    schemas[t_type] = transaction.keys()

  # Print schemas
  st.header("Detected Schemas")
  for t_type, schema in schemas.items():
    st.write(f"{t_type} schema: {sorted(schema)}")
