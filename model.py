import pandas as pd
import pickle
from sklearn.linear_model import LinearRegression

# Load dataset
df = pd.read_csv('house_price_dataset_clean.csv')

# Features and target
X = df[['Size (sq. ft.)',
        'Bedrooms',
        'Bathrooms',
        'Age of House (Years)',
        'Distance to City Center (Miles)']]

y = df['Price']

# Train model
model = LinearRegression()
model.fit(X, y)

# Save model
with open('trained_model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("Model trained and saved successfully!")