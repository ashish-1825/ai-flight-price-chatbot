# ✈️ AI Flight Price Chatbot

An **AI-powered chatbot** built using **Streamlit** that helps users find the **cheapest flights** between cities from a given dataset. It supports **natural language queries**, **filtering by travel class**, and simulates an intelligent assistant for flight suggestions. This project was developed as part of the **AI Essentials subject** for a college assignment.

---

## 🔍 Features

- 💬 Chatbot interface using natural language input
- 🧠 Basic AI logic using NLP (intent pattern matching)
- 💸 Finds the top 3 cheapest flights from a dataset
- 🎫 Filter flights by **class** (Economy / Business)
- ⏱️ Sort by duration, stops
- 🎨 Built using Python, Pandas & Streamlit
- 🎓 Designed as an academic project

---

## 🗂️ Dataset Overview

The app uses a cleaned dataset (`Clean_Dataset.csv`) with the following columns:

- `Airline`
- `Source`
- `Destination`
- `Route`
- `Dep_Time`
- `Arrival_Time`
- `Duration`
- `Total_Stops`
- `Additional_Info`
- `Price`
- `Class`

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/ai-flight-price-chatbot.git
cd ai-flight-price-chatbot


### 2. Install Required Libraries
pip install -r requirements.txt


 Run the Streamlit Chatbot App
streamlit run chatbot_app.py

 Example User Queries
Try typing these into the chatbot:

cheapest flight from Delhi to Mumbai
show me flights from Bangalore to Kolkata in economy
business class flights from Chennai to Delhi

AI Concepts Used
Although not using heavy ML models, this project simulates an AI assistant by:
Implementing intent detection using regex-based NLP
Simulating decision-making for best flight selection
Planning to integrate a machine learning price prediction model in future

Future Enhancements
🧠 Add real NLP with spaCy or transformers
🔮 Integrate a ML model for predicting flight prices
🌐 Connect to real-time APIs like Skyscanner, Google Flights
🎙️ Voice-based interaction with speech-to-text
