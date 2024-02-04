import os
from matplotlib import pyplot as plt
import numpy as np
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.layers import Conv2D,MaxPooling2D
from keras.layers import Dense,Dropout,Flatten

"Dataset: https://www.kaggle.com/msambare/fer2013"


train_data='data/train/'
validation_data='data/test/'

train_datagen = ImageDataGenerator(rescale=1./255,rotation_range=30,shear_range=0.3,
                zoom_range=0.3,horizontal_flip=True,fill_mode='nearest')
train_generator = train_datagen.flow_from_directory(train_data,color_mode='grayscale',target_size=(48, 48),
                    batch_size=32,class_mode='categorical',shuffle=True)
validation_datagen = ImageDataGenerator(rescale=1./255)
validation_generator = validation_datagen.flow_from_directory(validation_data,color_mode='grayscale',
                       target_size=(48, 48),batch_size=32,
					   class_mode='categorical',shuffle=True)



class_labels=['Angry','Disgust', 'Fear', 'Happy','Neutral','Sad','Surprise']





model = Sequential()

model.add(Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=(48,48,1)))

model.add(Conv2D(64, kernel_size=(3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.1))

model.add(Conv2D(128, kernel_size=(3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.1))

model.add(Conv2D(256, kernel_size=(3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.1))

model.add(Flatten())
model.add(Dense(512, activation='relu'))
model.add(Dropout(0.2))

model.add(Dense(7, activation='softmax'))

model.compile(optimizer = 'adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

history=model.fit(train_generator,
                epochs=50,
                validation_data=validation_generator,
                )
model.save('emotion detection.h5')
epochs = range(1, len(loss) + 1)
plt.plot(epochs, history.history['loss'], 'y', label='Train loss')
plt.plot(epochs, history.history['val_loss'], 'r', label='Val loss')
plt.title('Train and val loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.show()


plt.plot(epochs, history.history['accuracy'], 'y', label='Train accuracy')
plt.plot(epochs, history.history['val_accuracy'], 'r', label='Val accuracy')
plt.title('Train and val accuracy')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.show()

#Test 

test_image, test_labl = validation_generator.__next__()
predict=model.predict(test_image)
predict= np.argmax(predict, axis=1)
test_lab = np.argmax(test_labl, axis=1)

from sklearn import metrics
print (metrics.accuracy_score(test_lab, predict))
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(test_lab, predict)
import seaborn as sns
sns.heatmap(cm, annot=True)
image = test_img[1]
orig_lab = class_labels[test_lab[1]]
pred_lab = class_labels[predict[1]]
plt.imshow(image[:,:,0], cmap='gray')
plt.show()
