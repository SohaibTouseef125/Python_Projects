import streamlit as st
import pandas as pd
import requests
import datetime
import random

# Set Page Config
st.set_page_config(page_title="Growth Mindset Challenge", page_icon="🌱", layout="wide")

# Dark Mode Toggle
if "dark_mode" not in st.session_state:
    st.session_state.dark_mode = False

def apply_dark_mode():
    st.markdown(
        """
        <style>
            body { background-color: #222; color: white; }
            .stButton>button { background-color: #444; color: white; }
        </style>
        """, unsafe_allow_html=True
    )

if st.button("🌙 Toggle Dark Mode"):
    st.session_state.dark_mode = not st.session_state.dark_mode

if st.session_state.dark_mode:
    apply_dark_mode()

# Fetch Motivational Quotes
quote_url = "https://type.fit/api/quotes"
try:
    response = requests.get(quote_url, timeout=5)
    response.raise_for_status()
    quote_data = response.json()
    random_quote = random.choice(quote_data)
    quote_text = f"> **{random_quote['text']}** - *{random_quote.get('author', 'Unknown')}*"
except requests.exceptions.RequestException:
    quote_text = "> **Keep pushing forward!** - *Anonymous*"

st.sidebar.markdown(quote_text)

# User Progress Tracker
st.title("🌱 Growth Mindset Challenge")
st.subheader("Track Your Learning Progress")

date_today = datetime.date.today()

if "progress_data" not in st.session_state:
    st.session_state.progress_data = []

goal = st.text_input("🎯 Enter today's learning goal:")
progress = st.slider("📊 How much progress did you make?", 0, 100, 50)

if st.button("Save Progress"):
    if goal:
        st.session_state.progress_data.append({"date": str(date_today), "goal": goal, "progress": progress})
        st.success("✅ Progress saved!")
    else:
        st.warning("⚠️ Please enter a learning goal before saving.")

# Show progress history
df = pd.DataFrame(st.session_state.progress_data)
if not df.empty:
    st.write("### Your Progress Over Time")
    st.line_chart(df.set_index("date")["progress"])

# Daily Journal Feature
st.subheader("📝 Daily Journal")
if "journal_entries" not in st.session_state:
    st.session_state.journal_entries = []

journal_text = st.text_area("Write about today's learning experience:")
if st.button("Save Journal Entry"):
    if journal_text.strip():
        st.session_state.journal_entries.append({"date": str(date_today), "entry": journal_text})
        st.success("✅ Journal entry saved!")
    else:
        st.warning("⚠️ Journal entry cannot be empty.")

# Show Journal Entries
if st.session_state.journal_entries:
    st.write("### Past Journal Entries")
    for entry in reversed(st.session_state.journal_entries):
        st.markdown(f"**{entry['date']}** - {entry['entry']}")

# Resources Section
st.subheader("📚 Useful Learning Resources")
st.markdown("""
- [🔗 Growth Mindset - Carol Dweck](https://www.mindsetworks.com/science/)
- [📖 Article: Developing a Growth Mindset](https://www.edutopia.org/article/developing-growth-mindset)
- [🎥 Video: The Power of Belief](https://www.youtube.com/watch?v=pN34FNbOKXc)
- [💡 Free Courses on Coursera](https://www.coursera.org/)
- [Growth Mindset Guide](https://www.mindsetworks.com)
- [Streamlit Documentation](https://docs.streamlit.io)
""")

# Footer
st.write("---")
st.write("This app was built using **Streamlit**. Keep learning and growing! 🚀")
