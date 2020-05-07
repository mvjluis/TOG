from keras.models import Sequential
from keras.layers import Convolution2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense

# Initialize CNN
classifier = Sequential()
# Convolution
classifier.add(
    Convolution2D(32, 3, 3, input_shape=(64, 64, 3), activation='relu'))  # use_bias=false,bias_initializer='zeros'
# Pooling
classifier.add(MaxPooling2D(pool_size=(2, 2)))
# Second Layer
classifier.add(Convolution2D(32, 3, 3, activation='relu'))  # use_bias=false,bias_initializer='zeros'
classifier.add(MaxPooling2D(pool_size=(2, 2)))
# Flattening
classifier.add(Flatten())
# Full connection
classifier.add(Dense(output_dim=128, activation='relu'))  # use_bias=false,bias_initializer='zeros'
classifier.add(Dense(output_dim=1, activation='sigmoid'))  # use_bias=false,bias_initializer='zeros'
# Compiling the CNN
classifier.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Fitting the CNN to the images
from keras.preprocessing.image import ImageDataGenerator

train_datagen = ImageDataGenerator(rescale=1. / 255, shear_range=0.2, zoom_range=0.2, horizontal_flip=True)
test_datagen = ImageDataGenerator(rescale=1. / 255)
training_set = train_datagen.flow_from_directory('dataset/training_set', target_size=(64, 64), batch_size=32,
                                                 class_mode='binary')  # class_mode "categorical" when more than 2 classes, "input" when identical
test_set = test_datagen.flow_from_directory('dataset/test_set', target_size=(64, 64), batch_size=32,
                                            class_mode='binary')
classifier.fit_generator(training_set, samples_per_epoch=8000, nb_epoch=2, validation_data=test_set,
                         nb_val_samples=2000)

# Testing CNN
import numpy as np
from keras.preprocessing import image

test_image = image.load_img("images/cat04.jpg", target_size=(64, 64))
test_image = image.img_to_array(test_image)
test_image = np.expand_dims(test_image, axis=0)
result = classifier.predict(test_image)
training_set.class_indices
print(result[0][0], "Is Dog") if result[0][0] >= 0.5 else print(result[0][0], "Is Cat")