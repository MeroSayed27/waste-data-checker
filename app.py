import streamlit as st
import pandas as pd

st.title("♻️ Waste Data Quality Dashboard")
st.write("Upload your dataset to analyze waste data quality.")

uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    # Load raw data
    df = pd.read_csv(uploaded_file)

    original_total = len(df)

    # Clean data
    cleaned_df = df[df["quantity_kg"] > 0]
    cleaned_df = cleaned_df[cleaned_df["location"] != ""]

    clean_records = len(cleaned_df)
    removed_records = original_total - clean_records
    quality_score = (clean_records / original_total) * 100

    st.subheader("Cleaned Data")
    st.dataframe(cleaned_df)

    col1, col2, col3 = st.columns(3)
    col1.metric("Total Records", original_total)
    col2.metric("Clean Records", clean_records)
    col3.metric("Removed Records", removed_records)

    st.subheader("Summary")
    st.write(f"Total records: {original_total}")
    st.write(f"Clean records: {clean_records}")
    st.write(f"Removed records: {removed_records}")
    st.write(f"Data Quality Score: {quality_score:.2f}%")

    st.subheader("Waste Type Distribution")
    st.bar_chart(cleaned_df["waste_type"].value_counts())

    csv = cleaned_df.to_csv(index=False).encode("utf-8")
    st.download_button(
        "Download Cleaned CSV",
        csv,
        "cleaned_waste_data.csv",
        "text/csv"
    )

else:
    st.warning("Please upload a CSV file to continue.")