# import streamlit as st
# import pandas as pd
# import os
# from io import BytesIO
# from  pathlib import Path

# names=["Mustafa" ,"Ali"]
# userName=["mMustafa" ,"mAli"]
# passwords=["123xyz" ,"789abc"]

# # Set up our App
# st.set_page_config(page_title="📀 Data Sweper", layout="wide")
# st.title("📀 Data Sweper")
# st.write("""Transforming your files between CSV and Excel format with built-in data cleaning and visualization.""")


# # Check if user is logged in
# if 'logged_in' not in st.session_state:
#     st.session_state['logged_in'] = False

# # Login functionality
# if not st.session_state['logged_in']:
#     with st.form(key="login_form"):
#         username = st.text_input("Username")
#         password = st.text_input("Password", type="password")
#         submit_button = st.form_submit_button("Login")
        
#         if submit_button:
#             if username in userName and password == passwords[userName.index(username)]:
#                 st.session_state['logged_in'] = True
#                 st.success("Login successful! Redirecting...")
#                 st.rerun()  # To reload the app after login
#             else:
#                 st.error("Invalid username or password")

# # If logged in, proceed to the next page
# if st.session_state['logged_in']:
    
 
# # Upload files
#             uploaded_files = st.file_uploader("Upload your files (CSV or Excel):", type=["csv", "xlsx"], accept_multiple_files=True)

# if uploaded_files:
#     for file in uploaded_files:
#         file_ext = os.path.splitext(file.name)[-1].lower()

#         # Read the file
#         if file_ext == ".csv":
#             df = pd.read_csv(file)
#         elif file_ext == ".xlsx":
#             df = pd.read_excel(file)
#         else:
#             st.error(f"Unsupported file type: {file_ext}")
#             continue

#         # Display file info
#         st.write(f"*File name:* {file.name}")
#         st.write(f"File size: {file.size / 1024:.2f} KB")

#         # Display a preview of the dataframe
#         st.write("Preview of the dataframe:")
#         st.dataframe(df.head())

#         # Data cleaning process
#         st.subheader("Data Cleaning Process")
#         if st.checkbox(f"Clean data for:{file.name}"):
#             col1,col2 = st.columns(2)
#             with col1:
#                 if st.button(f"Remove duplicates for: {file.name}"):
#                     df.drop_duplicates(inplace=True)
#                     st.write("Duplicate rows removed.")
#             with col2:
#                 if st.button(f"Fill missing values for: {file.name}"):
#                     numeric_cols = df.select_dtypes(include=["number"]).columns
#                     df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
#                     st.write("Missing values have been filled.")
                    
#                     #choose specific columns to convert 
#                     st.subheader("Select Columns to convert")
#                     columns= st.multiselect(f"choose columns for:{file.name}",df.columns,default=df.columns)
#                     df=df[columns]
#         # Data visualization
#         st.subheader("Data Visualization")
#         if st.checkbox(f"Show visualization for:{file.name}"):
#             st.bar_chart(df.select_dtypes(include="number").iloc[:,:5])

#         # Convert to Excel/CSV
#         st.subheader("📎 Conversion Options")
#         conversion_type = st.radio(f"Convert {file.name} to:", ["CSV", "Excel"], key=file.name)
#         if st.button(f"Convert {file.name}"):

#             # Initialize the buffer here before usage
#             buffer = BytesIO()  # Create in-memory buffer

#             if conversion_type == "CSV":
#                 df.to_csv(buffer, index=False)
#                 file_name = file.name.replace(file_ext, ".csv")
#                 mime_type = "text/csv"
#             elif conversion_type == "Excel":
#                 df.to_excel(buffer, index=False)
#                 file_name = file.name.replace(file_ext, ".xlsx")
#                 mime_type = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"

#             # Seek to the start of the buffer before downloading
#             buffer.seek(0)

#             # Provide a download button for the converted file
#             st.download_button(
#                 label=f"Download {file_name}",
#                 data=buffer,
#                 file_name=file_name,
#                 mime=mime_type
#             )

#         st.success("All files processed successfully.")
import streamlit as st
import pandas as pd
import os
from io import BytesIO
from pathlib import Path

names = ["Mustafa", "Ali"]
userName = ["mMustafa", "mAli"]
passwords = ["123xyz", "789abc"]

# Set up our App
st.set_page_config(page_title="📀 Data Sweper", layout="wide")
st.title("📀 Data Sweper")
st.write("""Transforming your files between CSV and Excel format with built-in data cleaning and visualization.""")

# Check if user is logged in
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

# Login functionality
if not st.session_state['logged_in']:
    with st.form(key="login_form"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        submit_button = st.form_submit_button("Login")
        
        if submit_button:
            if username in userName and password == passwords[userName.index(username)]:
                st.session_state['logged_in'] = True
                st.success("Login successful! Redirecting...")
                st.rerun()  # To reload the app after login
            else:
                st.error("Invalid username or password")

# If logged in, proceed to the next page
if st.session_state['logged_in']:
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
            if st.checkbox(f"Clean data for:{file.name}"):
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

                    # Choose specific columns to convert
                    st.subheader("Select Columns to convert")
                    columns = st.multiselect(f"Choose columns for:{file.name}", df.columns, default=df.columns)
                    df = df[columns]

            # Data visualization
            st.subheader("Data Visualization")
            if st.checkbox(f"Show visualization for:{file.name}"):
                st.bar_chart(df.select_dtypes(include="number").iloc[:, :5])

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
