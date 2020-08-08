import tensorflow as tf
import numpy as np

# https://pythonprogramming.net/introduction-deep-learning-python-tensorflow-keras/
mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()

x_train = tf.keras.utils.normalize(x_train, axis=1)
x_test = tf.keras.utils.normalize(x_test, axis=1)

x_train = np.expand_dims(x_train, axis=3)
x_test = np.expand_dims(x_test, axis=3)

# https://www.kaggle.com/cdeotte/how-to-choose-cnn-architecture-mnist
model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Conv2D(32, (5,5), activation='relu', input_shape=(28,28,1)))
model.add(tf.keras.layers.MaxPool2D(pool_size=(2,2)))
model.add(tf.keras.layers.Conv2D(64, (5,5), activation='relu', input_shape=(28,28,1)))
model.add(tf.keras.layers.MaxPool2D(pool_size=(2,2)))
model.add(tf.keras.layers.Dropout(0.3))
model.add(tf.keras.layers.Flatten())
model.add(tf.keras.layers.Dense(128, activation='relu'))
model.add(tf.keras.layers.Dropout(0.2))
model.add(tf.keras.layers.Dense(10, activation='softmax'))

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(x_train, y_train, epochs=5)

val_loss, val_acc = model.evaluate(x_test, y_test)
print("validate loss: ", val_loss)  # 0.0272
print("validate acc: ", val_acc)    # 0.9921

model.save('model')