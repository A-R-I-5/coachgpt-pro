import streamlit as st
import openai
import datetime

# App config
st.set_page_config(page_title="CoachGPT Pro", layout="centered")
st.title("🏋️‍♂️ CoachGPT Pro – Business + Fitness AI")

# Set OpenAI key from secrets
openai.api_key = st.secrets["OPENAI_API_KEY"]

# Tabs for coaching and fitness
tab1, tab2 = st.tabs(["🧠 Business Coaching", "💪 Gym Tracker"])

with tab1:
    st.subheader("Business Coaching")
    business_input = st.text_area("Ask your business question:")
    if st.button("Get Advice"):
        if business_input:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a motivating and practical business coach."},
                    {"role": "user", "content": business_input}
                ]
            )
            st.write(response['choices'][0]['message']['content'])

with tab2:
    st.subheader("Log Workout")
    exercise = st.text_input("Exercise (e.g. Squat)")
    sets = st.number_input("Sets", 1, 10, 3)
    reps = st.number_input("Reps", 1, 20, 10)
    weight = st.number_input("Weight (kg)", 0.0, 300.0, 50.0)
    if st.button("Save Workout"):
        today = datetime.date.today()
        with open("gym_log.csv", "a") as f:
            f.write(f"{today},{exercise},{sets},{reps},{weight}\n")
        st.success("Workout saved!")

    st.subheader("Workout History")
    try:
        with open("gym_log.csv", "r") as f:
            st.text(f.read())
    except FileNotFoundError:
        st.info("No logs yet.")
