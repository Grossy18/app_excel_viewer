import streamlit as st
import pandas as pd

st.set_page_config(page_title="📊 Excel Viewer", layout="wide")

st.title("📄 Upload and View Excel File")

uploaded_file = st.file_uploader("Upload Excel file", type=["xlsx"])

if uploaded_file:
    try:
        df = pd.read_excel(uploaded_file)
        st.success("✅ File loaded successfully!")
        st.dataframe(df)
    except Exception as e:
        st.error(f"❌ Error reading file: {e}")
