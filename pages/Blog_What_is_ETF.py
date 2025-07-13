import streamlit as st

st.title("📝 Blog: What is an ETF?")
st.markdown("""
**Exchange-Traded Funds (ETFs)** are baskets of securities that trade like a stock on an exchange.

- ✅ Diversified
- ✅ Low-cost
- ✅ Easy to trade

### Code Example
```python
import yfinance as yf
data = yf.download("VOO", period="1y")