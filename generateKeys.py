import pickle
from pathlib import Path
import streamlit_authenticator as stauth
import streamlit as st

names=["Mustafa" ,"Ali"]
userName=["mMustafa" ,"mAli"]
passwords=["123xyz" ,"789abc"]
 
# hashed_passwords = stauth.Hasher(passwords).generate_hashes()
# file_path=Path(__file__).parent
# with file_path.open("wb") as file:
#     pickle.dump(hashed_passwords ,file)
with st.form(key="my_form"):
    username = st.text_input("Username")
    password = st.text_input("Password")
    st.form_submit_button("Login")

