import streamlit as st
import yfinance as yf
import plotly.graph_objects as go

st.title("📊 Portfolio Dashboard")

tickers = st.multiselect("Select Stocks", ["AAPL", "MSFT", "TSLA", "GOOG", "AMZN"], default=["AAPL", "MSFT"])
if tickers:
    data = yf.download(tickers, period="6mo")["Adj Close"]
    fig = go.Figure()
    for ticker in tickers:
        fig.add_trace(go.Scatter(x=data.index, y=data[ticker], name=ticker))
    st.plotly_chart(fig, use_container_width=True)