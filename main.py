import kagglehub
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import precision_recall_fscore_support, accuracy_score

# Download latest version
path = kagglehub.dataset_download("rakeshkapilavai/extrovert-vs-introvert-behavior-data")

print("Path to dataset files:", path)
# Display the first few rows of the dataset
import pandas as pd
df = pd.read_csv(path+ "/personality_dataset.csv")
#know the ratio of missing values
print("Missing values in each column:\n", df.isnull().sum())
df = df.dropna()

# Extrovert to 0 introvert to 1
df['Personality'] = df['Personality'].map({'Extrovert': 0, 'Introvert': 1})
df['Stage_fear'] = df['Stage_fear'].map({'Yes': 1, 'No': 0})
df['Drained_after_socializing'] = df['Drained_after_socializing'].map({'Yes': 1, 'No': 0})
x = df.drop(columns=['Personality'])
y = df['Personality']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

scalar = StandardScaler()
x_train = scalar.fit_transform(x_train)
x_test = scalar.transform(x_test)

# probability=True is used to get the probability of each class
model = SVC(probability=True)
model.fit(x_train, y_train)
y_pred = model.predict(x_test)
predicted_prob = model.predict_proba(x_test)
print("Accuracy: ", accuracy_score(y_test, y_pred))
precision, recall, f1, _ = precision_recall_fscore_support(y_test, y_pred, average='binary')
print("Precision: ", precision)
print("Recall: ", recall)   
print("F1 Score: ", f1)

