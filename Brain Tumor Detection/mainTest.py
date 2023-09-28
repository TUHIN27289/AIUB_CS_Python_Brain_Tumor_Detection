import cv2
from keras.models import load_model
from PIL import Image
import numpy as np
model=load_model('BrainTumor10Epochs.h5')
#model=load_model('BrainTumor10EpochsCategorical.h5')

image=cv2.imread('D:\\python_project_thesis\\Brain Tumor Detection\\pred\\pred5.jpg')
img=Image.fromarray(image)
img=img.resize((64,64))
img=np.array(img)

#print(img)
input_img=np.expand_dims(img, axis=0)
result=model.predict(input_img)
#result=model.predict_classes(img)

print(result)








