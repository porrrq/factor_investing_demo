import streamlit as st
import pandas as pd

###############
# PAGE CONFIG #
###############
st.set_page_config(
    page_icon = "📘",
    page_title = "Documentation"
)
################
# PAGE CONTENT #
################
st.title("📘 Documentation")
# Introduction
st.markdown("## Introduction")
st.markdown("This project presents a **simple** factor-based equity screening model that utilizes multiple financial metrics to rank and evaluate stocks in SET100. The methodology follows a quantitative investing approach inspired by academic research and institutional practices, such as *MSCI’s Foundations of Factor Investing.*")
st.markdown("To illustrate, I use 6 factors to calculate stock composite score to representing the overall attractiveness of a stock across multiple dimensions including")
st.table(
    pd.DataFrame({
        "Factors" : ["Value", "Size", "Volatility", "Momentum", "Dividend Yield", "Quality"],
        "Captured By": ["P/E, P/BV", "Market Capitalization", "Bata", "52week Return", "Dividend Yield", "ROE, DE ratio"]
    })
)
st.caption("*Note that all the data comes from www.SET.or.th as 4/8/2025*.")

st.divider()

# Methodology
st.markdown("## 🧠 Methodology")
st.markdown("### Data management")
st.markdown("This section will includes import, cleaning, and organized data.")
# Import and Cleaning
st.markdown("First of all, I import all needed libraries.")
st.code(
    '''
    import pandas as pd
    from scipy.stats import zscore
    ''',
    language="python"
)
st.markdown("Now, let's import the data*.")
st.code(
    '''
    # Import SET100 data
    url = "https://raw.githubusercontent.com/porrrq/file-hosts/refs/heads/main/others/set100.csv"
    df = pd.read_csv(url)

    # Preview first 5 observations
    df.head()
    ''',
    language="python"
)
url = "https://raw.githubusercontent.com/porrrq/file-hosts/refs/heads/main/others/set100.csv"
df = pd.read_csv(url)

st.table(df.head())
st.caption("\* The data has been independently collected using a web scraping script I wrote myself in Python.")
st.markdown("You might notice that `AAV` doens't have a `dividendYield` because not all companies pay dividends, which is why some stocks may have no dividend yield. Thus, I will replace an empty `dividendYield` by `0`.")

st.code(
    '''
    df.loc[:,'dividendYield'] = df.loc[:,'dividendYield'].fillna(0)
    ''',
    language="python"

)
df.loc[:,'dividendYield'] = df.loc[:,'dividendYield'].fillna(0)
st.markdown("Now let's check whether the data still has some missing values.")
st.code(
   '''
    df_with_na = df[df.isna().any(axis=1)]
    df_with_na
   ''' ,
   language="python"
)
df_with_na = df[df.isna().any(axis=1)]
st.table(df_with_na)
st.markdown("As you can see, some companies has no `PE ratio` this can be occurs when the company has negative earnings. Moreover, `GULF` has no `ytdPercentChange`. Since GULF is a newly listed security on the Stock Exchange of Thailand (SET), with its trading commencing on April 3, 2025, it does not yet have a 52-week return available.")
st.markdown("For simpliciy, I will ditch all of the above symbol.")
st.code(
   '''
   df = df.dropna().reset_index(drop=True)
   ''' ,
   language="python"
)

st.markdown("This is the end of data mangement section. The next session I will dive into the calculate.")
st.divider()

###############
# Calculation #
###############

st.markdown("### Calculation")
st.markdown('''
            I will calculate a **composite score** in order to ranking stocks. Using the equal weighted average of
            - -Z(Z(P/E) , Z(P/BV)) => Value
            - -Z(marketCap) => Size
            - -Z(beta) => Volatility
            - Z(ytdPercentChange) => Momentum
            - Z(dividendYield) => Dividend Yield
            - Z(Z(ROE) , -Z(DE)) => Quality
            ''')
st.markdown("Remark: I use negative z-score for `P/E`, `P/BV`, `marketCap`, `beta`, and `DE` because lower those value are better.")
st.code('''
        # --------------------------- [ Value ] ---------------------------
        # Calculate a z-score of P/E.
        df.loc[:,'z_pe'] = zscore(df['pe'], axis=0)
        # Calculate a z-score of P/BV.
        df.loc[:,'z_pb'] = zscore(df['pb'], axis=0)
        # Calculate an average of P/E and P/BV.
        df.loc[:,'val'] = df[['z_pe','z_pb']].mean(axis=1)
        # Convert the average to z-score.
        df.loc[:,'val'] = zscore(df['val'], axis=0)
        # Apply negative.
        df.loc[:,'val'] = -df.loc[:,'val']
        
        # --------------------------- [ Size ] ---------------------------
        # Calculate a z-score of marketCap.
        df.loc[:,'size'] = zscore(df['marketCap'], axis=0)
        # Apply negative.
        df.loc[:,'size'] = -df.loc[:,'size']
        
        # ------------------------ [ Volatility ] ------------------------
        # Calculate a z-score of beta.
        df.loc[:,'vol'] = zscore(df['beta'], axis=0)
        # Apply negative.
        df.loc[:, 'vol'] = -df.loc[:, 'vol']
        
        # ------------------------- [ Momentum ] -------------------------
        # Calculate a z-score of ytdPercentChange.
        df.loc[:,'mome'] = zscore(df['ytdPercentChange'], axis=0)
        
        # ---------------------- [ Dividend yield ] ----------------------
        # Calculate a z-score of dividendYield.
        df.loc[:,'divYield'] = zscore(df['dividendYield'], axis=0)
        
        # ------------------------- [ Quality ] --------------------------
        # Calculate a z-score of DE ratio.
        df.loc[:,'z_de'] = zscore(df['de'], axis=0)
        # Apply negative.
        df.loc[:,'z_de'] = -df.loc[:,'z_de']
        # Calculate a z-score of ROE.
        df.loc[:,'z_roe'] = zscore(df['roe'], axis=0)
        # Calculate an average of those value.
        df.loc[:,'q'] = df[['z_roe','z_de']].mean(axis=1)
        # Convert the average to Z-score.
        df.loc[:,'q'] = zscore(df['q'], axis=0)
        
        # ---------------------- [ Composite Score ] ----------------------
        # Calculate a composite score.
        df.loc[:,'score'] = df[['val','size','vol','mome','divYield','q']].mean(axis=1)
        # Convert to z-score.
        df.loc[:,'score'] = zscore(df['score'], axis=0)
        ''',
        language="python")

st.markdown("That's all for the calculation. But I will make it easier to visualize it by calculate a `ranking` for both composite and individual factor using the following code.")
st.code('''
        for factor in ['score','val','size','vol','mome','divYield','q']:
            df.loc[:,f'rank_{factor}'] = df.loc[:, f'{factor}'].rank(pct=True)
        ''')


st.markdown("Done!")
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