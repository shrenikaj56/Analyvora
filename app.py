import streamlit as st
from utils.data_loader import load_dataset
from utils.data_health import (
    get_total_rows,
    get_total_columns,
    get_missing_values,
    get_duplicate_rows,
    get_numeric_columns,
    get_categorical_columns,
    get_missing_percentage,
    get_duplicate_percentage,
    get_missing_table,
    get_quality_score,
    get_recommendations,
)

# -------------------- Page Configuration --------------------

st.set_page_config(
    page_title="Analyvora",
    page_icon="📊",
    layout="wide"
)

# -------------------- Header --------------------

st.title("📊 Analyvora")
st.subheader("Intelligent Data Analytics Platform")

st.markdown("---")

# -------------------- File Upload --------------------

uploaded_file = st.file_uploader(
    "Upload your dataset",
    type=["csv", "xlsx"]
)

# -------------------- Main Application --------------------

if uploaded_file is not None:

    # Load Dataset
    df = load_dataset(uploaded_file)

    st.success("✅ Dataset uploaded successfully!")

    # Dataset Preview
    st.subheader("📄 Dataset Preview")
    st.dataframe(df.head())

    # -------------------- Data Health Summary --------------------

    st.markdown("---")
    st.subheader("📊 Data Health Summary")

    col1, col2, col3 = st.columns(3)

    col1.metric("Rows", get_total_rows(df))
    col2.metric("Columns", get_total_columns(df))
    col3.metric("Missing Values", get_missing_values(df))

    col4, col5, col6 = st.columns(3)

    col4.metric("Duplicate Rows", get_duplicate_rows(df))
    col5.metric("Numeric Columns", get_numeric_columns(df))
    col6.metric("Categorical Columns", get_categorical_columns(df))

    # -------------------- Data Types --------------------

    st.markdown("---")
    st.subheader("📋 Data Types")

    data_types = df.dtypes.astype(str).reset_index()
    data_types.columns = ["Column", "Data Type"]

    st.dataframe(data_types)

    # -------------------- Data Quality Score --------------------

    st.markdown("---")
    st.subheader("⭐ Data Quality Score")

    score = get_quality_score(df)

    if score >= 90:
        st.success(f"Excellent Data Quality: {score}%")
    elif score >= 70:
        st.warning(f"Moderate Data Quality: {score}%")
    else:
        st.error(f"Poor Data Quality: {score}%")

    st.progress(score / 100)

    # -------------------- Statistics --------------------

    st.markdown("---")
    st.subheader("📈 Data Statistics")

    col1, col2 = st.columns(2)

    col1.metric(
        "Missing %",
        f"{get_missing_percentage(df)}%"
    )

    col2.metric(
        "Duplicate %",
        f"{get_duplicate_percentage(df)}%"
    )

    # -------------------- Missing Values Table --------------------

    st.markdown("---")
    st.subheader("📌 Missing Values by Column")

    missing_table = get_missing_table(df)

    if not missing_table.empty:
        st.dataframe(missing_table)
    else:
        st.success("✅ No missing values found.")

    # -------------------- Recommendations --------------------

    st.markdown("---")
    st.subheader("💡 Recommendations")

    recommendations = get_recommendations(df)

    for recommendation in recommendations:
        st.info(recommendation)

else:
    st.info("👆 Upload a CSV or Excel file to begin analysis.")