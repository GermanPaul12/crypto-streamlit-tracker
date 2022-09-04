import yfinance as yf
import streamlit as st
import pandas as pd
from datetime import datetime
from datetime import date
from dateutil.relativedelta import relativedelta
import plotly.express as px

crypto_mapping = {"Bitcoin USD": "BTC-USD", "Bitcoin EUR": "BTC-EUR", "Ethereum USD": "ETH-USD", "Ethereum EUR": "ETH-EUR",
                  "Cardano USD": "ADA-USD", "Cardano EUR": "ADA-EUR", "BNB USD": "BNB-USD", "BNB EUR": "BNB-EUR",
                  "VeChain USD": "VET-USD", "VeChain EUR": "VET-EUR", "Solana USD": "SOL-USD", "Solana EUR": "SOL-EUR",}

st.title("Crypto Tracker")
crypto_option = st.sidebar.selectbox(
    "Which Crypto do you want to visualize?", ("Bitcoin USD", "Bitcoin EUR", "Ethereum USD", "Ethereum EUR", "Cardano USD",
                                               "Cardano EUR", "BNB USD", "BNB EUR", "VeChain USD", "VeChain EUR", "Solana USD",
                                               "Solana EUR"
                                               )
)

start_date = st.sidebar.date_input("Start Date (The longer your interval, the higher the Data Interval should be!)", date.today() - relativedelta(months=1))
end_date = st.sidebar.date_input("End Date", date.today())

data_interval = st.sidebar.selectbox(
    "Data Interval",
    (
        "1m",
        "2m",
        "5m",
        "15m",
        "30m",
        "60m",
        "90m",
        "1h",
        "1d",
        "5d",
        "1wk",
        "1mo",
        "3mo",
    ),
)

symbol_crypto = crypto_mapping[crypto_option]
data_crypto = yf.Ticker(symbol_crypto)

value_selector = st.sidebar.selectbox(
    "Value Selector", ("Open", "High", "Low", "Close", "Volume")
)

if st.sidebar.button("Generate"):
    crypto_hist = data_crypto.history(
        start=start_date, end=end_date, interval=data_interval
    )
    fig = px.line(crypto_hist, 
    x=crypto_hist.index, y=value_selector,
    labels={"x": "Date"})
    st.plotly_chart(fig)
