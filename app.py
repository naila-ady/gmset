# import streamlit as st
# import pandas as pd
# import os
# from io import BytesIO

# # Set up our App

# st.set_page_config(page_title="📀 Data sweper", layout="wide")
# st.title("📀 Data sweper")
# st.write("""Transforming your files between CSV and Excel format wit built in data and visualization""")

# # saving files

# uploaded_files=st.file_uploader("upload ur files( csv or excel files):", type=["csv" ,"xlsx"],
#                                 accept_multiple_files=True)

# if uploaded_files:
#     for  files in uploaded_files:
#         files_ext = os.path.splitext(files.name)[-1].lower()

#         if files_ext ==".csv":
#             df =pd.read_csv(files)
#         elif files_ext == ".xlsx":
#             df = pd.read_excel(files)
#         else: 
#             st.error(f"Unsupported file type: {files_ext}")
#             continue

# # dispaly file info
#         st.write(f"*file name:* {files.name}")
#         st.write(f"file size{files.size/1024}")

#         st.write("preview the head of the dataframe")
#         st.dataframe(df.head())

#         #options for data cleaning
#         st.subheader("Data Cleaning process")
#         if st.checkbox(f"cleaning data for filename:{files.name}"):
#             col1, col2 = st.columns(2)
#             with col1:
#                 if st.button(f"Remove duplicate files:{files.name}"):
#                  df.drop_duplicates(inplace=True)
#                 st.write("Duplicate Recovered")
#             with col2:
#                 if st.button(f"Fill mising Values for: {files.name}"):
#                     numeric_cols = df.select_dtypes(include=["number"]).columns
#                     df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
#                     st.write("Missing Values have been filled")
                    
#                     #v
#     st.subheader("Data Visualization")
#     if st.checkbox(f"show visualization for: {files.name}"):
#         st.bar_chart(df.select_dtypes(include="number").iloc[: ,:2])
        
#         # convert to excel ->csv to excel
#         st.subheader("📎Conversion Options")
#         conversion_type= st.radio(f"convert {files.name} to :",["CSV" ,"Excel"], key=files.name)
#         if st.button(f"Convert {files.name}"):
#             buffer=BytesIO()
#         if conversion_type =="CSV":
#              df.to_csv(buffer,index=False)
#              file_name =files.name.replace(files_ext,".csv")
#              mime_type="text/csv"
             
             
             
#         elif conversion_type =="Excel":
#              df.to_excel(buffer,index=False)
#              file_name =files.name.replace(files_ext,".xlsx")
#              mime_type="application/vnd.openxmlformats-officedocuments.spreadsheetml.sheet"
#         buffer.seek(0)
             
#              #download button
#         st.success("All files processed")
             
            
import streamlit as st
import pandas as pd
import os
from io import BytesIO

# Set up our App
st.set_page_config(page_title="📀 Data Sweper", layout="wide")
st.title("📀 Data Sweper")
st.write("""Transforming your files between CSV and Excel format with built-in data cleaning and visualization.""")

# Upload files
uploaded_files = st.file_uploader("Upload your files (CSV or Excel):", type=["csv", "xlsx"], accept_multiple_files=True)

if uploaded_files:
    for file in uploaded_files:
        file_ext = os.path.splitext(file.name)[-1].lower()

        # Read the file
        if file_ext == ".csv":
            df = pd.read_csv(file)
        elif file_ext == ".xlsx":
            df = pd.read_excel(file)
        else:
            st.error(f"Unsupported file type: {file_ext}")
            continue

        # Display file info
        st.write(f"*File name:* {file.name}")
        st.write(f"File size: {file.size / 1024:.2f} KB")

        # Display a preview of the dataframe
        st.write("Preview of the dataframe:")
        st.dataframe(df.head())

        # Data cleaning process
        st.subheader("Data Cleaning Process")
        if st.checkbox(f"Clean data for: {file.name}"):
            col1, col2 = st.columns(2)
            with col1:
                if st.button(f"Remove duplicates for: {file.name}"):
                    df.drop_duplicates(inplace=True)
                    st.write("Duplicate rows removed.")
            with col2:
                if st.button(f"Fill missing values for: {file.name}"):
                    numeric_cols = df.select_dtypes(include=["number"]).columns
                    df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
                    st.write("Missing values have been filled.")

        # Data visualization
        st.subheader("Data Visualization")
        if st.checkbox(f"Show visualization for: {file.name}"):
            st.bar_chart(df.select_dtypes(include="number").iloc[:, :2])

        # Convert to Excel/CSV
        st.subheader("📎 Conversion Options")
        conversion_type = st.radio(f"Convert {file.name} to:", ["CSV", "Excel"], key=file.name)
        if st.button(f"Convert {file.name}"):

            # Initialize the buffer here before usage
            buffer = BytesIO()  # Create in-memory buffer

            if conversion_type == "CSV":
                df.to_csv(buffer, index=False)
                file_name = file.name.replace(file_ext, ".csv")
                mime_type = "text/csv"
            elif conversion_type == "Excel":
                df.to_excel(buffer, index=False)
                file_name = file.name.replace(file_ext, ".xlsx")
                mime_type = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"

            # Seek to the start of the buffer before downloading
            buffer.seek(0)

            # Provide a download button for the converted file
            st.download_button(
                label=f"Download {file_name}",
                data=buffer,
                file_name=file_name,
                mime=mime_type
            )

        st.success("All files processed successfully.")
