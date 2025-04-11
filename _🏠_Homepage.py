import streamlit as st
import pandas as pd

###############
# PAGE CONFIG #
###############
st.set_page_config(
    page_icon = "📈",
    page_title = "Factor Investing Demo"
)

df = pd.read_csv("set100_ranking.csv")
# Rename
df = df.rename(columns = {
    "symbol" : "Symbol",
    "marketCap" : "Market Capitalization",
    "pe" : "P/E",
    "pb" : "P/BV",
    "dividendYield" : "Dividend Yield",
    "ytdPercentChange" : "YTD% Change",
    "de" : "D/E",
    "roe" : "ROE",
    "beta" : "Beta"
})



###############
# PAGE CONTENT#
###############

st.title("📈 Factor Investing Demo")
st.markdown("Project's objective is to try to implement a simple factor investing using python. You can read a full methodology at")
st.page_link("pages/2_📘_Documentation.py", label="Documentation", icon="📘")
st.caption("This project uses a SET100 data from www.SET.or.th at 4/8/2025")

# Tables
display_list1 = ["Symbol" ,"ROE" ,"P/E", "P/BV", "D/E", "Dividend Yield", "YTD% Change","Beta", "Market Capitalization"]
# Top 10 overall
st.markdown("# 🏆 Top 10 Highest-Ranked Stocks Based on Multi-Factor Analysis")
df_topoverall = df.sort_values(by="rank_score", ascending=False)[display_list1].iloc[:10,:]
st.table(df_topoverall)
cols = st.columns(2)

with cols[0]:
    # Top 5 Value
    st.markdown("## 🏷️ Top 5 Value Stocks")
    st.caption("Base on P/E and P/BV.")
    df_topval = df.sort_values(by="rank_val", ascending=False).iloc[:5,:]
    st.table(df_topval[["Symbol" , "P/E" , "P/BV"]])

    # Top 5 Momentum stock
    st.markdown("## 📈 Top 5 Momentum Stocks")
    st.caption("Based on YTD price performance.")
    df_topmome = df.sort_values(by="rank_mome", ascending=False).iloc[:5,:]
    st.table(df_topmome[['Symbol', 'YTD% Change']])

    # Top 5 Highest Quality
    st.markdown("## 🧾 Top 5 Highest Quality Stocks")
    st.caption("Based on ROE and D/E.")
    df_topq = df.sort_values(by="rank_q", ascending=False).iloc[:5,:]
    st.table(df_topq[['Symbol', 'ROE', 'D/E']])

with cols[1]:
    # Top 5 Lowest Volatility
    st.markdown("## 🛡️ Top 5 Low-Volatility Stocks")
    st.caption("Based on beta.")
    df_topvol = df.sort_values(by="rank_vol", ascending=False).iloc[:5,:]
    st.table(df_topvol[["Symbol", "Beta"]])

    # Top 5 Highest Dividend Yield
    st.markdown("## 💰 Top 5 High Dividend Yield Stocks")
    st.caption("Based on Dividend Yield.")
    df_topmome = df.sort_values(by="rank_divYield", ascending=False).iloc[:5,:]
    st.table(df_topmome[['Symbol', 'Dividend Yield']])

    
st.divider()
st.markdown("""
---

### 👤 About Me

Hi! I'm **Punyawat Pungphomin**, a finance student passionate about data analytics, quantitative investing, and financial technology.  
This project is part of my journey to explore **factor investing strategies** by combining finance theory with Python programming.

I collected and cleaned all the data myself using a custom web scraping script written in Python,  
then analyzed and visualized it with **Pandas**, **SciPy**, and **Streamlit**.

Thank you for your attention!
Feel free to connect or reach out via:
- 📧 Email: punyawat.punphomin@gmail.com  
- 💼 LinkedIn: [punyawatp](www.linkedin.com/in/punyawatp)

""")