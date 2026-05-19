import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Input

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix

dataset = pd.read_csv('iris.csv', header=None)

X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

label_encoder = LabelEncoder()
y = label_encoder.fit_transform(y)

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = Sequential([
    Input(shape=X_train.shape[1:]),

    Dense(1000, activation='relu'),
    Dense(500, activation='relu'),
    Dense(300, activation='relu'),

    Dense(3, activation='softmax')
])

model.summary()

model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

history = model.fit(
    X_train,
    y_train,
    epochs=50,
    batch_size=32,
    validation_data=(X_test, y_test)
)

loss, accuracy = model.evaluate(X_test, y_test)

print(f"\nLoss: {loss}")
print(f"Accuracy: {accuracy}")

pd.DataFrame(history.history).plot(figsize=(10, 6))

plt.title("Training History")
plt.xlabel("Epoch")
plt.ylabel("Value")
plt.grid(True)

# Menyimpan grafik history
plt.savefig('training_history.png')
plt.show()

predictions = model.predict(X_test)

predicted_classes = predictions.argmax(axis=1)

print("\nPrediksi:")
print(predicted_classes)

print("\nLabel Asli:")
print(y_test)

cm = confusion_matrix(y_test, predicted_classes)

plt.figure(figsize=(8, 6))

sns.heatmap(
    cm,
    annot=True,
    fmt='d',
    cmap='Blues',
    xticklabels=label_encoder.classes_,
    yticklabels=label_encoder.classes_
)

plt.xlabel('Predicted')
plt.ylabel('True')
plt.title('Confusion Matrix')

# Menyimpan grafik confusion matrix
plt.savefig('confusion_matrix.png')
plt.show()

def predict_new_data():

    sepal_length = float(input("Masukkan sepal length: "))
    sepal_width = float(input("Masukkan sepal width: "))
    petal_length = float(input("Masukkan petal length: "))
    petal_width = float(input("Masukkan petal width: "))

    new_data = np.array([
        [
            sepal_length,
            sepal_width,
            petal_length,
            petal_width
        ]
    ])

    prediction = model.predict(new_data)

    predicted_class = prediction.argmax(axis=1)

    predicted_label = label_encoder.inverse_transform(predicted_class)

    print(f"\nPrediksi kelas: {predicted_label[0]}")

predict_new_data()