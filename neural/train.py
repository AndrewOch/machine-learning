from keras import datasets, layers, models
from keras.utils import to_categorical
import numpy as np
from PIL import Image
import os

(train_images, train_labels), (test_images, test_labels) = datasets.mnist.load_data()

train_images, test_images = train_images / 255.0, test_images / 255.0


def load_minus_images(folder):
    images = []
    for filename in os.listdir(folder):
        if filename.endswith('.png'):
            img = Image.open(os.path.join(folder, filename)).convert('L')
            img = np.array(img)
            images.append(img)
    return np.array(images)


train_minus_images = load_minus_images('minus/train')
test_minus_images = load_minus_images('minus/test')

train_minus_labels = np.full(train_minus_images.shape[0], 10)
test_minus_labels = np.full(test_minus_images.shape[0], 10)

train_minus_images = train_minus_images / 255.0
test_minus_images = test_minus_images / 255.0

train_images = np.concatenate((train_images, train_minus_images))
test_images = np.concatenate((test_images, test_minus_images))
train_labels = np.concatenate((train_labels, train_minus_labels))
test_labels = np.concatenate((test_labels, test_minus_labels))

train_labels = to_categorical(train_labels, 11)
test_labels = to_categorical(test_labels, 11)

model = models.Sequential()
model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.Flatten())
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dense(11, activation='softmax'))

model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

model.fit(train_images[..., np.newaxis], train_labels, epochs=5,
          validation_data=(test_images[..., np.newaxis], test_labels))

model.save('digit_recognition_model.h5')
