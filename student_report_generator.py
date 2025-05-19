import streamlit as st
import pandas as pd
import io

# Streamlit UI Title
st.title("📊 Student Report Generator")

# Upload CSV File
uploaded_file = st.file_uploader("📂 Upload a CSV file with student scores", type=["csv"])

if uploaded_file:
    # Load CSV
    df = pd.read_csv(uploaded_file)

    # Display detected columns for debugging
    st.write("📝 **Detected Columns:**", list(df.columns))

    # Convert column names to lowercase for case-insensitive matching
    df.columns = df.columns.str.lower().str.strip()

    # Ensure the required 'id' and 'pass' columns exist
    required_columns = {"id", "pass"}
    if not required_columns.issubset(set(df.columns)):
        st.error(f"⚠️ CSV must contain: {required_columns}. Please check column names.")
    else:
        # Select subject columns dynamically (exclude 'id' and 'pass')
        subject_cols = [col for col in df.columns if col not in {"id", "pass"}]

        if len(subject_cols) < 2:
            st.error("⚠️ CSV must have at least 2 subjects for average calculation.")
        else:
            # Convert subjects to numeric
            df[subject_cols] = df[subject_cols].apply(pd.to_numeric, errors="coerce")

            # Calculate average
            df["Average"] = df[subject_cols].mean(axis=1).round(2)

            # **Fix Pass/Fail Column by Mapping Yes → Pass, No → Fail**
            df["Final Status"] = df["pass"].str.strip().str.lower().map({"yes": "Pass ✅", "no": "Fail ❌"})

            # Display processed report
            st.subheader("📋 Processed Student Report:")
            st.dataframe(df)

            # Bar chart visualization (show only Pass students)
            st.subheader("📊 Student Performance Comparison")
            df_pass = df[df["Final Status"] == "Pass ✅"]
            if not df_pass.empty:
                st.bar_chart(df_pass.set_index("id")[subject_cols + ["Average"]])
            else:
                st.warning("No students passed! Adjust the dataset if necessary.")

            # Download processed report
            output = io.StringIO()
            df.to_csv(output, index=False)
            st.download_button(
                label="📥 Download Processed Report",
                data=output.getvalue(),
                file_name="student_report.csv",
                mime="text/csv",
            )
