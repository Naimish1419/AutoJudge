# AutoJudge – Programming Problem Difficulty Prediction

## 📌 Project Overview
AutoJudge is a machine learning–based system that automatically predicts the **difficulty level of programming problems** using only their textual descriptions.

The project performs **two tasks**:
- **Classification**: Predicts difficulty class — *Easy / Medium / Hard*
- **Regression**: Predicts a numerical **difficulty score**

A simple **Flask web application** is provided to demonstrate real-time predictions.

---

## 📊 Dataset Used
The dataset consists of programming problems collected from online coding platforms.

Each data point contains:
- `title`
- `description`
- `input_description`
- `output_description`
- `problem_class` (Easy / Medium / Hard)
- `problem_score` (numerical difficulty)

The original dataset was provided in **JSONL format** and later converted to CSV for preprocessing and model training.

---

## 🛠 Data Preprocessing
The following preprocessing steps were applied:
- Missing text fields were handled using empty string replacement
- All text fields were concatenated into a single input feature
- The numerical difficulty score was **log-transformed** to reduce skewness

Final input text used for modeling:
```
title + description + input_description + output_description
```

---

## 🔍 Feature Extraction
- **TF-IDF Vectorization**
  - Unigrams, bigrams, and trigrams
  - Stopword removal
  - Sublinear term frequency scaling
  - Maximum features set to 15,000

---

## 🤖 Models Used

### 🔹 Classification Model
- **Random Forest Classifier**
- Task: Predict difficulty class (*Easy / Medium / Hard*)

### 🔹 Regression Model
- **XGBoost Regressor**
- Task: Predict numerical difficulty score

Both models were trained separately and saved using `joblib`.

---

## 📈 Evaluation Metrics

### Classification
- Accuracy
- Confusion Matrix

### Regression
- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)
- R² Score

> Predicting an exact numerical difficulty score from text is inherently noisy.  
> The achieved results are reasonable given the subjective nature of problem difficulty.

---

## 🌐 Web Interface
A **Flask-based web application** allows users to:
1. Enter a programming problem description, input, and output
2. Get:
   - Predicted difficulty class
   - Predicted difficulty score

The application runs **locally** and does not require online hosting.

---

## ▶️ Steps to Run the Project Locally

1. Install required dependencies
```
pip install -r requirements.txt
```

2. Run the Flask application
```
python app.py
```

3. Open the application in browser
```
http://127.0.0.1:5000/
```

---

## 🎥 Demo Video
📌 **Demo Video Link**:  
👉 *(To be added after recording the demo video)*

The demo video shows:
- Brief explanation of the project
- Machine learning approach
- Working web interface with predictions

---

## 📂 Project Structure
```
AutoJudge/
│
├── app.py
├── classifier.pkl
├── regressor.pkl
├── README.md
│
└── templates/
    └── index.html
```

---

## 🧪 Experimental Setup
- Train-test split: 80% training, 20% testing
- Fixed random seed for reproducibility
- Models trained using only textual information (no user statistics)

---

## ✅ Conclusion
This project demonstrates that **problem difficulty can be predicted reasonably well using textual descriptions alone**.

The system integrates:
- Data preprocessing
- Feature extraction
- Classification
- Regression
- Web-based deployment

Future improvements may include:
- Sentence embeddings (BERT)
- Ordinal regression techniques
- Cloud deployment

---

## 👤 Author
**Name**: Naimish Mehta  
**Institute**: IIT Roorkee  
**Enrollment No.**: 23112059

---

## 📎 License
This project is intended for academic and educational purposes only.

