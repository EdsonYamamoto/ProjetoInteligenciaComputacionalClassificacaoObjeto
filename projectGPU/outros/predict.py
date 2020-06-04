from keras.models import load_model
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
import numpy


IMG_SIZE = 200
filePath = "C:/Users/T-Gamer/Documents/git/ObjectClassification/projectGPU/Dataset/PRINTS/31.jpg"

# load model
model = load_model('bestmodel.h5')

x = img_to_array(load_img(filePath, target_size=(IMG_SIZE, IMG_SIZE)))
X= []
X.append(x)

X = numpy.asarray(X)

prediction = model.predict( X )
print(prediction)
