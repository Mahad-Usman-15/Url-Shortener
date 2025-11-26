import streamlit as st
import pyshorteners
from pydantic import BaseModel,AnyHttpUrl, ValidationError
class IsUrl(BaseModel):
    is_url_format: AnyHttpUrl
st.title("🔗 URL Shortener")
st.markdown("This is the small project of url shortner")
long_url = st.text_input("Enter the Url",placeholder="Enter the Url")
s = pyshorteners.Shortener()
if st.button("Generate URL"):
    try:
      IsUrl(is_url_format=long_url)
      short_url = s.tinyurl.short(long_url)
      st.success(f"Original URL: {long_url}")
      st.success(f"Shortened URL: {short_url}")
    except ValidationError as e:
     st.error(f"Validation error: {e}") 