import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Analyvora",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Analyvora")
st.subheader("Intelligent Data Analytics Platform")

st.markdown("---")

uploaded_file = st.file_uploader(
    "Upload your dataset",
    type=["csv", "xlsx"]
)

if uploaded_file is not None:

    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)

    else:
        df = pd.read_excel(uploaded_file)

    st.success("Dataset uploaded successfully!")

    st.write("### Dataset Preview")

    st.dataframe(df.head())

    st.write("## Dataset Information")

    col1, col2, col3 = st.columns(3)

    col1.metric("Rows", df.shape[0])

    col2.metric("Columns", df.shape[1])

    col3.metric("Missing Values", df.isnull().sum().sum())

    st.write("### Data Types")

    st.dataframe(df.dtypes.astype(str))
