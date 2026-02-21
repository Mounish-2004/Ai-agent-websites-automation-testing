import streamlit as st
import pandas as pd
import plotly.express as px
import time

from playwright_executor import PlaywrightExecutor
from test_case_parser import generate_test_steps
from report_generator import generate_pdf_report
from history_manager import init_db, save_history, get_user_history
from auth_manager import init_user_db, register_user, login_user

st.set_page_config(page_title="AI Autonomous Testing Platform", layout="wide")

init_db()
init_user_db()

if "authenticated" not in st.session_state:
    st.session_state.authenticated = False
if "username" not in st.session_state:
    st.session_state.username = None

# ---------------- LOGIN ----------------
if not st.session_state.authenticated:

    st.title("🔐 Secure Login")

    tab1, tab2 = st.tabs(["Login", "Register"])

    with tab1:
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        if st.button("Login"):
            if login_user(username, password):
                st.session_state.authenticated = True
                st.session_state.username = username
                st.rerun()
            else:
                st.error("Invalid Credentials")

    with tab2:
        new_user = st.text_input("New Username")
        new_pass = st.text_input("New Password", type="password")

        if st.button("Register"):
            if register_user(new_user, new_pass):
                st.success("Registered Successfully")
            else:
                st.error("Username already exists")

    st.stop()

# ---------------- DASHBOARD ----------------
st.title("🚀 AI Autonomous Web Testing Platform")
st.caption(f"Welcome {st.session_state.username}")

if st.button("Logout"):
    st.session_state.authenticated = False
    st.rerun()

col1, col2 = st.columns(2)

with col1:
    website_url = st.text_input("🌐 Website URL")

with col2:
    headless_mode = st.toggle("Headless Mode", value=False)

natural_query = st.text_area("🧠 Natural Language Test Instructions")

if st.button("Run Test 🚀"):

    if website_url and natural_query:

        with st.spinner("Generating AI test steps..."):
            structured_steps = generate_test_steps(natural_query)

            structured_steps.insert(0, {
                "action": "open",
                "target": website_url,
                "assertions": []
            })

            executor = PlaywrightExecutor(
                headless=headless_mode,
                use_llm_debugging=True
            )

            results = executor.execute_test(
                structured_steps,
                test_name=website_url
            )

            save_history(st.session_state.username, results)

        if results["status"] == "PASS":
            st.success("Test Passed ✅")
        else:
            st.error("Test Failed ❌")

        st.json(results)

        pdf_file = generate_pdf_report(results)

        with open(pdf_file, "rb") as f:
            st.download_button(
                label="Download PDF Report",
                data=f,
                file_name="test_report.pdf",
                mime="application/pdf"
            )

    else:
        st.warning("Enter URL and instructions")

# ---------------- HISTORY ----------------
st.subheader("📊 Your Test History")

history = get_user_history(st.session_state.username)

if history:
    df = pd.DataFrame(history, columns=[
        "ID", "Username", "Test Name",
        "Status", "Execution Time", "Timestamp"
    ])

    st.dataframe(df)

    fig = px.pie(df, names="Status", title="Pass vs Fail")
    st.plotly_chart(fig, use_container_width=True)

else:
    st.info("No tests executed yet.")