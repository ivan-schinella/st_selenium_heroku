import streamlit as st
from selenium import webdriver

# import chromedriver_autoinstaller
# chromedriver_autoinstaller.install()

chrome_options = webdriver.ChromeOptions()
# chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")

if "driver" not in st.session_state:
    st.session_state.driver = webdriver.Chrome(options=chrome_options)

st.session_state.driver.get('https://www.python.org/')

st.write(st.session_state.driver.title)
print(st.session_state.driver.title)
st.session_state.driver.close()
