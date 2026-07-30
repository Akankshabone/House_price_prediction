# 🏠 House Price Prediction System

## 📌 Project Overview

The House Price Prediction System is a Machine Learning web application that predicts the estimated price of a house based on key property features such as:

* House Size (Square Feet)
* Number of Bedrooms
* Number of Bathrooms
* Age of the House
* Distance from City Center

The project uses a **Linear Regression** model trained on historical housing data and provides predictions through a user-friendly **Flask web interface**.

---

## 🚀 Features

* Predict house prices instantly.
* Simple and responsive web interface.
* Machine Learning model trained using Scikit-learn.
* Flask-based backend for prediction handling.
* Interactive result page displaying estimated property value.
* Easy to deploy and customize.

---

## 🛠️ Technologies Used

### Programming Language

* Python

### Machine Learning

* Scikit-learn
* Pandas
* NumPy

### Web Development

* Flask
* HTML5
* CSS3
* Bootstrap 5

### Model

* Linear Regression

---

## 📂 Project Structure

```text
HousePricePredictor/
│
├── app.py
├── model.py
├── trained_model.pkl
├── house_price_dataset_clean.csv
│
├── templates/
│   ├── predict_price.html
│   └── result.html
│
└── README.md
```

---

## ⚙️ How It Works

### Step 1: Data Preparation

The dataset contains housing information including:

* Size of House
* Bedrooms
* Bathrooms
* Age of House
* Distance to City Center
* House Price

The data is cleaned and prepared for training.

### Step 2: Model Training

The Linear Regression algorithm learns the relationship between house features and property prices.

```python
model = LinearRegression()
model.fit(X, y)
```

The trained model is saved using Pickle:

```python
pickle.dump(model, open('trained_model.pkl', 'wb'))
```

### Step 3: Prediction

Users enter house details through the web form.

The application:

1. Receives user input.
2. Loads the trained model.
3. Predicts the house price.
4. Displays the estimated value.

---

## 📊 Input Parameters

| Feature   | Description               |
| --------- | ------------------------- |
| Size      | House size in square feet |
| Bedrooms  | Number of bedrooms        |
| Bathrooms | Number of bathrooms       |
| Age       | Age of the house in years |
| Distance  | Distance from city center |

---

## ▶️ Installation & Setup

### Clone Repository

```bash
git clone https://github.com/your-username/HousePricePredictor.git
cd HousePricePredictor
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows:

```bash
venv\Scripts\activate
```

Mac/Linux:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install flask pandas numpy scikit-learn
```

---

## 🧠 Train the Model

Run:

```bash
python model.py
```

This will generate:

```text
trained_model.pkl
```

---

## 🌐 Run the Application

```bash
python app.py
```

Open:

```text
http://127.0.0.1:5000/
```

---

## 📸 Application Workflow

1. Enter property details.
2. Click **Predict Price**.
3. Model processes inputs.
4. Predicted house price is displayed.

---

## 🔮 Future Enhancements

* Support multiple machine learning algorithms.
* Improve prediction accuracy using advanced models.
* Add data visualization dashboards.
* Deploy on cloud platforms such as Render, Railway, or AWS.
* Integrate location-based pricing features.
* Add model performance metrics and analytics.

---

## 🎯 Learning Outcomes

This project demonstrates:

* Machine Learning model development.
* Data preprocessing and feature selection.
* Model serialization using Pickle.
* Flask web application development.
* Frontend and backend integration.
* End-to-end ML project deployment workflow.

---

## 👩‍💻 Author

**Akanksha Bone**

Machine Learning & Python Developer

---

## 📜 License

This project is developed for educational and learning purposes. Feel free to modify and enhance it for your own projects.
