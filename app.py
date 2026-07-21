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
from utils.cleaning import (
    remove_duplicates,
    fill_missing_values
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
   

    

    # -------------------- Data Cleaning --------------------

       

    st.markdown("---")
    st.subheader("🧹 Data Cleaning")

    # Create Tabs
    tab1, tab2 = st.tabs(
        ["🗑️ Remove Duplicates", "🩹 Fill Missing Values"]
    )

    # ==================== Remove Duplicate Rows ====================

    with tab1:

        if st.button("Remove Duplicate Rows"):

            cleaned_df = remove_duplicates(df)

            original_rows = len(df)
            cleaned_rows = len(cleaned_df)
            removed_rows = original_rows - cleaned_rows

            if removed_rows == 0:
                st.info("ℹ️ No duplicate rows found.")
            else:
                st.success(f"✅ {removed_rows} duplicate row(s) removed.")

            st.write("### 📄 Cleaned Dataset Preview")

            st.write(
                f"**Rows:** {cleaned_df.shape[0]} | **Columns:** {cleaned_df.shape[1]}"
            )

            st.dataframe(cleaned_df.head())

            csv = cleaned_df.to_csv(index=False).encode("utf-8")

            st.download_button(
                label="📥 Download Cleaned Dataset",
                data=csv,
                file_name="cleaned_dataset.csv",
                mime="text/csv",
                key="download_duplicates"
            )

    # ==================== Fill Missing Values ====================

    with tab2:

        method = st.selectbox(
            "Select Missing Value Handling Method",
            ["Mean", "Median", "Mode"]
        )

        if st.button("Fill Missing Values"):

            cleaned_df = fill_missing_values(df, method)

            st.success(f"✅ Missing values filled using **{method}**.")

            st.write("### 📄 Cleaned Dataset Preview")

            st.write(
                f"**Rows:** {cleaned_df.shape[0]} | **Columns:** {cleaned_df.shape[1]}"
            )

            st.dataframe(cleaned_df.head())

            csv = cleaned_df.to_csv(index=False).encode("utf-8")

            st.download_button(
                label="📥 Download Cleaned Dataset",
                data=csv,
                file_name="cleaned_dataset.csv",
                mime="text/csv",
                key="download_missing"
            )
else:
    st.info("👆 Upload a CSV or Excel file to begin analysis.")