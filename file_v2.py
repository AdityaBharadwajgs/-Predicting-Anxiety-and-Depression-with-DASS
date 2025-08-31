import streamlit as st
import pickle

# ✅ Custom styling: only colors adjusted as per your request
page_bg = """
<style>
/* Background image for the app */
[data-testid='stAppViewContainer'] {
    background-image: url("https://img.freepik.com/free-photo/still-life-sustainability-concept-arrangement_23-2148996992.jpg?w=2000&t=st=1712302813~exp=1712303413~hmac=877d5b945f8fe728271de92c5f2a7d850374a34607862f96753c7da0aea25a60");
    background-size: cover;
}

/* Sidebar text color */
[data-testid="stSidebar"] {
    color: white;
}

/* Dropdown, radio buttons, input boxes: make inside text white */
div[data-baseweb="select"] * {
    color: white !important;
}

div[data-baseweb="radio"] label {
    color: white !important;
}

input, select, textarea {
    color: white !important;
}

/* Button text white */
.stButton > button {
    color: white !important;
}

/* Recommendation table text (over light background) — force black */
h3, table, th, td {
    color: black !important;
}

/* Ensure main body headings and text stay black */
[data-testid="stMarkdownContainer"] h1,
[data-testid="stMarkdownContainer"] h2,
[data-testid="stMarkdownContainer"] p,
[data-testid="stMarkdownContainer"] li {
    color: black !important;
}
</style>
"""


# Load the saved SVC models
with open("a_svc_model.pkl", "rb") as f:
    svc_model_anxiety = pickle.load(f)

with open("d_svc_model.pkl", "rb") as f:
    svc_model_depression = pickle.load(f)

# Questionnaire questions
questions_anxiety = {
    "I was aware of dryness of my mouth": ["Did not apply to me at all", "Applied to me to some degree, or some of the time", "Applied to me to a considerable degree or a good part of time","Applied to me very much or most of the time"],
    "I experienced breathing difficulty (e.g. excessively rapid breathing, breathlessness in the absence of physical exertion)": ["Did not apply to me at all", "Applied to me to some degree, or some of the time", "Applied to me to a considerable degree or a good part of time","Applied to me very much or most of the time"],
    "I experienced trembling (e.g. in the hands)": ["Did not apply to me at all", "Applied to me to some degree, or some of the time", "Applied to me to a considerable degree or a good part of time","Applied to me very much or most of the time"],
    "I was worried about situations in which I might panic and make a fool of myself": ["Did not apply to me at all", "Applied to me to some degree, or some of the time", "Applied to me to a considerable degree or a good part of time","Applied to me very much or most of the time"],
    "I felt I was close to panic": ["Did not apply to me at all", "Applied to me to some degree, or some of the time", "Applied to me to a considerable degree or a good part of time","Applied to me very much or most of the time"],
    "I was aware of the action of my heart in the absence of physical exertion (e.g. sense of heart rate increase, heart missing a beat)": ["Did not apply to me at all", "Applied to me to some degree, or some of the time", "Applied to me to a considerable degree or a good part of time","Applied to me very much or most of the time"],
    "I felt scared without any good reason": ["Did not apply to me at all", "Applied to me to some degree, or some of the time", "Applied to me to a considerable degree or a good part of time","Applied to me very much or most of the time"]
}

questions_depression = {
    "I couldn't seem to experience any positive feeling at all": ["Did not apply to me at all", "Applied to me to some degree, or some of the time", "Applied to me to a considerable degree or a good part of time","Applied to me very much or most of the time"],
    "I found it difficult to work up the initiative to do things": ["Did not apply to me at all", "Applied to me to some degree, or some of the time", "Applied to me to a considerable degree or a good part of time","Applied to me very much or most of the time"],
    "I felt that I had nothing to look forward to": ["Did not apply to me at all", "Applied to me to some degree, or some of the time", "Applied to me to a considerable degree or a good part of time","Applied to me very much or most of the time"],
    "I felt down-hearted and blue": ["Did not apply to me at all", "Applied to me to some degree, or some of the time", "Applied to me to a considerable degree or a good part of time","Applied to me very much or most of the time"],
    "I was unable to become enthusiastic about anything": ["Did not apply to me at all", "Applied to me to some degree, or some of the time", "Applied to me to a considerable degree or a good part of time","Applied to me very much or most of the time"],
    "I felt I wasn't worth much as a person": ["Did not apply to me at all", "Applied to me to some degree, or some of the time", "Applied to me to a considerable degree or a good part of time","Applied to me very much or most of the time"],
    "I felt that life was meaningless": ["Did not apply to me at all", "Applied to me to some degree, or some of the time", "Applied to me to a considerable degree or a good part of time","Applied to me very much or most of the time"]
}

gender_to_numeric = {"Female": 0, "Male": 1}

# Severity table (white bg + black text)
severity_table_html = """
<div style="background-color: rgba(255, 255, 255, 0.8); padding: 10px; border-radius: 5px; margin-top: 20px;">
    <h3>Severity Score Reference</h3>
    <table style="width: 100%; border-collapse: collapse;">
        <tr style="border: 1px solid black;">
            <th style="border: 1px solid black; padding: 8px; text-align: center;">Severity Labels</th>
            <th style="border: 1px solid black; padding: 8px; text-align: center;">Depression</th>
            <th style="border: 1px solid black; padding: 8px; text-align: center;">Anxiety</th>
        </tr>
        <tr style="border: 1px solid black;">
            <td style="border: 1px solid black; padding: 8px;">Normal</td>
            <td style="border: 1px solid black; padding: 8px; text-align: center;">0-9</td>
            <td style="border: 1px solid black; padding: 8px; text-align: center;">0-7</td>
        </tr>
        <tr style="border: 1px solid black;">
            <td style="border: 1px solid black; padding: 8px;">Mild</td>
            <td style="border: 1px solid black; padding: 8px; text-align: center;">10-13</td>
            <td style="border: 1px solid black; padding: 8px; text-align: center;">8-9</td>
        </tr>
        <tr style="border: 1px solid black;">
            <td style="border: 1px solid black; padding: 8px;">Moderate</td>
            <td style="border: 1px solid black; padding: 8px; text-align: center;">14-20</td>
            <td style="border: 1px solid black; padding: 8px; text-align: center;">10-14</td>
        </tr>
        <tr style="border: 1px solid black;">
            <td style="border: 1px solid black; padding: 8px;">Severe</td>
            <td style="border: 1px solid black; padding: 8px; text-align: center;">21-27</td>
            <td style="border: 1px solid black; padding: 8px; text-align: center;">15-19</td>
        </tr>
        <tr style="border: 1px solid black;">
            <td style="border: 1px solid black; padding: 8px;">Extremely Severe</td>
            <td style="border: 1px solid black; padding: 8px; text-align: center;">28+</td>
            <td style="border: 1px solid black; padding: 8px; text-align: center;">20+</td>
        </tr>
    </table>
</div>
"""

def calculate_prediction(age, gender, user_input, model):
    user_input = [age, gender] + user_input
    prediction = model.predict([user_input])[0]
    return prediction

def home_page():
    st.title("Mental Health Prediction")
    st.markdown("""
    A step towards mental wellness.         
    Illuminate Your Path to Wellness.
    <br><br> Let our questionnaire be your guiding light,<br> illuminating the way towards mental clarity<br> and inner harmony.<br>
    <br>Incorporating mental health<br> assessments into platforms for young<br> people is essential, as it allows for early<br> detection of issues, encourages<br> self-care practices, and facilitates access<br> to support systems, enabling them to<br> navigate life's ups and downs with<br> resilience and well-being.
    """, unsafe_allow_html=True)

def questionnaire_page_anxiety():
    st.title("Anxiety Level Prediction")
    st.write("Please answer the questions below.")

    a_age = st.number_input("Enter your age:", min_value=16, max_value=45, step=1, value=None)
    gender = st.radio("Select your gender:", ["Male", "Female", "Others"], index=0)
    a_gender_numeric = gender_to_numeric.get(gender, None)

    user_input = []
    for question, options in questions_anxiety.items():
        selected_option = st.selectbox(f"{question}:", options)
        user_input.append(options.index(selected_option))

    if st.button("Make Prediction for Anxiety"):
        if a_age is None or gender == "":
            st.error("Please enter your age and select your gender before making a prediction.")
        else:
            a_prediction = calculate_prediction(a_age, a_gender_numeric, user_input, svc_model_anxiety)
            st.write(f"Your Anxiety Score: {a_prediction} / 21")
            st.subheader("Recommendations:")
            if a_prediction in range(0,8):
                st.write("* You are normal!")
                st.write("* Continue with your practices.")
            elif a_prediction in range(8,10):
                st.write("* Get enough sleep.")
                st.write("* Maintain a healthy diet. Include dark chocolate and green tea.")
                st.write("* Try to be physically active.")
            elif a_prediction in range(10,15):
                st.write("* Avoid alcohol and recreational drugs.")
                st.write("* Avoid smoking.")
                st.write("* Try out relaxation techniques like meditation and yoga.")
                st.write("* Limit caffeine intake.")
            elif a_prediction in range(15,20):
                st.write("* Try out pet caring.")
                st.write("* Talk to someone you trust.")
                st.write("* Keep a diary.")
                st.write("* Maintain a healthy diet.")
                st.write("* Limit caffeine intake.")
                st.write("* Avoid smoking.")
            elif a_prediction > 19:
                st.write("* Seek immediate professional help.")
                st.write("* Try out therapy and counseling.")
            st.markdown(severity_table_html, unsafe_allow_html=True)

def questionnaire_page_depression():
    st.title("Depression Level Prediction")
    st.write("Please answer the questions below.")

    d_age = st.number_input("Enter your age:", min_value=16, max_value=45, step=1, value=None)
    gender = st.radio("Select your gender:", ["Male", "Female", "Others"], index=0)
    d_gender_numeric = gender_to_numeric.get(gender, None)

    user_input = []
    for question, options in questions_depression.items():
        selected_option = st.selectbox(f"{question}:", options)
        user_input.append(options.index(selected_option))

    if st.button("Make Prediction for Depression"):
        if d_age is None or gender == "":
            st.error("Please enter your age and select your gender before making a prediction.")
        else:
            d_prediction = calculate_prediction(d_age, d_gender_numeric, user_input, svc_model_depression)
            st.write(f"Your Depression Score: {d_prediction} / 21")
            st.subheader("Recommendations:")
            if d_prediction in range(0, 10):
                st.write("* Practice self-care.")
                st.write("* Maintain social connections.")
                st.write("* Engage in volunteer activities.")
            elif d_prediction in range(10, 14):
                st.write("* Seek social support.")
                st.write("* Practice relaxation techniques like yoga and meditation.")
                st.write("* Monitor progress.")
                st.write("* Engage in enjoyable activities.")
            elif d_prediction in range(14, 21):
                st.write("* Try out therapy.")
                st.write("* Limit sources of stress.")
                st.write("* Monitor progress.")
            elif d_prediction in range(20, 28):
                st.write("* Seek professional help.")
                st.write("* Try out therapy and counseling.")
                st.write("* Prioritize safety.")
                st.write("* Practice meditation.")
            elif d_prediction > 27:
                st.write("* Seek immediate professional help.")
                st.write("* Avoid isolation.")
                st.write("* Try out therapy and counseling.")
            st.markdown(severity_table_html, unsafe_allow_html=True)

def main():
    st.markdown(page_bg, unsafe_allow_html=True)
  # ✅ CSS applied here
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to:", ["Home", "Anxiety Prediction", "Depression Prediction"])

    if page == "Home":
        home_page()
    elif page == "Anxiety Prediction":
        questionnaire_page_anxiety()
    elif page == "Depression Prediction":
        questionnaire_page_depression()

# Run the app
if __name__ == "__main__":
    main()
