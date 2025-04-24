import pandas as pd
import streamlit as st

# Load data
df = pd.read_csv(r"C:\Users\Ashish Kumar\Downloads\Clean_Dataset.csv\Clean_Dataset.csv")

# Streamlit App Title
st.title("✈️ AI Flight Price Tracker")
st.markdown("Find the **cheapest flight** between two cities.")

# Get unique city options
cities_from = sorted(df["source_city"].unique())
cities_to = sorted(df["destination_city"].unique())

# UI - Select boxes
source = st.selectbox("Select Source City", cities_from)
destination = st.selectbox("Select Destination City", cities_to)

# Button to find flight
if st.button("Find Cheapest Flight"):
    results = df[(df["source_city"] == source) & (df["destination_city"] == destination)]

    if results.empty:
        st.warning("❌ No flights found between selected cities.")
    else:
        cheapest = results.loc[results["price"].idxmin()]
        st.success("✅ Cheapest Flight Found!")
        st.markdown(f"""
        **✈️ Airline**: {cheapest['airline']}  
        **🔢 Flight**: {cheapest['flight']}  
        **💵 Price**: ₹{cheapest['price']}  
        **🕒 Departure**: {cheapest['departure_time']}  
        **🕓 Arrival**: {cheapest['arrival_time']}  
        **🛑 Stops**: {cheapest['stops']}  
        **🎟️ Class**: {cheapest['class']}  
        **⏱️ Duration**: {cheapest['duration']} hrs  
        **📆 Days Left**: {cheapest['days_left']}
        """)

# run this in cmd -> streamlit run "D:\Study\Coding\Coding\AI\flight_gui.py"
