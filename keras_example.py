import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Activation, Dense
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.metrics import categorical_crossentropy

train_labels = []
train_samples = []

physical_devices = tf.config.experimental.list_physical_devices('GPU')
print('Num GPU Available: ', len(physical_devices))
tf.config.experimental.set_memory_growth(physical_devices[0], True)


model = Sequential([
	Dense(units=16, input_shape=(1,), activation='relu'),
	Dense(units=32, activation='relu'),
	Dense(units=2, activation='softmax')
	])

model.summary()

model.compile(optimizer=Adam(learning_rate=0.0001), loss='sparse_categorical_crossentropy', metrics=['accuracy'])
model.fit(x=scaled_train_samples, y=train_labels, batch_size=10, epochs=30, shuffle=True, verbose=2)
