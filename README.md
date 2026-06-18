# 🎓 College Admission Predictor

Predict a student's probability of getting admission to a graduate program using Machine Learning and an interactive Streamlit web application.

## 🚀 Features

* Predict admission chances based on academic profile
* Interactive Streamlit Web Interface
* Linear Regression Model
* Data Analysis using Pandas & NumPy
* Model Training with Scikit-Learn
* Visualization using Matplotlib
* Jupyter Notebook for experimentation

---

## 📂 Project Structure

```text
College-Admission-Predictor/
│
├── app.py
├── admission_predict.csv
├── Admission prediction.ipynb
├── requirements.txt
└── README.md
```

---

## 📊 Dataset Features

The model uses the following inputs:

* GRE Score
* TOEFL Score
* University Rating
* SOP Strength
* LOR Strength
* CGPA
* Research Experience

Output:

* Chance of Admission (%)

---

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Scikit-Learn
* Matplotlib
* Streamlit
* Jupyter Notebook

---

## ⚙️ Installation

### Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/College-Admission-Predictor.git
cd College-Admission-Predictor
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux/macOS

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Streamlit Application

```bash
streamlit run app.py
```

or

```bash
python -m streamlit run app.py
```

The application will open in your browser:

```text
http://localhost:8501
```

---

## 📓 Run Jupyter Notebook

```bash
jupyter notebook
```

Open:

```text
Admission prediction.ipynb
```

and run all cells.

---

## 🎯 Sample Prediction

Input:

```text
GRE Score         : 330
TOEFL Score       : 115
University Rating : 5
SOP               : 4.5
LOR               : 4.5
CGPA              : 9.5
Research          : Yes
```

Output:

```text
Chance of Admission: 92.8%
```

---

## 📈 Model Performance

* Algorithm: Linear Regression
* Cross Validation Accuracy: ~81%
* R² Score: ~0.82

---

## 🤝 Contributing

Contributions, issues and feature requests are welcome.

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

---

## ⭐ Support

If you found this project useful, consider giving it a star on GitHub.

---

Developed by Vedant Ved 🚀
