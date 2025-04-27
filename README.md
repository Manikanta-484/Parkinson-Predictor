# 🧠 Parkinson's Disease Predictor

This is a web application built with **Streamlit** that predicts whether a person has **Parkinson's Disease** based on vocal measurements.  
The model was trained using machine learning techniques and deployed using **Streamlit Cloud**.

---

## 🚀 Features

- Predict Parkinson's Disease by entering 22 vocal measurements.
- Paste all input values separated by commas and auto-fill the form.
- Instant and user-friendly prediction result.
- Deployed online with Streamlit for easy access.

---

## 📂 Project Structure

```
parkinson-predictor/
├── app.py                # Main Streamlit application
├── parkinsons_model.pkl   # Pre-trained ML model
├── scaler.pkl             # StandardScaler fitted on training data
├── requirements.txt       # List of Python libraries required
└── README.md              # Project documentation (this file)
```

---

## ⚙️ Installation (Local Setup)

1. **Clone** the repository:
   ```bash
   git clone https://github.com/yourusername/parkinson-predictor.git
   cd parkinson-predictor
   ```

2. **Install** required libraries:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run** the Streamlit app:
   ```bash
   streamlit run app.py
   ```

---

## 🛠 Requirements

- Python 3.7 or higher
- Libraries:
  - streamlit
  - scikit-learn
  - joblib
  - numpy

(Automatically installed when you run `pip install -r requirements.txt`)

---

## 🌐 Live Demo

You can try the live app here:  
👉 [**Click to Open App**](https://your-streamlit-deployment-link)

---

## ✨ How to Use

1. Open the app.
2. Paste all 22 feature values separated by commas, like:
   ```
   119.99200,157.30200,74.99700,0.00784,0.00007,0.00370,0.00554,0.01109,0.04374,0.42600,0.02182,0.03130,0.02971,0.06545,0.02211,21.03300,0.414783,0.815285,-4.813031,0.266482,2.301442,0.284654
   ```
3. Click the **"Fill"** button to auto-fill the individual fields.
4. Adjust values if needed.
5. Click **"Predict"** to see if the person has Parkinson's Disease.

---

## 📜 License

This project is licensed for educational and personal use.

---

## 🤝 Acknowledgments

- Streamlit Team
- Scikit-Learn Documentation
- Kaggle Parkinson’s Dataset

---

> Developed with ❤️ by **Manikanta**
