import streamlit as st

###############
# PAGE CONFIG #
###############
st.set_page_config(
    page_icon = "👤",
    page_title = "About Me",
    layout="wide"
)
################
# PAGE CONTENT #
################
st.title("👤 About Me")
st.markdown("""
Hi! I'm **Punyawat Pungphomin**, a finance student passionate about data analytics, quantitative investing, and financial technology.  
This project is part of my journey to explore **factor investing strategies** by combining finance theory with Python programming.

I collected and cleaned all the data myself using a custom web scraping script written in Python,  
then analyzed and visualized it with **Pandas**, **SciPy**, and **Streamlit**.

Thank you for your attention!
Feel free to connect or reach out via:
- 📧 Email: punyawat.punphomin@gmail.com  
- 💼 LinkedIn: [punyawatp](www.linkedin.com/in/punyawatp)
""")