import streamlit as st # type: ignore
import pandas as pd
import sweetviz # type: ignore
import os

st.set_page_config(page_title="Auto EDA Tool", layout="wide")
st.title("Auto EDA Tool")
st.write("Upload your CSV file and get a full EDA report instanatly.")

Uploaded_file = st.file_uploader("Upload your CSV", type="csv")

if Uploaded_file:
    df = pd.read_csv(Uploaded_file)
    st.write("### Data Preview", df.head())
    
    if st.button("Generate EDA Report"):
        report = sweetviz.analyze(df)
        report_path = "EDA_Report.html"
        report.show_html(report_path, open_browser=False)
        
        with open(report_path, "r", encoding="utf-8") as f:
            html_content = f.read()
            st.components.v1.html(html_content, height=1000, scrolling=True)