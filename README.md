# 🧠 Mental Health Prediction System

A **Streamlit-based web application** that predicts **Anxiety** and **Depression** levels using the **DASS-21 (Depression, Anxiety, and Stress Scale)** questionnaire. This project integrates **Machine Learning (SVC models)** to analyze user responses and provide severity scores with personalized recommendations.

---

## 🌟 Features
- 📋 **Interactive Questionnaire** – Users answer validated mental health-related questions.
- 🤖 **Machine Learning Models** – Predicts severity of anxiety and depression using trained **SVC models**.
- 🎨 **Modern UI/UX** – Styled with custom CSS for a clean and professional interface.
- 📊 **Severity Score Table** – Displays classification ranges for easy interpretation.
- 💡 **Personalized Suggestions** – Provides actionable tips and wellness practices.
- 🌐 **Web-Based** – Runs easily with **Streamlit**, deployable on **Streamlit Cloud** or other hosting platforms.

---

## 🔧 Tech Stack
- **Python 3**
- **Streamlit** (frontend & backend)
- **scikit-learn** (machine learning)
- **Pickle** (model storage & loading)

---

## 📂 Project Structure
```
Mental-Health-Prediction/
│── file_v2.py                # Main Streamlit app
│── a_svc_model.pkl           # Trained SVC model for Anxiety
│── d_svc_model.pkl           # Trained SVC model for Depression
│── README.txt                # Project documentation
│── requirements.txt          # Required dependencies
```

---

## ⚙️ Installation & Setup

1. **Clone this repository**
```bash
git clone https://github.com/your-username/Mental-Health-Prediction.git
cd Mental-Health-Prediction
```

2. **Create a virtual environment (optional but recommended)**
```bash
python -m venv venv
source venv/bin/activate     # On macOS/Linux
venv\Scripts\activate        # On Windows
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Run the app**
```bash
streamlit run file_v2.py
```

---

## 📊 Severity Levels (DASS-21 Reference)

| Severity        | Depression Score | Anxiety Score |
|-----------------|------------------|---------------|
| Normal          | 0 – 9            | 0 – 7         |
| Mild            | 10 – 13          | 8 – 9         |
| Moderate        | 14 – 20          | 10 – 14       |
| Severe          | 21 – 27          | 15 – 19       |
| Extremely Severe| 28+              | 20+           |

---

## 🚀 Deployment
You can easily deploy this project on:
- Streamlit Community Cloud
- Heroku / Render / AWS

To deploy on **Streamlit Cloud**:
1. Push this repo to GitHub.
2. Go to Streamlit Cloud.
3. Connect your GitHub repo and deploy.

---

## 📸 Screenshots (Optional)
_Add sample screenshots of your app here after running it._

---

## 👨‍💻 Author
Developed by **Aditya** ✨
Feel free to contribute, raise issues, or fork this project!
