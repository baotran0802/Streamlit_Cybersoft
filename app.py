#This is Streamlit app
import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Ask your CSV",
    page_icon="📊",
    layout="wide"
)
if "message" not in st.session_state:
    st.session_state.message = []
if "df" not in st.session_state:
    st.session_state.df = None
if "data summary" not in st.session_state:
    st.session_state.data_summary = None

st.title("Ask your CSV")
st.markdown("Upload your data and ask question in plain English")

#Sidebar for file upload
with st.sidebar:
    st.header("Data Upload")
    uploaded_file =st.file_uploader("Upload a CSV file", type=['csv'])

    if uploaded_file:
        try:
            df =pd.read_csv(uploaded_file)
            st.success(f"Loaded {df.shape[0]} rows x {df.shape[1]} columns.")

            #Data preview
            with st.expander("Preview Data"):
                st.dataframe(df.head())
                #basic stats
                with st.expander("Data summary"):
                    col1, col2 = st.columns(2)
                    with col1:
                        st.metric("Total Rows", df.shape[0])
                        st.metric("Total Columns", df.shape[1])
                    with col2:
                        st.metric("Memory Usage", f"{df.memory_usage().sum() / 1024:.1f} KB")
                        st.metric("Missing Values", df.isnull().sum().sum())
        except Exception as e:
            st.error(f"Error reading file: {str(e)}")
