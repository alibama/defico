import streamlit as st
import requests
import json

st.set_page_config(page_title="Charge Viewer") 

# API credentials
API_KEY = "key_goes_here"  

# Fetch data from API
url = "https://api.raincards.xyz/v1/transactions"
headers = {
    "Accept": "application/json",
    "Api-Key": API_KEY
}
response = requests.get(url, headers=headers)
data = response.json()


# Get list of unique cardholderFirstNames
first_names = list(set(charge["cardholderFirstName"] for charge in data))

# Create dropdown selector for first name
selected_first_name = st.selectbox("Select cardholder", first_names)

# Filter charges by selected first name
charges = [charge for charge in data if charge["cardholderFirstName"] == selected_first_name]

# Display table of charges
st.header(f"Charges for {selected_first_name}")
st.table(charges) 

# Display categories
categories = {charge["category"] for charge in charges}
st.header("Categories")
for cat in categories:
    st.text(cat)

